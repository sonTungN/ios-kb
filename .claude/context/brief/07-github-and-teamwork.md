---
id: BRIEF-07
title: GitHub repository rules, development history, README & team roles
domain: brief
authority: brief
scope: The assigned org repo and invitation process, the ban on personal/public repos, what markers examine in the commit history, the README contract (incl. demo account), the pre-submission repo checklist, and the Project Manager / Technical Lead roles.
keys: [GitHub, repository, private, organization, rmit-vietnam-computing-technologies, invitation, seven days, branches, commits, history, incremental, commit messages, merge, README, demo account, checklist, plagiarism, leak, Project Manager, Technical Lead, gatekeeper, roles, contribution, teamwork]
related: [BRIEF-01, BRIEF-06, BRIEF-09, BUILD-01]
source: _source/canvas-extract-raw.md — "Assigned GitHub Repository" → "Teamwork"
---

# GitHub & teamwork

## Assigned GitHub repository

- Each team is provided with an **individual private GitHub repository** in the organization **`rmit-vietnam-computing-technologies`** (`https://github.com/rmit-vietnam-computing-technologies/`).
- **The teaching team creates the repository** and adds each member as a collaborator — do not create it yourself.
- Repo name format: **`<year>-<course>-<assignment>-<campus>-<your-group-name>`** — e.g. `2026b-COSC3062-a2-sg-your-group-name`.

### Accepting the invitation

1. GitHub emails a collaborator invitation to the address associated with each member's GitHub account.
2. Open the invitation email and accept.
3. **Accept within seven days** — GitHub invitations expire after this period.
4. Confirm access to the private repository in the org.
5. Clone/set up the assigned repository and **use it for all development work**.

Check spam/junk folders. If the invitation expired, the GitHub username is incorrect, or access fails — **contact the teaching team as soon as possible**.

## Repository requirements

- All project code must be committed and pushed to the assigned private repository.
- **Do not create or use a personal public repository.** Do not upload, duplicate, mirror, or share the project code in another repository or anywhere on the internet.
- **Work stored outside the assigned private repository may not be accepted for marking** — "your project code will not be marked!"
- Rationale given: code in personal repositories "could expose it to copying by other teams, which would lead to serious issues of plagiarism. These problems have happened in the past."
- The source code in the Canvas ZIP **must be identical to the final commit** of the assigned repository.
- `GitHub.txt` contains the complete repo URL (`BRIEF-01`).

## Development-history requirements — the history IS assessment evidence

Markers will examine:

- the **number of branches**; the **purpose** of each branch; **branch names**;
- the **number of commits**; **commit dates and timestamps**;
- whether commits are **reasonably distributed across the ~four-week development period**;
- whether development appears **incremental** or was rushed into a short period immediately before submission;
- the **clarity and meaning of commit messages**;
- whether branches were **merged logically**;
- whether the repository shows an **understandable progression** from initial setup to the final application.

Calibration from the brief:

- Commit and branch counts are considered **in relation to the scope and quality of the work**. Large numbers of **empty, trivial, duplicated, or artificially divided commits earn no additional credit**.
- Branches should have a **clear purpose** and represent **meaningful units of work** (features, fixes, refactoring, development stages) — not a branch per small change.
- Guide: **roughly one branch per feature or development stage, and regular commits from every team member across the full four weeks**, rather than a small number of large uploads.

## README requirement

The repo must contain a comprehensive `README.md` including:

- the project name;
- a concise project description;
- **the cultural heritage the game is based on + a short summary of the Cultural Element → Gameplay Mechanic → Player Learning relationship**;
- setup and build instructions;
- instructions for running and using the app, **including a demo account (username and password) that the marker can log in with**;
- the required Xcode and iOS versions;
- any known issues or limitations;
- any additional information required by the marker.

## Pre-submission repo checklist

Before submitting, confirm that:

- [ ] all relevant branches have been pushed;
- [ ] the intended final work has been merged into the **default branch**;
- [ ] the final project **builds from a fresh clone**;
- [ ] all required assets and JSON resources are tracked;
- [ ] no required source file exists only on a local computer;
- [ ] the source code in the Canvas ZIP **matches the final repository commit**.

## Teamwork — mandatory roles

- Each team **must nominate a Project Manager and a Technical Lead**, and record both roles in the report's Project Responsibilities table (`BRIEF-06` §11).
- **Project Manager:** responsible for planning and controlling tasks, chairing meetings, and building good team spirit.
- **Technical Lead:** responsible for evaluating and making major technical decisions; acts as **gatekeeper of the team's GitHub repository, determining what is accepted into the default branch**. May also coach other members on design, coding, debugging, and testing.
- **Holding a role does not reduce a member's expected development contribution.**
- Contribution is assessed **overall**: initiative (helping manage the project, contributing strong ideas), amount of work, quality of work, and support given to other members.
