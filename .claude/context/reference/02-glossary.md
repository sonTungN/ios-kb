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
