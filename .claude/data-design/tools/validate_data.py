#!/usr/bin/env python3
"""
Content linter for data-design/.

Validates the data against schema/*.json, then checks the design rules that keep the
dataset historically honest and mechanically tense.
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


SCHEMA_DIR = pathlib.Path(__file__).resolve().parent.parent / "schema"


def check_schema(kind, doc, path):
    """Enforce the JSON Schema contract itself.

    The rules further down check the *design*; this checks the *shape*. Without it
    the schema is documentation nobody runs, and a Swift decoder written against it
    is the first thing to discover the data never matched. Keys beginning with '_'
    are authoring annotations and are allowed everywhere by the schemas.
    """
    try:
        import jsonschema
    except ImportError:
        warn(str(path), "jsonschema is not installed, so schema/%s.schema.json was NOT enforced "
                        "(pip3 install jsonschema)" % kind)
        return
    sf = SCHEMA_DIR / ("%s.schema.json" % kind)
    if not sf.exists():
        return err(str(path), "schema/%s.schema.json is missing" % kind)
    try:
        schema = json.loads(sf.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return err(str(sf), "invalid JSON — %s" % e)
    for e in sorted(jsonschema.Draft7Validator(schema).iter_errors(doc),
                    key=lambda x: list(x.path)):
        err("%s at %s" % (path, "/".join(map(str, e.path)) or "<root>"),
            "schema — %s" % e.message)


def check_effect_reasons(where, choice, stat_ids):
    """Every nonzero effect must say WHY — one bilingual chip per stat.

    The number tells the player what moved; the chip tells them why their choice
    moved it. A delta with no reason reads as the game taxing them at random,
    which is exactly the feeling this design must never produce. Chips are chips:
    <= ~60 chars per language, not sentences.
    """
    effects = {k for k, v in (choice.get("effects") or {}).items() if v}
    reasons = choice.get("effectReasons") or {}
    for st in effects:
        r = reasons.get(st)
        if not isinstance(r, dict) or not r.get("vi") or not r.get("en"):
            err(where, "effect on '%s' has no effectReasons chip (vi+en) — a stat that moves "
                       "without a why reads as a random tax, not a consequence" % st)
        else:
            for lang in LANGS:
                t = str(r.get(lang, ""))
                if "TODO" in t:
                    err(where, "effectReasons.%s.%s still contains TODO" % (st, lang))
                elif len(t) > 60:
                    warn(where, "effectReasons.%s.%s is %d chars — that is a sentence, not a "
                                "chip. The outcome text carries the story; the chip carries "
                                "the cause" % (st, lang, len(t)))
    for st in reasons:
        if st not in effects:
            err(where, "effectReasons names '%s' but the choice has no nonzero effect on it "
                       "— an orphaned reason explains nothing" % st)


def check_dominance(where, choices, get_extras):
    """THE TRADE RULE: a choice may beat its pair on every stat only by paying in flags.

    If one side is >= the other on every declared stat AND carries the same
    grants/revokes/counters, the other side is a dead option and the card asks
    nothing. The two shipped stat-dominant spine pairs are legal precisely
    because their dominance is the trap: card 11 pays +25 sinh_ke but revokes
    giu_van; card 33's cheap side skips the required ho_so.
    """
    if len(choices) != 2:
        return
    a, b = choices
    stats = set((a.get("effects") or {})) | set((b.get("effects") or {}))
    if not stats:
        return
    av = [(a.get("effects") or {}).get(s, 0) for s in sorted(stats)]
    bv = [(b.get("effects") or {}).get(s, 0) for s in sorted(stats)]
    if av == bv:
        return
    a_dom = all(x >= y for x, y in zip(av, bv))
    b_dom = all(x <= y for x, y in zip(av, bv))
    if (a_dom or b_dom) and get_extras(a) == get_extras(b):
        err(where, "one choice dominates the other on every stat with identical "
                   "grants/revokes/counters — the losing side is a dead option. Either give "
                   "the dominant side a flag price (that is what makes a trap a trap) or "
                   "make the numbers trade")


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
    the victory rule: if it lid, a Khó win and a Dễ win would mean different things and
    the level's argument would be a different argument at every setting.
    """
    path = root / "game.json"
    if not path.exists():
        warn(str(root), "no game.json — difficulty, and anything else that is game-wide "
                        "rather than per-level, has nowhere to be declared")
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

    levels = {}
    for p in sorted(root.glob("**/game_contents.json")) + sorted(root.glob("**/*.game_contents.json")):
        d = load(p)
        if d:
            check_schema("level", d, p)
            levels[d.get("id")] = (d, p)

    cards = defaultdict(list)
    for p in sorted(root.glob("**/cards/*.json")):
        c = load(p)
        if c:
            check_schema("card", c, p)
            cards[c.get("levelId")].append((c, p))
    # the spine ships as one file per level: {"levelId", "cards": [card, ...]}
    for p in sorted(root.glob("**/game_spine.json")):
        f = load(p)
        if not f:
            continue
        for i, c in enumerate(f.get("cards") or []):
            cp = pathlib.Path("%s#%s" % (p, c.get("id") or i))
            check_schema("card", c, cp)
            if c.get("levelId") != f.get("levelId"):
                err(str(cp), "levelId '%s' differs from the file's '%s'" % (c.get("levelId"), f.get("levelId")))
            cards[c.get("levelId")].append((c, cp))
        seen = [c.get("id") for c in f.get("cards") or []]
        for cid in set(seen):
            if seen.count(cid) > 1:
                err(str(p), "duplicate card id '%s'" % cid)
        orders = [c.get("order") for c in f.get("cards") or []]
        if orders != sorted(orders):
            warn(str(p), "cards are not listed in order; the app sorts, but a reader will not")

    check_game(root)

    if not levels:
        print("No level files (game_contents.json) found under %s." % root)
        return 0

    for lid, (lvl, dpath) in levels.items():
        where = str(dpath)
        deck = cards.get(lid, [])
        by_id = {c.get("id"): (c, p) for c, p in deck}
        stat_ids = {s.get("id") for s in lvl.get("stats", [])}
        flag_ids = {f.get("id") for f in lvl.get("flags", [])}
        counter_ids = {c.get("id") for c in lvl.get("counters", [])}

        check_i18n(where, "lesson", lvl.get("lesson", {}))

        # --- two-sided stat failure ---
        for s in lvl.get("stats", []):
            sw = "%s stat=%s" % (where, s.get("id"))
            if s.get("failHigh") is None:
                err(sw, "no failHigh — an unbounded stat removes all tension")
            if not s.get("failHighText"):
                err(sw, "no failHighText — the max-out failure must have a historical explanation")

        trial = lvl.get("finalTrial", {})
        req_all = trial.get("requireAll", [])

        # --- victory must not be decided by stats ---
        if not req_all:
            err(where, "finalTrial.requireAll is empty — victory would collapse to a stat check")
        if len(req_all) < 2:
            err(where, "finalTrial.requireAll has < 2 flags — the level is a single gate")
        if not trial.get("insufficientAlone"):
            err(where, "finalTrial.insufficientAlone is empty — the level teaches nothing on defeat")
        check_i18n(where, "finalTrial.defeatByStatsText", trial.get("defeatByStatsText", {}))

        # --- the final trial's gate: enough left to act, never enough to win ---
        #
        # requireAll decides the outcome. statGate only asks whether the household can still
        # act at all — holding all three preparations with every stat under 10 is a
        # household that prepared correctly and then collapsed before it could use any of it.
        gate = trial.get("statGate") or {}
        crisis_low = {c.get("stat"): (c.get("trigger") or {}).get("value")
                      for c in lvl.get("crises", [])
                      if (c.get("trigger") or {}).get("when") == "lte"}

        if gate and not trial.get("defeatByExhaustionText"):
            err(where, "finalTrial has a statGate but no defeatByExhaustionText — losing with all "
                       "the preparations in hand is a completely different ending from losing "
                       "without them, and it is the more affecting one. It needs its own text")
        elif gate:
            check_i18n(where, "finalTrial.defeatByExhaustionText",
                       trial.get("defeatByExhaustionText", {}))

        for st, v in gate.items():
            s_def = next((s for s in lvl.get("stats", []) if s.get("id") == st), None)
            if s_def is None:
                err(where, "finalTrial.statGate references undeclared stat '%s'" % st)
                continue
            hi = s_def.get("failHigh", 100)
            if v >= hi * 0.5:
                warn(where, "finalTrial.statGate floors %s at %d, half or more of its %d range — "
                            "that is the trial being decided by stats after all, which is the one "
                            "thing this design exists to avoid. The gate asks whether the household can "
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
                            "(necessary to act, not sufficient to win) but confirm intended" % st)

        for st in sorted(stat_ids - set(gate)):
            warn(where, "stat '%s' has no finalTrial.statGate — it can sit at 1 on the day of the "
                        "trial and the trial will not notice" % st)

        for f in req_all + trial.get("requireAny", []):
            if f not in flag_ids:
                err(where, "finalTrial references undeclared flag '%s'" % f)
        for c in trial.get("requireCounter", {}):
            if c not in counter_ids:
                err(where, "finalTrial references undeclared counter '%s'" % c)

        advisors_before = {it.get("before") for it in lvl.get("interstitials", [])
                           if it.get("type") == "advisor" and it.get("before")}

        # --- every victory flag has a carrier, and that carrier costs something ---
        for flag in lvl.get("flags", []):
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
                s_def = next((s for s in lvl.get("stats", []) if s.get("id") == st), None)
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
                                "THRESHOLD, not a floor. A floor says the household needs the means to "
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

            # a flag may offer a second, dearer door later in the spine
            for alt_id in flag.get("alternateCarrierCardIds") or []:
                if alt_id not in by_id:
                    err(where, "flag '%s' names alternate carrier '%s' which does not exist"
                        % (fid, alt_id))
                    continue
                alt_card, alt_path = by_id[alt_id]
                alt_grant = [ch for ch in alt_card.get("choices", [])
                             if fid in (ch.get("grants") or [])]
                if not alt_grant:
                    err(str(alt_path), "alternate carrier for flag '%s' has no choice granting it"
                        % fid)
                if (alt_card.get("order") is not None and by_id.get(carrier_id)
                        and by_id[carrier_id][0].get("order") is not None
                        and alt_card["order"] <= by_id[carrier_id][0]["order"]):
                    err(where, "flag '%s' lists '%s' as an alternate carrier, but it is not later "
                               "than the primary carrier '%s' — a last chance has to come last"
                        % (fid, alt_id, carrier_id))
                for ch in alt_grant:
                    prim = by_id.get(carrier_id)
                    if not prim:
                        continue
                    p_cost = min((sum(v for v in (c.get("effects") or {}).values() if v < 0)
                                  for c in prim[0].get("choices", [])
                                  if fid in (c.get("grants") or [])), default=0)
                    a_cost = sum(v for v in (ch.get("effects") or {}).values() if v < 0)
                    if a_cost >= p_cost:
                        err(str(alt_path),
                            "the second chance at flag '%s' costs %d, no more than the first (%d) — "
                            "a cheap last chance deletes the deadline it is supposed to enforce"
                            % (fid, a_cost, p_cost))

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
        stat_ids = {s["id"] for s in lvl.get("stats", [])}
        seen_crisis = set()
        for cr in lvl.get("crises", []):
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

            if not cr.get("oncePerRun"):
                err(cw, "oncePerRun is not set — a repeatable rescue makes the stat unkillable "
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

            check_effect_reasons("%s rescue" % cw, cr.get("rescue") or {}, stat_ids)
            check_effect_reasons("%s refuse" % cw, cr.get("refuse") or {}, stat_ids)

            if cr.get("historicity") not in ("documented", "simplified", "invented"):
                err(cw, "historicity must be documented / simplified / invented (Report §2 buckets)")

        # every stat should be rescuable on both sides, or the danger band is a silent death sentence
        for st in sorted(stat_ids):
            for side in ("lte", "gte"):
                if (st, side) not in seen_crisis:
                    warn(where, "stat '%s' has no '%s' crisis — that edge kills with no way back" % (st, side))

        # --- ambient: relief that must stay small, positive, and capped ---
        pol = lvl.get("ambientPolicy") or {}
        cap_abs = pol.get("maxAbsEffect", 8)
        cap_n = pol.get("maxPerRun", 5)
        cap_total = pol.get("totalGainMustStayUnder")
        nets, seen_amb = [], set()
        for am in lvl.get("ambient", []):
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
            # ambient is drawn too, so the NGƯỜI-is-never-weather law binds it as well:
            # a beat that moves nguoi must be scheduled inside chapter I only
            a_chap = am.get("chapter")
            if a_chap is not None and a_chap not in ("C1", "C2", "C3"):
                err(aw, "chapter '%s' is not C1/C2/C3" % a_chap)
            if eff.get("nguoi") and a_chap != "C1":
                err(aw, "moves nguoi but is not restricted to chapter C1 — after chapter I the "
                        "draw may never move NGƯỜI (design/game_strategy_and_logic.md §3)")
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
        if lvl.get("ambient") and not pol:
            err(where, "ambient beats declared with no ambientPolicy — nothing caps how often they "
                       "fire or how much they give back")

        # --- weave: undated ordinary business, drawn per run ---
        #
        # The spine (cards/) is dated history and never moves. The weave is period texture
        # with no date, drawn fresh each run. Three things must hold or randomising it
        # stops being safe: it must not claim a date, it must not carry the level's
        # argument, and no draw may change whether the level can be won.
        wpol = lvl.get("weavePolicy") or {}
        slots = wpol.get("slotsPerChapter") or {}
        w_cap = wpol.get("maxAbsEffect", 10)
        swing_budget = wpol.get("maxWorstCaseSwing") or {}
        by_chapter = defaultdict(list)
        seen_weave = set()

        for wv in lvl.get("weave", []):
            wid, chap = wv.get("id"), wv.get("chapter")
            ww = "%s weave '%s'" % (where, wid)
            if wid in seen_weave:
                err(ww, "duplicate weave id")
            seen_weave.add(wid)
            if wid in by_id:
                err(ww, "id collides with a spine card in cards/ — a card is either dated "
                        "history or undated texture, never both")

            if chap not in slots:
                err(ww, "chapter '%s' is not in weavePolicy.slotsPerChapter" % chap)
            elif slots.get(chap, 0) < 1:
                err(ww, "chapter '%s' has 0 slots — this card can never be drawn" % chap)
            else:
                by_chapter[chap].append(wv)

            # the whole licence to shuffle rests on this field being null
            if wv.get("year") is not None:
                err(ww, "has year %s — a weave card is shuffled into a chapter, so a date on it "
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
                check_effect_reasons("%s choices[%d]" % (ww, i), ch, stat_ids)
                # transmission is the subject, and the subject is never weather:
                # from chapter II on, who stays and who leaves moves only on dated
                # decisions and ticks — a drawn card may not touch NGƯỜI there
                if chap in ("C2", "C3") and (ch.get("effects") or {}).get("nguoi"):
                    err(ww, "choices[%d] moves nguoi in %s — after chapter I the draw may "
                            "never move NGƯỜI; transmission changes only on dated decisions "
                            "(see design/game_strategy_and_logic.md §3)" % (i, chap))
            check_dominance(ww, choices,
                            lambda c: (tuple(c.get("grants") or []),
                                       tuple(c.get("revokes") or []),
                                       tuple(sorted((c.get("counters") or {}).items()))))

            # Reigns-style eligibility: a weave card may declare when it no longer
            # fits the run's state. Filtering only ever REMOVES cards from the bag,
            # so the solvency proof over the full pool still bounds every draw.
            cond = wv.get("conditions")
            if cond is not None:
                if not isinstance(cond, dict) or not set(cond) <= {"allOf", "anyOf", "noneOf"}:
                    err(ww, "conditions must be an object with only allOf/anyOf/noneOf lists")
                else:
                    for k, toks in cond.items():
                        for t in toks if isinstance(toks, list) else [toks]:
                            if not isinstance(t, str) or not (t in flag_ids or t.startswith("chose:")):
                                err(ww, "conditions.%s token '%s' is neither a declared flag id "
                                        "nor a chose:<tag> choice memory" % (k, t))

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
        if by_chapter and swing_budget:
            for st in sorted(stat_ids):
                budget = swing_budget.get(st)
                if budget is None:
                    warn(where, "weavePolicy.maxWorstCaseSwing has no entry for stat '%s' — that "
                                "stat's exposure to the draw is unchecked" % st)
                    continue
                floor = ceil = 0
                for chap, pool in by_chapter.items():
                    n = slots.get(chap, 0)
                    best = sorted(max((ch.get("effects") or {}).get(st, 0)
                                      for ch in wv.get("choices", []) or [{}]) for wv in pool)
                    worst = sorted(min((ch.get("effects") or {}).get(st, 0)
                                       for ch in wv.get("choices", []) or [{}]) for wv in pool)
                    # a `conditions`-filtered slot can deal nothing at all, so the
                    # bound must cover the skip: a slot's worst contribution is the
                    # harsher of "the cruellest card" and "no card" (0), and its most
                    # generous contribution the kinder of "the kindest card" and 0.
                    floor += sum(min(0, v) for v in best[:n])
                    ceil += (sum(max(0, v) for v in worst[-n:]) if n else 0)
                if floor < -budget:
                    err(where, "SOLVENCY: the harshest legal draw costs %s %+d even played "
                               "perfectly, past maxWorstCaseSwing (%d) — the shuffle would decide "
                               "whether the level is winnable, which is exactly what it must not do"
                        % (st, floor, budget))
                if ceil > budget:
                    err(where, "SOLVENCY: the most generous legal draw pushes %s %+d, past "
                               "maxWorstCaseSwing (%d) — overshoot is a failure state too, and the "
                               "draw must not be able to cause it" % (st, ceil, budget))

        for chap, n in sorted(slots.items()):
            pool = len(by_chapter.get(chap, []))
            if n and pool < n:
                err(where, "chapter %s draws %d weave cards from a pool of %d" % (chap, n, pool))
            elif n and pool == n:
                warn(where, "chapter %s draws %d from a pool of %d — every run sees the same set, "
                            "so the slot costs content and buys no variety" % (chap, n, pool))

        # --- interstitials: pacing beats carry no stat effects ---
        for it in lvl.get("interstitials", []):
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
        ledger = lvl.get("ledger")
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
                        "pool in game_contents.json, where it can be drawn and shuffled safely.")

            if cid == "07-lang-chay" and card.get("showYear", True):
                err(cw, "showYear must be false — the burning year is unsourced (research register #3) "
                        "and must never be printed in a player facing string")
            check_i18n(cw, "title", card.get("title", {}))
            for lang, text in (card.get("title") or {}).items():
                if isinstance(text, str) and len(text.split()) > 7:
                    warn(cw, "title.%s runs to %d words — a title names the moment, the prompt tells it"
                         % (lang, len(text.split())))
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
                check_effect_reasons("%s choices[%d]" % (cw, i), ch, stat_ids)
            check_dominance(cw, choices,
                            lambda c: (tuple(c.get("grants") or []),
                                       tuple(c.get("revokes") or []),
                                       tuple(sorted((c.get("counters") or {}).items()))))

            # chronology: order must agree with year
            o, y = card.get("order"), card.get("year")
            if o is not None and y is not None:
                seen_order[o] = (y, cid)

        ordered = sorted(seen_order.items())
        for (o1, (y1, id1)), (o2, (y2, id2)) in zip(ordered, ordered[1:]):
            if y2 < y1:
                err(where, "chronology broken: '%s' (order %s, year %s) precedes '%s' (order %s, year %s)"
                    % (id1, o1, y1, id2, o2, y2))

        # --- checks that activate as the deck lands (silent on an empty deck) ---
        if deck:
            # chapter windows come from the chapter banners' `before` anchors —
            # each names the card id that opens the next chapter, so the boundary
            # order is that card's own order (resolvable exactly when cards exist)
            bounds = sorted(by_id[b][0].get("order")
                            for it in lvl.get("interstitials", [])
                            if it.get("type") == "chapter"
                            for b in [it.get("before")]
                            if b in by_id and by_id[b][0].get("order") is not None)

            def chap_of(order):
                c = 1
                for b in bounds:
                    if order is not None and order >= b:
                        c += 1
                return "C%d" % c

            # 3 · FAUCETS AND DRAINS (design/game_strategy_and_logic.md §3 law 1):
            # every stat must be both earnable and losable in every chapter, spine
            # and weave together. Mirrors trace_run.py --audit; this copy runs on
            # the real data files so the law survives the mirror.
            flow = {}
            for card, cpath in deck:
                c = chap_of(card.get("order"))
                for ch in card.get("choices", []):
                    for st, v in (ch.get("effects") or {}).items():
                        f = flow.setdefault(c, {}).setdefault(st, [0, 0])
                        f[0 if v > 0 else 1] += v
            for wv in lvl.get("weave", []):
                for ch in wv.get("choices", []):
                    for st, v in (ch.get("effects") or {}).items():
                        f = flow.setdefault(wv.get("chapter"), {}).setdefault(st, [0, 0])
                        f[0 if v > 0 else 1] += v
            # only judge a chapter once a meaningful share of its spine exists
            counts = {}
            for card, cpath in deck:
                c = chap_of(card.get("order"))
                counts[c] = counts.get(c, 0) + 1
            full = {"C1": 12, "C2": 10, "C3": 14}
            for c, n in sorted(counts.items()):
                if n < full.get(c, 12):
                    continue
                for st in sorted(stat_ids):
                    pos, neg = flow.get(c, {}).get(st, [0, 0])
                    if pos == 0 or neg == 0:
                        err(where, "chapter %s has no %s for stat '%s' — a stat that only %s "
                                   "in a chapter is a script, not a resource"
                            % (c, "faucet" if pos == 0 else "drain", st,
                               "drains" if pos == 0 else "rises"))

            # 4 · the chose:<tag> vocabulary must resolve to real spine choices
            declared = {}
            for card, cpath in deck:
                for ch in card.get("choices", []):
                    t = ch.get("tag")
                    if t:
                        declared.setdefault(t, []).append(card.get("id"))
            for t, owners in declared.items():
                if len(owners) > 1:
                    err(where, "choice tag '%s' is declared by %s — a memory must have exactly "
                               "one source" % (t, owners))
            referenced = set()
            for wv in lvl.get("weave", []):
                for toks in (wv.get("conditions") or {}).values():
                    for t in toks if isinstance(toks, list) else [toks]:
                        if isinstance(t, str) and t.startswith("chose:"):
                            referenced.add((t[6:], "weave '%s'" % wv.get("id")))
            for it in lvl.get("interstitials", []):
                cond = it.get("condition")
                if isinstance(cond, str) and cond.startswith("chose:"):
                    referenced.add((cond[6:], "interstitial '%s'" % it.get("type")))
            for t, src in sorted(referenced):
                if t not in declared:
                    err(where, "%s references chose:%s but no spine choice declares tag '%s'"
                        % (src, t, t))

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
