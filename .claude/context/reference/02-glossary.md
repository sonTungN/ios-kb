---
id: REF-02
title: Glossary — project-specific terms
domain: reference
authority: reference
scope: Definitions for every term of art used in the brief and this KB, so a term met in one file resolves without loading the file that introduced it.
keys: [glossary, term, definition, meaning, jargon, vocabulary]
related: [BRIEF-02]
source: Compiled from the brief, 13 Aug 2026
---

# Glossary

| Term | Meaning here |
| --- | --- |
| **Living heritage** | Cultural practices that stay meaningful by being *experienced, understood, shared, adapted, and passed on* — crafts, games, festivals, foodways, performances, everyday practices — as opposed to static monuments or archives (`BRIEF-02`). |
| **"Culture in Play"** | The theme's demand that cultural knowledge shape the *game system* (rules, decisions, constraints), not just its artwork or trivia (`BRIEF-02`). |
| **Cultural Element → Gameplay Mechanic → Player Learning** | The required explanatory chain: which heritage element was chosen, what mechanic it generates, what the player learns by playing. Appears in the report §1 and the README (`BRIEF-06`, `BRIEF-07`). |
| **Hackathon** | The framing of the project: a simulated 4-week team sprint from concept to shipped game (`BRIEF-02`). |
| **2D game** | The required form — board/card/dice/strategy/resource/puzzle/route/simulation or similar; explicitly *not* a SpriteKit/GameKit 3D-or-engine project (`BRIEF-02`). |
| **MVVM** | Model-View-ViewModel — the mandatory architecture: Models, Views, ViewModels, persistence/data services, supporting components, clearly separated (`BRIEF-03`). |
| **CRUD** | Create, Read, Update, Delete — required for relevant game data such as profiles, progress, leaderboard scores (`BRIEF-03`). |
| **Cloud sync** | User-data synchronization via a cloud service (like Firebase) so the experience is consistent across devices (`BRIEF-03`). |
| **`GoogleService-Info.plist`** | Firebase's per-app config file — must be committed so markers build without credentials; stands in for "the equivalent configuration file" of any chosen cloud service (`BRIEF-01`). |
| **Killer feature** | "A distinctive functionality, gameplay mechanic, educational approach, cultural integration, or user experience that provides a strong reason for a user to choose your application over comparable alternatives" — report §3 (`BRIEF-06`). |
| **Industry requirement** | One of the practices presented at the **Week 7 Guest Lecture**; each team implements **two** and evidences them in report §5 (`BRIEF-05`, `BRIEF-06`). |
| **Project Manager (PM)** | Mandatory role: plans/controls tasks, chairs meetings, builds team spirit, finalises the responsibilities table (`BRIEF-07`). |
| **Technical Lead (TL)** | Mandatory role: major technical decisions; gatekeeper of the default branch (`BRIEF-07`). |
| **Project Responsibilities table** | Report §11: each member's actual responsibilities + workload %, totalling 100%, naming PM and TL (`BRIEF-06`). |
| **Unlisted (YouTube)** | Video visibility level required for the demo video: reachable by link, not publicly searchable (`BRIEF-06`). |
| **Demo account** | A username + password in the README that lets the marker log in without registering (`BRIEF-07`). |
| **Save and Resume ("fully closing")** | The optional feature's bar: progress survives the app being *removed from memory* (hold & swipe up in the app switcher) — not merely backgrounded (`BRIEF-05` §6). |
| **Week 11** | The submission week — due Friday 11 Sep 2026, 17:00 ICT (`BUILD-02`). |
| **Marking environment** | Xcode 26.4.1, iOS 26.4.1 target, iPhone 17 Pro simulator, lab-iMac-class Mac (`BRIEF-01`). |
| **Address (KB)** | A stable ID like `BRIEF-04` used to route and cite KB files (`OVERVIEW.md`). |

---

## The game's own vocabulary

Defined by `.claude/data-design/`, which is the authority on all of it.

| Term | Meaning here |
| --- | --- |
| **_Reigns_** | The commercial card game whose format this project rebuilds: a single card at a time, two choices, left or right swipe, stats moving with each decision. The format is borrowed; the content and the win rule are the team's own (`DEC-01` D1a). |
| **Spine card** | A dated card fixed to a real, sourced event. Never shuffled, never skipped, always in chronological order. 36 of them make the run. |
| **Weave card** | An undated card of ordinary craft life, drawn at random — 4 per run from a pool of 17. Three laws: `year: null`, never carries a required flag, never tagged `documented`. It is where run-to-run variety comes from. |
| **Carrier** | A spine card that grants a **preparation flag** — the mini-boss of the run. Each one has a floor, a mandatory cost, and an advisor before it. |
| **Preparation flag** | A boolean the run either holds or does not by the end. Seven exist; five are required in some combination. Flags — not stats — decide victory. |
| **`statFloor`** | The minimum a stat must reach for a carrier's attempt to succeed. It is *the means to act*, never a threshold to farm: below it the cost is still paid and the flag is not granted. |
| **Tick / `truyen_thua`** | The transmission counter, 0–3. Three cards can raise it, one trap can take one back, and the trial requires ≥ 2. It is the only non-boolean the win rule reads. |
| **Trap** | A card that looks like the best deal on the table and revokes a flag or a tick. Two exist: the dealer buying the rescued woodblocks, and the 1990 switch to vàng mã. |
| **Crisis** | A rescue card that fires when a stat enters a danger band — eight of them, one per stat per side, once each per run. Every rescue is priced from a *different* stat. On Khó there are no bands at all. |
| **Ambient** | A small, positive, non-decision beat. Capped per run so the free points can never outweigh what the preparations cost. |
| **Interstitial** | A non-decision screen between cards. Four types: **advisor** (what the next card will cost), **omen** (what is coming), **echo** (a callback to an earlier choice), **chapter** (the era turn). |
| **Chapter** | One of the run's three eras — *Giữ lửa* (cards 1–12) · *Giữ nếp* (13–22) · *Hồi sinh* (23–36) — played as a sequential **level**: unlocks when the previous chapter ends, opens on its era screen, closes on a summary/lesson screen. Stats, flags, ticks and spent crises carry across unchanged; restarting an earlier chapter locks the later ones. |
| **Final Trial** | The run's ending: the UNESCO inscription of 9 Dec 2025. Not a card — it asks nothing and judges. It reads flags and the counter for victory, and stats only as a low survival floor. |
| **Ledger / Sổ gia truyền** | The in-game screen listing preparations held, open and missed. Its **scope** is the main thing difficulty changes: Dễ = one big ledger anytime · Thường/Khó = three per-chapter ledgers · Cực khó = none. |
| **Codex / Bộ sưu tập tranh** | The collectible gallery of real paintings with their documented meanings. Also the CRUD + search/filter surface and `mg_match`'s content source. |
| **`historicity`** | Per-card honesty tag — `documented` / `simplified` / `invented`. The three buckets report §2 must declare, so tagging as you write pre-writes that section. |
| **Solvency invariant** | The guarantee that no legal weave draw can change *whether* a run is winnable — only how it feels and what it costs. Machine-checked by the linter. |
| **Two axes of difficulty** | *Across chapters* = progression, from the shape of the problem. *Inside the run* = the Dễ/Thường/Khó control, which changes **only information and slack** — never a number, a cost, a flag or the win rule. |
