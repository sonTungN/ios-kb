#!/usr/bin/env python3
"""
Content linter for data-storage/.

Checks the rules that keep the dataset historically honest and mechanically tense.
This is authoring tooling only — it is not part of the iOS app and nothing here
ships inside the Xcode project.

    python3 tools/validate_data.py content/

Exit code 0 = clean, 1 = problems found.
"""
import json
import pathlib
import sys
from collections import defaultdict

LANGS = ("vi", "en")
errors, warnings = [], []


def err(where, msg):
    errors.append("%s: %s" % (where, msg))


def warn(where, msg):
    warnings.append("%s: %s" % (where, msg))


def check_i18n(where, field, value):
    if not isinstance(value, dict):
        return err(where, "%s is not an i18n object" % field)
    for lang in LANGS:
        text = value.get(lang)
        if not text or not str(text).strip():
            err(where, "%s.%s is empty — every string must ship in both languages" % (field, lang))
        elif "TODO" in str(text):
            err(where, "%s.%s still contains TODO" % (field, lang))


def load(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        err(str(path), "invalid JSON — %s" % e)
        return None


def check_game(root):
    """game.json — difficulty is information and slack, never numbers.

    The player-facing Dễ/Thường/Khó control may change how much the game tells you and
    how much room it leaves. It may not change a starting stat, a choice cost, a flag or
    the victory rule: if it did, a Khó win and a Dễ win would mean different things and
    the level's argument would be a different argument at every setting.
    """
    path = root / "game.json"
    if not path.exists():
        warn(str(root), "no game.json — difficulty, and anything else that is game-wide "
                        "rather than per-dynasty, has nowhere to be declared")
        return
    game = load(path)
    if not game:
        return
    where = str(path)

    pol = game.get("difficultyPolicy") or {}
    allowed = set(pol.get("mayChange") or [])
    fixed = pol.get("neverChanges") or {}
    if not allowed:
        err(where, "difficultyPolicy.mayChange is empty — nothing constrains what a difficulty "
                   "setting is permitted to touch")
    for k in allowed & set(fixed):
        err(where, "'%s' is in both mayChange and neverChanges" % k)
    if "runReview" not in fixed:
        err(where, "runReview is not guaranteed in difficultyPolicy.neverChanges — the run review "
                   "is where a defeat becomes a lesson, so it must not be something a difficulty "
                   "can take away")

    modes = game.get("difficulties") or []
    if len(modes) < 2:
        err(where, "fewer than 2 difficulties declared")

    meta = {"id", "name", "blurb"}
    seen, declared = set(), []
    for m in modes:
        mid = m.get("id")
        mw = "%s difficulty '%s'" % (where, mid)
        if mid in seen:
            err(mw, "duplicate difficulty id")
        seen.add(mid)
        check_i18n(mw, "name", m.get("name", {}))
        check_i18n(mw, "blurb", m.get("blurb", {}))

        for key in m:
            if key in meta or key.startswith("_"):
                continue
            if key in fixed:
                err(mw, "sets '%s', which difficultyPolicy.neverChanges guarantees — a guarantee "
                        "restated per mode is a guarantee waiting to be edited out of one of them"
                    % key)
            elif key not in allowed:
                err(mw, "sets '%s', which is not in difficultyPolicy.mayChange — difficulty "
                        "changes what the player is told and how much slack they get, never "
                        "the numbers, the costs or the win rule" % key)

        for key in allowed:
            if key not in m:
                err(mw, "does not set '%s' — every difficulty must answer every dial, or the "
                        "behaviour falls through to whatever the code happens to default to" % key)
        declared.append(m)

    # a dial that reads the same everywhere is a placebo, not a setting
    for k in sorted(allowed):
        vals = {json.dumps(m.get(k), sort_keys=True) for m in declared}
        if len(vals) == 1 and len(declared) > 1:
            warn(where, "every difficulty sets '%s' to the same value — that dial is declared "
                        "but does nothing; move it to neverChanges or make it vary" % k)


def main(root):
    root = pathlib.Path(root)
    if not root.exists():
        print("No content directory yet at %s — nothing to validate." % root)
        return 0

    dynasties = {}
    for p in sorted(root.glob("**/dynasty.json")) + sorted(root.glob("**/*.dynasty.json")):
        d = load(p)
        if d:
            dynasties[d.get("id")] = (d, p)

    cards = defaultdict(list)
    for p in sorted(root.glob("**/cards/*.json")):
        c = load(p)
        if c:
            cards[c.get("dynastyId")].append((c, p))

    check_game(root)

    if not dynasties:
        print("No dynasty files found under %s." % root)
        return 0

    for did, (dyn, dpath) in dynasties.items():
        where = str(dpath)
        deck = cards.get(did, [])
        by_id = {c.get("id"): (c, p) for c, p in deck}
        stat_ids = {s.get("id") for s in dyn.get("stats", [])}
        flag_ids = {f.get("id") for f in dyn.get("flags", [])}
        counter_ids = {c.get("id") for c in dyn.get("counters", [])}

        check_i18n(where, "lesson", dyn.get("lesson", {}))

        # --- two-sided stat failure ---
        for s in dyn.get("stats", []):
            sw = "%s stat=%s" % (where, s.get("id"))
            if s.get("failHigh") is None:
                err(sw, "no failHigh — an unbounded stat removes all tension")
            if not s.get("failHighText"):
                err(sw, "no failHighText — the max-out failure must have a historical explanation")

        trial = dyn.get("finalTrial", {})
        req_all = trial.get("requireAll", [])

        # --- victory must not be decided by stats ---
        if not req_all:
            err(where, "finalTrial.requireAll is empty — victory would collapse to a stat check")
        if len(req_all) < 2:
            err(where, "finalTrial.requireAll has < 2 flags — the level is a single gate")
        if not trial.get("insufficientAlone"):
            err(where, "finalTrial.insufficientAlone is empty — the level teaches nothing on defeat")
        check_i18n(where, "finalTrial.defeatByStatsText", trial.get("defeatByStatsText", {}))

        # --- the final trial's gate: enough left to fight, never enough to win ---
        #
        # requireAll decides the battle. statGate only asks whether the court can still
        # act at all — holding all three preparations with every stat under 10 is a
        # dynasty that prepared correctly and then collapsed before it could use any of it.
        gate = trial.get("statGate") or {}
        crisis_low = {c.get("stat"): (c.get("trigger") or {}).get("value")
                      for c in dyn.get("crises", [])
                      if (c.get("trigger") or {}).get("when") == "lte"}

        if gate and not trial.get("defeatByExhaustionText"):
            err(where, "finalTrial has a statGate but no defeatByExhaustionText — losing with all "
                       "the preparations in hand is a completely different ending from losing "
                       "without them, and it is the more affecting one. It needs its own text")
        elif gate:
            check_i18n(where, "finalTrial.defeatByExhaustionText",
                       trial.get("defeatByExhaustionText", {}))

        for st, v in gate.items():
            s_def = next((s for s in dyn.get("stats", []) if s.get("id") == st), None)
            if s_def is None:
                err(where, "finalTrial.statGate references undeclared stat '%s'" % st)
                continue
            hi = s_def.get("failHigh", 100)
            if v >= hi * 0.5:
                warn(where, "finalTrial.statGate floors %s at %d, half or more of its %d range — "
                            "that is the trial being decided by stats after all, which is the one "
                            "thing this design exists to avoid. The gate asks whether the court can "
                            "still act, not whether it is strong" % (st, v, hi))
            trigger = crisis_low.get(st)
            if trigger is not None and v >= trigger:
                warn(where, "finalTrial.statGate floors %s at %d, at or above its crisis band (%d) "
                            "— a player can then fail the trial on that stat without ever having "
                            "been offered the rescue that would have warned them. Keep every gate "
                            "below its band so the crisis is always the first signal"
                     % (st, v, trigger))
            if st in trial.get("insufficientAlone", []):
                warn(where, "stat '%s' is both a gate and declared insufficient — coherent "
                            "(necessary to fight, not sufficient to win) but confirm intended" % st)

        for st in sorted(stat_ids - set(gate)):
            warn(where, "stat '%s' has no finalTrial.statGate — it can sit at 1 on the day of the "
                        "battle and the trial will not notice" % st)

        for f in req_all + trial.get("requireAny", []):
            if f not in flag_ids:
                err(where, "finalTrial references undeclared flag '%s'" % f)
        for c in trial.get("requireCounter", {}):
            if c not in counter_ids:
                err(where, "finalTrial references undeclared counter '%s'" % c)

        advisors_before = {it.get("before") for it in dyn.get("interstitials", [])
                           if it.get("type") == "advisor" and it.get("before")}

        # --- every victory flag has a carrier, and that carrier costs something ---
        for flag in dyn.get("flags", []):
            fid, carrier_id = flag.get("id"), flag.get("carrierCardId")

            # a flag with a floor: you need the means to execute the preparation, not the
            # means to win without it. Necessary, never sufficient.
            floor = flag.get("statFloor") or {}
            if floor:
                if not flag.get("blockedText"):
                    err(where, "flag '%s' has a statFloor but no blockedText — a preparation that "
                               "silently fails to land is the cruellest thing this design can do. "
                               "The player must be told what was missing and why it mattered" % fid)
                else:
                    check_i18n(where, "flag '%s'.blockedText" % fid, flag.get("blockedText"))

                if fid in req_all and carrier_id not in advisors_before:
                    err(where, "required flag '%s' has a statFloor but no advisor interstitial "
                               "before its carrier '%s' — a gate the player cannot see coming at "
                               "ANY difficulty is a trap, not a challenge. Khó suppresses advisors "
                               "on purpose; that only works if there is one to suppress"
                        % (fid, carrier_id))

            for st, v in floor.items():
                s_def = next((s for s in dyn.get("stats", []) if s.get("id") == st), None)
                if s_def is None:
                    err(where, "flag '%s' floors undeclared stat '%s'" % (fid, st))
                    continue
                lo = s_def.get("failLow", 0)
                hi = s_def.get("failHigh", 100)
                if v <= lo:
                    err(where, "flag '%s' floors %s at %d, at or below its failLow (%d) — the stat "
                               "is already dead there, so the floor can never bind" % (fid, st, v, lo))
                elif v >= hi:
                    err(where, "flag '%s' floors %s at %d, at or above its failHigh (%d) — "
                               "unreachable without the run ending first" % (fid, st, v, hi))
                elif v > hi * 0.5:
                    warn(where, "flag '%s' floors %s at %d, over half of its %d range — that is a "
                                "THRESHOLD, not a floor. A floor says the court needs the means to "
                                "act; a threshold says it needs to be strong, which is the claim "
                                "finalTrial.insufficientAlone exists to refute. Confirm this is "
                                "meant, and check it does not make a pressure card correct play"
                         % (fid, st, v, hi))

                if st in trial.get("insufficientAlone", []):
                    warn(where, "flag '%s' floors '%s', which is declared insufficientAlone — "
                                "coherent (necessary to act, not sufficient to win) but easy to "
                                "read as a contradiction. Say so in the blocked text" % (fid, st))
                if s_def.get("start") is not None and v > s_def["start"]:
                    warn(where, "flag '%s' floors %s at %d, above its starting value (%d) — the "
                                "player must raise it before the carrier, which is a real design "
                                "choice and not a mistake, but it must be reachable"
                         % (fid, st, v, s_def["start"]))

            # everything below needs the carrier card itself to exist
            if carrier_id not in by_id:
                err(where, "flag '%s' names carrier '%s' which does not exist" % (fid, carrier_id))
                continue
            card, cpath = by_id[carrier_id]
            granting = [ch for ch in card.get("choices", []) if fid in (ch.get("grants") or [])]
            if not granting:
                err(str(cpath), "carrier for flag '%s' has no choice granting it" % fid)
            if fid in req_all:
                for ch in granting:
                    if not any(v < 0 for v in (ch.get("effects") or {}).values()):
                        err(str(cpath),
                            "THE COST RULE: choice granting victory flag '%s' has no negative stat "
                            "effect — the flag becomes a free checkbox" % fid)

            # a flag with a deadline: the window must exist, and must open before it shuts
            deadline = flag.get("expiresBefore")
            if deadline:
                if deadline not in by_id:
                    err(where, "flag '%s' expires before card '%s', which does not exist"
                        % (fid, deadline))
                else:
                    o_carrier = card.get("order")
                    o_deadline = by_id[deadline][0].get("order")
                    if o_carrier is not None and o_deadline is not None and o_carrier >= o_deadline:
                        err(where, "flag '%s' is carried by '%s' (order %s) but expires before '%s' "
                                   "(order %s) — the window shuts at or before it opens, so the "
                                   "flag can never be taken"
                            % (fid, carrier_id, o_carrier, deadline, o_deadline))

        # --- crises: the safety net must be paid for, and must not be infinite ---
        stat_ids = {s["id"] for s in dyn.get("stats", [])}
        seen_crisis = set()
        for cr in dyn.get("crises", []):
            crid, stat = cr.get("id"), cr.get("stat")
            cw = "%s crisis '%s'" % (where, crid)
            if stat not in stat_ids:
                err(cw, "targets undeclared stat '%s'" % stat)
            trig = cr.get("trigger", {})
            if trig.get("when") not in ("lte", "gte"):
                err(cw, "trigger.when must be 'lte' or 'gte'")
            key = (stat, trig.get("when"))
            if key in seen_crisis:
                err(cw, "duplicate crisis for stat '%s' on the same side" % stat)
            seen_crisis.add(key)

            if not cr.get("oncePerLevel"):
                err(cw, "oncePerLevel is not set — a repeatable rescue makes the stat unkillable "
                        "and the two-sided failure model stops meaning anything")

            eff = (cr.get("rescue") or {}).get("effects") or {}
            for st in eff:
                if st not in stat_ids:
                    err(cw, "rescue touches undeclared stat '%s'" % st)
            if not eff:
                err(cw, "rescue has no effects")
            elif not any(v < 0 for v in eff.values()):
                err(cw, "THE COST RULE (crisis): rescue has no negative stat effect — surviving a "
                        "crisis must narrow the board, not reset it")
            elif eff.get(stat, 0) == 0:
                err(cw, "rescue does not move the stat it rescues ('%s')" % stat)

            if cr.get("historicity") not in ("documented", "simplified", "invented"):
                err(cw, "historicity must be documented / simplified / invented (Report §2 buckets)")

        # every stat should be rescuable on both sides, or the danger band is a silent death sentence
        for st in sorted(stat_ids):
            for side in ("lte", "gte"):
                if (st, side) not in seen_crisis:
                    warn(where, "stat '%s' has no '%s' crisis — that edge kills with no way back" % (st, side))

        # --- ambient: relief that must stay small, positive, and capped ---
        pol = dyn.get("ambientPolicy") or {}
        cap_abs = pol.get("maxAbsEffect", 8)
        cap_n = pol.get("maxPerLevel", 5)
        cap_total = pol.get("totalGainMustStayUnder")
        nets, seen_amb = [], set()
        for am in dyn.get("ambient", []):
            aid = am.get("id")
            aw = "%s ambient '%s'" % (where, aid)
            if aid in seen_amb:
                err(aw, "duplicate ambient id")
            seen_amb.add(aid)
            check_i18n(aw, "name", am.get("name", {}))
            check_i18n(aw, "text", am.get("text", {}))
            eff = am.get("effects") or {}
            if not eff:
                err(aw, "has no effects — an ambient beat with no stat movement is an interstitial, "
                        "declare it there instead")
            for st, v in eff.items():
                if st not in stat_ids:
                    err(aw, "touches undeclared stat '%s'" % st)
                if abs(v) > cap_abs:
                    err(aw, "effect %s %+d exceeds ambientPolicy.maxAbsEffect (%d) — ambient beats are "
                            "small years, not turning points" % (st, v, cap_abs))
            if am.get("grants"):
                err(aw, "grants a flag — victory preparations must come from carrier cards, never "
                        "from a beat the player cannot decline")
            if am.get("historicity") not in ("documented", "simplified", "invented"):
                err(aw, "historicity must be documented / simplified / invented (Report §2 buckets)")
            net = sum(eff.values())
            if net <= 0:
                warn(aw, "net %+d — ambient beats exist to relieve the downward curve; a non-positive "
                         "one just adds length" % net)
            nets.append(net)

        if nets and cap_total is not None:
            worst = sum(sorted(nets, reverse=True)[:cap_n])
            if worst >= cap_total:
                err(where, "the %d most generous ambient beats total %+d, at or above "
                           "ambientPolicy.totalGainMustStayUnder (%d) — relief on that scale cancels "
                           "the carriers' cost and the sacrifice stops being a sacrifice"
                    % (cap_n, worst, cap_total))
        if dyn.get("ambient") and not pol:
            err(where, "ambient beats declared with no ambientPolicy — nothing caps how often they "
                       "fire or how much they give back")

        # --- weave: undated court business, drawn per run ---
        #
        # The spine (cards/) is dated history and never moves. The weave is period texture
        # with no date, drawn fresh each run. Three things must hold or randomising it
        # stops being safe: it must not claim a date, it must not carry the level's
        # argument, and no draw may change whether the level can be won.
        wpol = dyn.get("weavePolicy") or {}
        slots = wpol.get("slotsPerAct") or {}
        w_cap = wpol.get("maxAbsEffect", 10)
        swing_budget = wpol.get("maxWorstCaseSwing") or {}
        by_act = defaultdict(list)
        seen_weave = set()

        for wv in dyn.get("weave", []):
            wid, act = wv.get("id"), wv.get("act")
            ww = "%s weave '%s'" % (where, wid)
            if wid in seen_weave:
                err(ww, "duplicate weave id")
            seen_weave.add(wid)
            if wid in by_id:
                err(ww, "id collides with a spine card in cards/ — a card is either dated "
                        "history or undated texture, never both")

            if act not in slots:
                err(ww, "act '%s' is not in weavePolicy.slotsPerAct" % act)
            elif slots.get(act, 0) < 1:
                err(ww, "act '%s' has 0 slots — this card can never be drawn" % act)
            else:
                by_act[act].append(wv)

            # the whole licence to shuffle rests on this field being null
            if wv.get("year") is not None:
                err(ww, "has year %s — a weave card is shuffled into an act, so a date on it "
                        "would be a claim the game then contradicts by moving it. Give it a "
                        "date and it belongs in cards/ as spine." % wv.get("year"))

            for ch in wv.get("choices", []):
                for fl in (ch.get("grants") or []):
                    if fl in req_all:
                        err(ww, "grants required victory flag '%s' — the three preparations are "
                                "the level's argument and must land on dated cards every run, "
                                "not depend on a draw" % fl)
                    elif fl not in flag_ids:
                        err(ww, "references undeclared flag '%s'" % fl)

            choices = wv.get("choices", [])
            if len(choices) != 2:
                err(ww, "expected exactly 2 choices, found %d" % len(choices))
            check_i18n(ww, "prompt", wv.get("prompt", {}))
            check_i18n(ww, "historicalNote", wv.get("historicalNote", {}))
            for i, ch in enumerate(choices):
                check_i18n(ww, "choices[%d].label" % i, ch.get("label", {}))
                check_i18n(ww, "choices[%d].outcome" % i, ch.get("outcome", {}))
                for st, v in (ch.get("effects") or {}).items():
                    if st not in stat_ids:
                        err(ww, "choices[%d] affects undeclared stat '%s'" % (i, st))
                    elif abs(v) > w_cap:
                        err(ww, "choices[%d] moves %s %+d, over weavePolicy.maxAbsEffect (%d) — "
                                "a card that can land anywhere must not be able to decide the run"
                            % (i, st, v, w_cap))

            if wv.get("historicity") not in ("documented", "simplified", "invented"):
                err(ww, "historicity must be documented / simplified / invented (Report §2 buckets)")
            elif wv.get("historicity") == "documented":
                err(ww, "historicity 'documented' on an undated card — if the record documents it, "
                        "the record dates it, and it belongs in the spine")
            if not wv.get("sources"):
                warn(ww, "no sources — a weave card cites the *practice* it typifies, not an event, "
                         "so one citation per theme is enough; it is still owed")

        # THE SOLVENCY INVARIANT — the draw may change the run, never its winnability.
        # For each stat: assume the player takes the kindest branch of every card drawn,
        # then hand them the cruellest draw the slot counts allow. That floor must stay
        # inside the budget. Same again on the high side, where overshoot kills instead.
        if by_act and swing_budget:
            for st in sorted(stat_ids):
                budget = swing_budget.get(st)
                if budget is None:
                    warn(where, "weavePolicy.maxWorstCaseSwing has no entry for stat '%s' — that "
                                "stat's exposure to the draw is unchecked" % st)
                    continue
                floor = ceil = 0
                for act, pool in by_act.items():
                    n = slots.get(act, 0)
                    best = sorted(max((ch.get("effects") or {}).get(st, 0)
                                      for ch in wv.get("choices", []) or [{}]) for wv in pool)
                    worst = sorted(min((ch.get("effects") or {}).get(st, 0)
                                       for ch in wv.get("choices", []) or [{}]) for wv in pool)
                    floor += sum(best[:n])
                    ceil += sum(worst[-n:]) if n else 0
                if floor < -budget:
                    err(where, "SOLVENCY: the harshest legal draw costs %s %+d even played "
                               "perfectly, past maxWorstCaseSwing (%d) — the shuffle would decide "
                               "whether the level is winnable, which is exactly what it must not do"
                        % (st, floor, budget))
                if ceil > budget:
                    err(where, "SOLVENCY: the most generous legal draw pushes %s %+d, past "
                               "maxWorstCaseSwing (%d) — overshoot is a failure state too, and the "
                               "draw must not be able to cause it" % (st, ceil, budget))

        for act, n in sorted(slots.items()):
            pool = len(by_act.get(act, []))
            if n and pool < n:
                err(where, "act %s draws %d weave cards from a pool of %d" % (act, n, pool))
            elif n and pool == n:
                warn(where, "act %s draws %d from a pool of %d — every run sees the same set, "
                            "so the slot costs content and buys no variety" % (act, n, pool))

        # --- interstitials: pacing beats carry no stat effects ---
        for it in dyn.get("interstitials", []):
            iw = "%s interstitial %s" % (where, it.get("type"))
            if it.get("type") not in ("advisor", "omen", "echo", "chapter"):
                err(iw, "unknown interstitial type '%s'" % it.get("type"))
            if it.get("type") == "chapter" and not (it.get("before") and it.get("title")):
                err(iw, "a chapter banner needs 'before' (the card it precedes) and a 'title' — "
                        "it is the era turn made visible, not a decoration")
            if it.get("effects"):
                err(iw, "interstitials must not carry stat effects — they are information, not decisions")
            anchor = it.get("before") or it.get("after")
            if anchor and by_id and anchor not in by_id:
                err(iw, "anchors to card '%s' which does not exist" % anchor)

        # --- the ledger must track exactly the required flags ---
        ledger = dyn.get("ledger")
        if ledger is not None:
            slots = ledger.get("slots", [])
            if sorted(slots) != sorted(req_all):
                err(where, "ledger.slots %s does not match finalTrial.requireAll %s — the player would "
                           "be shown a goal that is not the goal" % (sorted(slots), sorted(req_all)))
            if ledger.get("hintPolicy") != "when-not-what":
                warn(where, "ledger.hintPolicy is not 'when-not-what' — hints that name the choice "
                            "remove the decision the level is built on")

        # --- per-card checks ---
        seen_order = {}
        for card, cpath in deck:
            cw = str(cpath)
            cid = card.get("id")
            if not card.get("sources"):
                err(cw, "no sources — every card must be traceable")
            for s in card.get("sources", []):
                if s.get("type") == "encyclopedia":
                    warn(cw, "only-encyclopedia sourcing is weak for the report; find a primary or scholarly source")
            hist = card.get("historicity")
            if hist not in ("documented", "simplified", "invented"):
                err(cw, "historicity must be documented|simplified|invented (feeds Report section 2)")
            if card.get("year") is None:
                err(cw, "no year — everything in cards/ is spine: it holds a fixed position "
                        "because a date holds it there. Undated content belongs in the weave "
                        "pool in dynasty.json, where it can be drawn and shuffled safely.")

            check_i18n(cw, "prompt", card.get("prompt", {}))
            check_i18n(cw, "historicalNote", card.get("historicalNote", {}))

            choices = card.get("choices", [])
            if len(choices) != 2:
                err(cw, "expected exactly 2 choices, found %d" % len(choices))
            for i, ch in enumerate(choices):
                check_i18n(cw, "choices[%d].label" % i, ch.get("label", {}))
                check_i18n(cw, "choices[%d].outcome" % i, ch.get("outcome", {}))
                for st in (ch.get("effects") or {}):
                    if st not in stat_ids:
                        err(cw, "choices[%d] affects undeclared stat '%s'" % (i, st))
                for fl in (ch.get("grants") or []) + (ch.get("revokes") or []):
                    if fl not in flag_ids:
                        err(cw, "choices[%d] references undeclared flag '%s'" % (i, fl))

            # chronology: order must agree with year
            o, y = card.get("order"), card.get("year")
            if o is not None and y is not None:
                seen_order[o] = (y, cid)

        ordered = sorted(seen_order.items())
        for (o1, (y1, id1)), (o2, (y2, id2)) in zip(ordered, ordered[1:]):
            if y2 < y1:
                err(where, "chronology broken: '%s' (order %s, year %s) precedes '%s' (order %s, year %s)"
                    % (id1, o1, y1, id2, o2, y2))

        # --- scope signal ---
        if deck and len(deck) < 20:
            warn(where, "only %d cards — a level tends to feel thin below ~25" % len(deck))

    for w in warnings:
        print("WARN  %s" % w)
    for e in errors:
        print("ERROR %s" % e)
    print("\n%d error(s), %d warning(s)" % (len(errors), len(warnings)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "content"))
