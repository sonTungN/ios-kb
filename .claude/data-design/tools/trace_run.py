#!/usr/bin/env python3
"""Reachability / balance search for the single-run Đông Hồ spine (36 cards).

Beam-searches the choice space (2 choices x 36 cards, plus accept/refuse on
crisis offers) and reports whether winning lines exist on Thường (crises on)
and Khó (no crises), which bands they touch, and a canonical best line.

The card table below MUST mirror content/dongho/level-map.md — when the map's
numbers change, change them here and re-run. This script is the reachability
pass every level map owes before its numbers are trusted.

Usage: python3 tools/trace_run.py
"""

START = {"nghe": 60, "sinh_ke": 50, "tieng": 55, "nguoi": 50}
STATS = ["nghe", "sinh_ke", "tieng", "nguoi"]
BAND_LO, BAND_HI = 20, 80          # Thường crisis bands
GATE = {"nghe": 15, "sinh_ke": 10, "tieng": 10, "nguoi": 15}

# rescue effects per stat-side (mirrors game_contents.json crises)
CRISES = {
    ("sinh_ke", "lo"): {"sinh_ke": 25, "tieng": -10},
    ("sinh_ke", "hi"): {"sinh_ke": -20, "tieng": -5},
    ("nghe", "lo"): {"nghe": 20, "sinh_ke": -15},
    ("nghe", "hi"): {"nghe": -20, "tieng": -5},
    ("tieng", "lo"): {"tieng": 20, "sinh_ke": -15},
    ("tieng", "hi"): {"tieng": -20, "sinh_ke": -10},
    ("nguoi", "lo"): {"nguoi": 20, "sinh_ke": -15},
    ("nguoi", "hi"): {"nguoi": -20, "tieng": -5},
}

def E(n, s, t, g):
    return {"nghe": n, "sinh_ke": s, "tieng": t, "nguoi": g}

