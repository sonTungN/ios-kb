---
id: BRIEF-04
title: The five required views — the marker's checklist
domain: brief
authority: brief
scope: Exact feature checklist for the five mandatory views — Menu (Welcome), Game, Leaderboard, How To Play, and Game Settings.
keys: [views, Menu, Welcome, Game View, Leaderboard, How To Play, Settings, Start New Game, Continue, score, Game Over, animations, achievement badges, interactive graphs, charts, tutorial, difficulty, Easy, Medium, Hard, game variations, theme switcher, light, dark, multi-language, language, picker]
related: [BRIEF-03, BRIEF-05, BRIEF-09]
source: _source/canvas-extract-raw.md — Technical Requirements §2 "Game Structure and Views"
---

# Technical requirements §2 — game structure and views

> "The game must consist of **at least** the following five core views."

## 1 · Menu View (Welcome View)

- The initial screen with navigation to other views.
- Must include options to **Start New Game**, **Continue** (for saved games), **Leaderboard**, **How To Play**, and **Settings**.
- Should display **login/logout status** and provide access to the **user's profile**.

## 2 · Game View

- The primary screen where the **2D game** is played.
- Must display the **current score, game status, and other relevant information**.
- Incorporate **animations** for player actions and game events — **at minimum three distinct animations**, for example: a move or placement action, a scoring or feedback event, and a view transition.
- Display a **"Game Over" screen** upon completion.

## 3 · Leaderboard View

- Display a **list of high scores with corresponding usernames**.
- Feature **achievement badges** (name **and** image) that users earn for reaching **educational or gameplay milestones**.
- Include **interactive graphs** (e.g., bar charts, line charts) to visualize player statistics like **win percentage, score trends, or games played**.

## 4 · How To Play View

- Provide clear, concise instructions on the game's **rules and objectives**.
- Implement an **interactive tutorial** with visual aids, animations, and prompts to guide new players through the mechanics and strategies.

## 5 · Game Settings View

- Allow users to adjust game **difficulty** (e.g., Easy, Medium, Hard) **with descriptions for each level**.
- Could offer different **game variations or rule sets** to enhance replayability for each difficulty.
- Include a **theme switcher** to toggle between **custom light and dark themes** for the app.
- Implement **multi-language support** (at least **English and one other language**, e.g., Vietnamese) via a **picker or dropdown menu**.

---

Cross-cutting obligations that touch every view: background music on Menu / How To Play / Leaderboard, sound effects, splash screen, device responsiveness and system light/dark support (`BRIEF-05`); login/profile plumbing (`BRIEF-03`).
