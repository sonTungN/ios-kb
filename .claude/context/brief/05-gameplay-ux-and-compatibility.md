---
id: BRIEF-05
title: Gameplay/UX features, compatibility, Week 7 industry requirements, optional advanced features & aesthetics
domain: brief
authority: brief
scope: Progression/levels, music and sound effects, animated splash screen, contextual search/filter, device and light/dark compatibility, the two mandatory Week 7 guest-lecture industry requirements, the optional advanced features, and the aesthetic/user-centred design criteria.
keys: [progression, levels, difficulty, sound, music, background music, sound effects, splash screen, search, filter, iPhone 17, iPhone 17 Pro, Pro Max, iPad Air, responsive, dark mode, light mode, system theme, Week 7, guest lecture, industry requirements, AI opponent, notifications, accessibility, VoiceOver, dynamic type, save and resume, aesthetic, HIG, Human Interface Guidelines, visual appeal, consistency, user-centered]
related: [BRIEF-04, BRIEF-06, BRIEF-09, DEC-01, BUILD-01]
source: _source/canvas-extract-raw.md — Technical Requirements §3–§6 + "Aesthetic and User-Centric Design"
---

# Technical requirements §3–§6 + aesthetics

## §3 · Gameplay and user experience features

- **Game Progression and Levels:** structure the game with **levels or stages of increasing difficulty** to keep gameplay engaging and **progressively introduce new educational elements**.
- **Sound and UI:**
  - **Background Music:** appropriate background music for the **Menu, How To Play, and Leaderboard** views.
  - **Sound Effects:** for key user interactions and game events (e.g., taking an action, winning/losing, game result).
- **Animated Splash Screen:** a professional, **animated** splash screen that appears when the app launches.
- **Search and Filter (Contextual):** implement search or filter functionality **where it adds value** — e.g., searching for a specific rule in How To Play, or filtering the leaderboard by achievements.

## §4 · Device and system compatibility

- **Device Support:** the UI must be **responsive and function correctly on iPhone 17, iPhone 17 Pro, iPhone 17 Pro Max, and 11-inch iPad Air**.
- **System Theme Support:** the app must look appealing and be **fully functional in both the system's light and dark modes, without UI glitches**. (Distinct from the in-app custom theme switcher of `BRIEF-04` §5.)

## §5 · Industry requirements from the Week 7 Guest Lecture — MANDATORY

- Each team **must implement two industry requirements** introduced and discussed during the **Week 7 Guest Lecture**.
- Purpose: exposure to current industry expectations, professional development practices, and considerations not fully covered in weekly course content.
- **"Students are strongly expected to sign up for and attend the Week 7 Guest Lecture posed in the Canvas annoucement [sic]."**
- The team should use the lecture to **identify suitable requirements that can be meaningfully incorporated** into the project.
- If the implementation **differs from the best-practice approach presented**, the team should **clearly explain and justify** the reason. (The report has a dedicated section on this — `BRIEF-06` §5.)

⏰ **Timing note (derived, `BUILD-02`):** week 7 is **10–14 Aug 2026** — the guest lecture and its sign-up are immediate-action items (`BUILD-01`).

## §6 · Optional advanced features

Graded under their own 6-point rubric criterion (`BRIEF-09`):

- **AI Game Opponent** *(not applicable to all game types)*: for games involving an opponent, a **simple rule-based AI using conditional logic** for a more challenging single-player experience.
- **Local Notifications:** in-app or local notifications to remind users of saved games, new challenges, or to share interesting facts related to the chosen cultural heritage.
- **Accessibility:** **VoiceOver support, dynamic type, and sufficient color contrast** to make the app usable for people with disabilities.
- **Save and Resume:** allow players to save progress in an ongoing game and resume later, **even after fully closing the app**.
  - "Exit" does **not** mean pressing home or swiping to the app switcher (app still in memory) — it means **hold and swipe up to totally remove the app from memory**. Reference video: `https://www.youtube.com/watch?v=abjFdj7yexI` (`REF-01`).

## Aesthetic and user-centric design

Evaluated on visual appeal and usability against professional standards like **Apple's Human Interface Guidelines** (its own 5-point rubric criterion — `BRIEF-09`):

- **Visual Appeal:** a unique, polished, and visually engaging design, with well-chosen color schemes, fonts, and layouts **for both light and dark themes**.
- **Intuitive User Interface:** intuitive and easy to navigate, **even for first-time users**.
- **Consistency:** a consistent design language (fonts, colors, imagery, component styles) throughout the app.
- **User-Centered Design:** the design philosophy must prioritize the user's needs, creating a smooth and frictionless journey.