# id, chapter, A-effects, B-effects, extras:
#   grantsA/revokesA/tickA, floor=(stat,val) applies to choice A's grant
CARDS = [
    ("01-phien-cho-thang-chap", 1, E(0, 5, 5, 0),    E(0, 10, -5, 0),  {}),
    ("02-von-lieng-cua-nghe",   1, E(10, -15, 0, 0), E(-5, 5, 0, 0),   {}),
    ("03-mua-cuoi-hoang-kim",   1, E(0, -5, 5, 10),  E(5, 5, 0, -5),   {}),
    ("04-phien-cho-vang",       1, E(0, -5, 10, 0),  E(0, 10, -10, 0), {}),
    ("05-doi-at-dau",           1, E(0, -10, 0, 5),  E(0, 5, -10, -10), {}),
    ("06-toan-quoc-khang-chien",1, E(0, -10, 0, 0),  E(5, 5, 0, -10),  {}),
    ("07-lang-chay",            1, E(0, -10, -10, 0), E(-15, 10, 0, 0),
        {"grantsA": "giu_van", "floor": ("nguoi", 20)}),
    ("08-ben-kia-song-duong",   1, E(0, 0, 10, 0),   E(0, 5, 0, -5),   {}),
    ("09-tan-cu-day-nghe",      1, E(5, -5, 0, 5),   E(-10, 5, 0, -5),
        {"grantsA": "giu_bi_quyet", "floor": ("nghe", 25)}),
    ("10-viec-tot-thanh-pho",   1, E(0, 20, 0, -15), E(0, -5, 0, 0),   {}),
    ("11-lai-buon-do-co",       1, E(0, 25, 0, 0),   E(0, -5, 0, 0),
        {"revokesA": "giu_van"}),
    ("12-ve-lang",              1, E(0, -5, 5, 5),   E(0, 15, -10, -5), {"tickA": 1}),

    ("13-htx-thanh-lap",        2, E(0, 15, 5, -5),  E(5, -5, -5, 0),  {}),
    ("14-mau-cai-tien",         2, E(-10, 10, 0, 0), E(5, -5, -5, 0),  {}),
    ("15-day-con-trong-xuong",  2, E(0, -5, 0, 5),   E(0, 5, 0, -10),  {"tickA": 1}),
    ("16-dat-nuoc-lien-mot-dai",2, E(0, 5, 5, 0),    E(0, 0, 0, 5),    {}),
    ("17-don-xuat-khau",        2, E(-5, 15, 0, 0),  E(10, -5, 0, 0),  {}),
    ("18-luu-mau-co",           2, E(5, -10, -5, 0), E(0, 5, 0, 0),
        {"grantsA": "giu_mau_co", "floor": ("nghe", 25)}),
    ("19-doi-moi",              2, E(0, 10, 0, -5),  E(0, -5, 0, 0),   {}),
    ("20-con-muon-o-lai",       2, E(0, -10, 0, 5),  E(0, 10, 0, -10), {"tickA": 1}),
    ("21-lich-tran-ve",         2, E(0, -5, 5, 0),   E(5, -5, -10, 0), {}),
    ("22-htx-giai-the",         2, E(-15, 25, 0, 0), E(0, -5, 0, 0),
        {"revokesA": "giu_mau_co", "tickA": -1}),

    ("23-nhat-ve-tung-tam",     3, E(0, -15, 5, 0),  E(0, 5, 0, 0),
        {"grantsA": "phuc_hoi_van", "floor": ("sinh_ke", 20)}),
    ("24-khach-tay-dau-tien",   3, E(0, 5, 5, 0),    E(0, 0, -5, 5),   {}),
    ("25-hang-du-lich",         3, E(-10, 15, 0, 0), E(5, -5, 0, 0),   {}),
    ("26-dung-nha-trung-bay",   3, E(0, -15, 5, 0),  E(0, 5, -5, 0),   {}),
    ("27-mo-cua-don-khach",     3, E(-5, -5, 5, 5),  E(5, 5, -5, 0),
        {"grantsA": "mo_cua", "floor": ("tieng", 20)}),
    ("28-di-san-quoc-gia",      3, E(0, -5, 5, 0),   E(0, 5, 0, 0),    {}),
    ("29-doan-truong-den-xuong",3, E(0, 5, 0, 5),    E(0, 10, -5, -5), {}),
    ("30-chau-noi-nghe",        3, E(0, -10, 0, 10), E(0, 10, 0, -10),
        {"grantsA": "truyen_nhan", "floor": ("nguoi", 20)}),
    ("31-ho-so-khoi-dong",      3, E(-5, -10, 5, 0), E(0, 5, 0, 0),
        {"grantsA": "ho_so", "floor": ("tieng", 25)}),
    ("32-noi-tieng-tren-mang",  3, E(-10, 10, 10, 0), E(5, -5, -5, 0),  {}),
    ("33-han-chot-31-3",        3, E(-10, -15, 0, -5), E(0, 5, 0, 0),
        {"grantsA": "ho_so", "floor": ("tieng", 25), "lastChance": True}),
    ("34-trung-tam-nha-nuoc",   3, E(0, 0, 10, 0),   E(5, 0, -5, 0),   {}),
    ("35-tranh-len-ao-dai",     3, E(-5, 5, 10, 0),  E(5, 0, -5, 0),   {}),
    ("36-dem-truoc-new-delhi",  3, E(0, 0, 5, 0),    E(5, 0, 0, 0),    {}),
]

REQUIRE_ALL = {"giu_bi_quyet", "truyen_nhan", "ho_so"}
REQUIRE_ANY = {"giu_van", "phuc_hoi_van"}
REQUIRE_COUNTER = 2


def wins(st):
    if not REQUIRE_ALL <= st["flags"]:
        return False
    if not (REQUIRE_ANY & st["flags"]):
        return False
    if st["tick"] < REQUIRE_COUNTER:
        return False
    return all(st[k] >= GATE[k] for k in STATS)


