---
id: BRIEF-01
title: Logistics, deliverables, ZIP structure & marking environment
domain: brief
authority: brief
scope: Weight, team size, due date, late policy, learning objectives, the mandatory source-file header, the marking environment, every deliverable file, and the exact ZIP structure and filenames.
keys: [deadline, due, week 11, late, penalty, 40%, team of 5, zip, submission, filename, Document.pdf, GitHub.txt, Youtube.txt, header, Xcode version, iOS version, marking environment, lab, iMac, GoogleService-Info.plist, learning objectives]
related: [BRIEF-06, BRIEF-07, BRIEF-09, BUILD-02]
source: _source/canvas-extract-raw.md — header, Learning Objectives, Deliverables, Project Deliverables, Submission Instructions; Canvas due-date metadata (epoch 1789120800)
---

# Logistics, deliverables & submission compliance

Submission compliance is **graded** (part of the 4-point *Well-formatted, Organized Code & GitHub Repository* criterion — see `BRIEF-09`). Non-compliance with the required structure or filenames "will be treated as submission non-compliance and will be assessed under the Code Quality, GitHub Repository and Submission Organisation criterion."

## Course & assessment

| Field | Value |
| --- | --- |
| Course | COSC3062 \| COSC3063 — iPhone Software Engineering |
| Semester | 2026B |
| Assessment | **Assignment 2 — Group Project** |
| Weight | **40%** of the course |
| Type | **Team of 5 students** |
| Duration | ~4 weeks |
| Available from | **Mon 10 Aug 2026, 10:00** (Canvas: "Available after Aug 10 at 10:00") |
| **Due** | **"5PM Friday of week 11"** — Canvas resolves this to **Friday 11 September 2026, 17:00** (sidebar: "Due Sep 11 by 17:00"; due-date metadata epoch `1789120800` = 2026-09-11 10:00 UTC = 17:00 Vietnam time). See `BUILD-02` for the derivation. |
| Points | 40 (Canvas sidebar: "Points 40"; rubric totals 40 — `BRIEF-09`) |
| Feedback mode | **Not available** — "because this is the second last assessment" |
| Submission | A single `.zip` uploaded to Canvas (only file type accepted). Multiple submissions allowed; **only the latest is graded**. |

## Late policy

- **10% per day**, up to 5 days late. After 5 days, the penalty is **100%**.

## Learning objectives assessed

- Describe the limitations and challenges of working in a mobile environment as well as the commercial and research opportunities presented by these technologies.
- Apply the different types of application models/frameworks used to develop mobile software applications.
- Learn about the components and structure of the iPhone application development framework and know how and when to apply the different components to develop a working system.
- Describe and apply software patterns for the development of the application models described above.
- Apply critical analysis, problem solving, and team facilitation skills to mobile app software engineering scenarios.

**Ready for Life and Work:** analyze and design a solution in Swift for a given problem · implement the solution using Xcode · test and debug using Xcode · **manage source code using GitHub** · **work efficiently in team**.

## Mandatory source-file header

Required at the top of **every** source code file:

```
/*
  RMIT University Vietnam
  Course: COSC3062|COSC3063 iPhone Software Engineering
  Semester: 2026B
  Assessment: Assignment 2
  Author: Your name (e.g. Nguyen Van Minh)
  ID: Your student id (e.g. 1234567)
  Created date: dd/mm/yyyy (e.g. 31/07/2026)
  Last modified: dd/mm/yyyy (e.g. 05/08/2026)
  Acknowledgement: Acknowledge the resources that you use here.
*/
```

## Marking environment

- **"Your app will be tested in the simulator of Xcode 26.4.1 and the target of iOS 26.4.1 on the iPhone 17 Pro Simulator in a Mac computer similar to that."**
- **Test your app carefully in one of the iMac computers in the lab** to resolve any unforeseen issues before submitting. If you develop on an older Xcode version on a personal MacBook, compile and run on a lab iMac before submitting.
- The project must **compile and run without requiring the marker to** repair file references, download missing resources, obtain API keys, or change the project configuration.
- **Commit `GoogleService-Info.plist`** (or the equivalent configuration file) to the private repository and include it in the submission, so the marker can build and run without obtaining credentials.
- Note the UI must also work on more devices than the marking simulator — iPhone 17 / 17 Pro / 17 Pro Max / 11-inch iPad Air (`BRIEF-05`).

## Deliverables — the four required items

| # | Item | Rule |
| --- | --- | --- |
| 1 | Complete Xcode project and source code | Complete Xcode project, Swift source files, asset catalogues, bundled JSON data, images, and all other resources required to compile and run. **Must be identical to the final commit of the assigned private GitHub repository.** |
| 2 | `Document.pdf` | The project report (`BRIEF-06`). "The filename must be exactly Document.pdf." |
| 3 | `GitHub.txt` | **Only** the complete URL of the assigned private GitHub repository — nothing else. Example: `https://github.com/rmit-vietnam-computing-technologies/2026b-COSC3062-a2-sg-my-group-name` |
| 4 | `Youtube.txt` | **Only** the URL of the YouTube demo presentation video — nothing else. Example: `https://youtu.be/AbCdEfGhIjk`. *(Derived, not stated: the video itself lives on YouTube as unlisted — `BRIEF-06` — only its URL is submitted.)* |

## Exact ZIP structure

ZIP name: `iOS_Assignment2_NameOfYourApp_YourGroupName.zip` — replace `NameOfYourApp` and `YourGroupName` with the actual app and group names. Example: `iOS_Assignment2_LangNghe_TeamPhoenix.zip`.

```
iOS_Assignment2_NameOfYourApp_YourGroupName.zip
└── iOS_Assignment2_NameOfYourApp_YourGroupName/
    ├── SourceCode/          ← inside is exactly the copy of the project in the private GitHub repo
    │   └── NameOfYourApp/
    │       └── (the whole Xcode project)
    ├── Document.pdf
    ├── GitHub.txt
    └── Youtube.txt
```

The following names must be used **exactly**: `SourceCode` · `Document.pdf` · `GitHub.txt` · `Youtube.txt`. Inside `SourceCode/NameOfYourApp/`, preserve a complete and working Xcode project.

Submit the ZIP to Canvas before the due date and time.