def step(st, idx, choice, kho):
    """Apply card idx with choice; return list of successor states (crisis branching)."""
    cid, ch, ea, eb, x = CARDS[idx]
    eff = ea if choice == "A" else eb
    s = dict(st)
    s["flags"] = set(st["flags"])
    s["used"] = set(st["used"])
    s["line"] = st["line"] + [choice]
    if choice == "A":
        if "grantsA" in x:
            fl = x.get("floor")
            if fl is None or s[fl[0]] >= fl[1]:
                # last-chance card only grants if flag still absent
                if not (x.get("lastChance") and "ho_so" in s["flags"]):
                    s["flags"].add(x["grantsA"])
        if "revokesA" in x:
            s["flags"].discard(x["revokesA"])
        s["tick"] = st["tick"] + x.get("tickA", 0)
    else:
        s["tick"] = st["tick"]
    for k, v in eff.items():
        s[k] += v
    outs, dead = [], False
    for k in STATS:
        if s[k] <= 0 or s[k] >= 100:
            dead = True
    if kho:
        return [] if dead else [s]
    # crisis offers (Thường): entering a band with that side unused
    branches = [s]
    for k in STATS:
        for side, cond in (("lo", s[k] <= BAND_LO), ("hi", s[k] >= BAND_HI)):
            if cond and (k, side) not in s["used"]:
                nb = []
                for b in branches:
                    acc = dict(b); acc["flags"] = set(b["flags"]); acc["used"] = set(b["used"])
                    acc["used"].add((k, side))
                    for kk, vv in CRISES[(k, side)].items():
                        acc[kk] += vv
                    acc["line"] = b["line"][:-1] + [b["line"][-1] + "+cx:%s-%s" % (k, side)]
                    ref = dict(b); ref["flags"] = set(b["flags"]); ref["used"] = set(b["used"])
                    ref["used"].add((k, side))
                    nb += [acc, ref]
                branches = nb
    return [b for b in branches
            if all(0 < b[k] < 100 for k in STATS)]


def search(kho, beam=6000, forced=None):
    """forced: dict {card_index: 'A'|'B'} — the canonical skeleton; others free."""
    st0 = dict(START)
    st0.update({"flags": set(), "used": set(), "tick": 0, "line": []})
    layer = [st0]
    for i in range(len(CARDS)):
        nxt = []
        for st in layer:
            choices = (forced[i],) if forced and i in forced else ("A", "B")
            for c in choices:
                nxt += step(st, i, c, kho)
        # dedup+prune: keep diverse best by (flags,tick,stat-signature)
        seen, keep = {}, []
        nxt.sort(key=lambda s: -(min(s[k] - GATE[k] for k in STATS)
                                 + 40 * len(s["flags"] & (REQUIRE_ALL | REQUIRE_ANY))
                                 + 20 * min(s["tick"], REQUIRE_COUNTER)))
        for s in nxt:
            key = (frozenset(s["flags"]), s["tick"],
                   tuple(s[k] // 5 for k in STATS), frozenset(s["used"]))
            if key not in seen:
                seen[key] = 1
                keep.append(s)
            if len(keep) >= beam:
                break
        layer = keep
        if not layer:
            return None, i
    winners = [s for s in layer if wins(s)]
    if not winners:
        return None, len(CARDS)
    winners.sort(key=lambda s: -min(s[k] - GATE[k] for k in STATS))
    return winners, len(CARDS)


def show(tag, winners, depth):
    if not winners:
        print("%s: NO WINNING LINE (search died at card %d)" % (tag, depth + 1))
        return
    best = winners[0]
    ncx = sum(1 for c in best["line"] if "+cx" in c)
    print("%s: %d winning end-states; best line (crises fired: %d):" % (tag, len(winners), ncx))
    print("   " + " ".join("%d%s" % (i + 1, c) for i, c in enumerate(best["line"])))
    print("   end  nghe %d · sinh_ke %d · tieng %d · nguoi %d · ticks %d · flags %s"
          % (best["nghe"], best["sinh_ke"], best["tieng"], best["nguoi"],
             best["tick"], sorted(best["flags"])))
    zero_cx = [s for s in winners if not any("+cx" in c for c in s["line"])]
    print("   winning end-states with ZERO crises: %d" % len(zero_cx))


def run_line(choices, kho):
    """Replay one fixed line of choices; accept a crisis offer only when it helps."""
    st = dict(START)
    st.update({"flags": set(), "used": set(), "tick": 0, "line": []})
    log = []
    for i, c in enumerate(choices):
        outs = step(st, i, c, kho)
        if not outs:
            return None, log + ["DEAD at card %d%s (%s)" % (i + 1, c, CARDS[i][0])]
        outs.sort(key=lambda s2: -min(s2[k] - GATE[k] for k in STATS))
        st = outs[0]
        log.append("%2d%s  %-22s %3d %3d %3d %3d  t%d%s" % (
            i + 1, c, CARDS[i][0], st["nghe"], st["sinh_ke"], st["tieng"], st["nguoi"],
            st["tick"], "  " + "+".join(sorted(x["grantsA"] for x in [CARDS[i][4]] if "grantsA" in x)) if c == "A" and "grantsA" in CARDS[i][4] else ""))
    return st, log


CANONICAL_THUONG = "A A B B A B A A A B B A A B A A A A A A B B A A A B A B A A A A B B A B".split()
CANONICAL_KHO = "B B A B B B A A A B B A A B A A A A A A A B A A A B A B B A A B B A B A".split()

# Canonical skeleton: the required carriers and both traps pinned. Card 23 (phuc_hoi_van) is
# deliberately left free — canonical_search() filters for the optional pair afterwards, so the
# search can find lines that reach it by either road.
FORCED = {6: "A", 8: "A", 9: "B", 10: "B", 11: "A", 14: "A", 17: "A", 19: "A",
          21: "B", 26: "A", 29: "A", 30: "A", 32: "B"}

def canonical_search(kho):
    w, d = search(kho=kho, forced=FORCED)
    if not w:
        return None
    full = [s2 for s2 in w if {"giu_mau_co", "mo_cua"} <= s2["flags"]]
    return (full or w)[0]


def audit():
    """--audit: the stat economy, printed from the same table the search runs on.

    Two laws, machine-checked here because the spine lives in this mirror until
    cards/*.json are written (the linter enforces the same laws on data files):

    1. FAUCETS AND DRAINS — every stat must be both earnable and losable in every
       chapter. A stat that only drains in a chapter is a scripted death, not a
       resource; one that only rises is not a resource at all.
    2. THE TRADE RULE — a choice may beat its pair on every stat only by paying
       in flags (a grant skipped, a revoke taken, a tick lost). Stat-dominance
       with no flag price is a dead option.
    """
    stats = ("nghe", "sinh_ke", "tieng", "nguoi")
    flow = {}
    for idx, (cid, ch, A, B, extra) in enumerate(CARDS, 1):
        for st in stats:
            f = flow.setdefault(ch, {}).setdefault(st, [0, 0, 0, 0])  # +sum, -sum, +cards, -cards
            p = sum(v for v in (A.get(st, 0), B.get(st, 0)) if v > 0)
            n = sum(v for v in (A.get(st, 0), B.get(st, 0)) if v < 0)
            f[0] += p; f[1] += n
            if p: f[2] += 1
            if n: f[3] += 1
    bad = 0
    print("SPINE ECONOMY (per chapter: +available / -available across both choices)")
    for ch in sorted(flow):
        print("  Chapter %d (cards %s)" % (ch, {1: "1-12", 2: "13-22", 3: "23-36"}[ch]))
        for st in stats:
            f = flow[ch][st]
            mono = ""
            if f[0] == 0 or f[1] == 0:
                mono = "   <-- MONOTONE: no %s in this chapter" % ("faucet" if f[0] == 0 else "drain")
                bad += 1
            print("    %-8s +%-4d (%2d cards)   %-5d (%2d cards)%s" % (st, f[0], f[2], f[1], f[3], mono))

    print("TRADE RULE (stat-dominant pairs must pay in flags)")
    for idx, (cid, ch, A, B, extra) in enumerate(CARDS, 1):
        a = [A.get(s, 0) for s in stats]; b = [B.get(s, 0) for s in stats]
        if a == b:
            continue
        a_dom = all(x >= y for x, y in zip(a, b))
        b_dom = all(x <= y for x, y in zip(a, b))
        if a_dom or b_dom:
            paid = any(k in extra for k in ("grantsA", "grantsB", "revokesA", "revokesB",
                                            "tickA", "tickB", "lastChance"))
            verdict = "paid in flags — legal" if paid else "UNPAID — dead option"
            if not paid:
                bad += 1
            print("  card %2d %-24s %s dominates on stats: %s (%s)"
                  % (idx, cid, "A" if a_dom else "B", extra or "no extras", verdict))
    print("FLOOR TIMING (can each statFloor actually bind?)")
    # Worst-reachable value of the floored stat at each floored carrier:
    # spine-only DP minimum (every choice adversarial), plus the harshest legal
    # weave allowance scheduled before that card (slots in earlier-or-same
    # chapter, most negative single effect on that stat in each slot's pool).
    # Ambient is all-positive and crisis rescues are opt-in — both excluded, so
    # this is the true pessimum of the forced game.
    slots_per = {1: 2, 2: 1, 3: 1}
    import json as _json, os as _os
    pool_min = {}
    lvl_path = _os.path.join(_os.path.dirname(__file__), "..", "content", "dongho", "game_contents.json")
    try:
        _lvl = _json.load(open(lvl_path, encoding="utf-8"))
        # the slot counts are the level's own dial, never a copy kept here
        _slots = (_lvl.get("weavePolicy") or {}).get("slotsPerChapter") or {}
        slots_per = {c: _slots.get("C%d" % c, slots_per[c]) for c in (1, 2, 3)}
        for wv in _lvl.get("weave", []):
            c = int(wv["chapter"][1])
            for chx in wv.get("choices", []):
                for st, v in (chx.get("effects") or {}).items():
                    pool_min[(c, st)] = min(pool_min.get((c, st), 0), v)
    except OSError:
        print("  (game_contents.json unreadable — weave allowance assumed 0)")
    lo = dict(START)
    for idx, (cid, ch, A, B, extra) in enumerate(CARDS, 1):
        fl = extra.get("floor")
        if fl:
            st, need = fl
            allowance = sum(slots_per[c] * pool_min.get((c, st), 0)
                            for c in range(1, ch + 1))
            worst = lo[st] + allowance
            live = worst < need
            print("  card %2d %-24s floor %s>=%-3d worst-reachable %d%+d=%d  -> %s"
                  % (idx, cid, st, need, lo[st], allowance, worst,
                     "LIVE" if live else "TRAINING (cannot bind)"))
        for st in lo:
            lo[st] += min(A.get(st, 0), B.get(st, 0))
            lo[st] = max(0, min(100, lo[st]))
    print("AUDIT: %s" % ("CLEAN" if not bad else "%d violation(s)" % bad))
    return bad


if __name__ == "__main__":
    import sys as _sys
    if "--audit" in _sys.argv:
        raise SystemExit(1 if audit() else 0)

    for kho in (False, True):
        best = canonical_search(kho)
        tag = "KHO" if kho else "THUONG"
        if best is None:
            print("SEARCH %s: NO LINE EXISTS with all carriers+no traps" % tag)
        else:
            ncx = sum(1 for c in best["line"] if "+cx" in c)
            print("SEARCH %s (crises %d): %s" % (tag, ncx,
                  " ".join("%d%s" % (i + 1, c) for i, c in enumerate(best["line"]))))
            print("   end %d/%d/%d/%d t%d flags %s" % (best["nghe"], best["sinh_ke"],
                  best["tieng"], best["nguoi"], best["tick"], sorted(best["flags"])))
    for name, line, kho in (("THUONG", CANONICAL_THUONG, False), ("KHO", CANONICAL_KHO, True)):
        st, log = run_line(line, kho=kho)
        ok = bool(st) and wins(st)
        print("REPLAY canonical %s: %s" % (name, "WINS" if ok else "FAILS — " + (log[-1] if log else "?")))
        if st:
            print("   end %d/%d/%d/%d t%d" % (st["nghe"], st["sinh_ke"], st["tieng"], st["nguoi"], st["tick"]))

    w, d = search(kho=False)
    show("THUONG", w, d)
    w2, d2 = search(kho=True)
    show("KHO   ", w2, d2)
