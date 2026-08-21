---
id: BRIEF-03
title: Technical requirements — MVVM architecture, user management, persistence & sync
domain: brief
authority: brief
scope: The mandatory MVVM structure, registration/login/logout and profiles, full CRUD, the allowed persistence options (Core Data/SwiftData, Firebase, UserDefaults) and the cloud-synchronization requirement.
keys: [MVVM, architecture, Model, View, ViewModel, persistence, data services, registration, sign-up, login, log-in, logout, log-out, profile, avatar, bio, CRUD, Core Data, SwiftData, Firebase, UserDefaults, cloud, synchronization, sync, multiple devices]
related: [BRIEF-04, BRIEF-06, DEC-01]
source: _source/canvas-extract-raw.md — Technical Requirements §1 "Application Architecture & Core Functionality"
---

# Technical requirements §1 — architecture & core functionality

## Architecture — MVVM is mandatory

- The app **must be built using the Model-View-ViewModel (MVVM) design pattern**.
- The project structure should clearly demonstrate appropriate separation between:
  - **Models**
  - **Views**
  - **ViewModels**
  - **Persistence and data services**
  - **Other supporting components**

(The report requires an Application Flow Diagram "designed with the MVVM architecture in mind" — `BRIEF-06` §6.)

## User management

- Implement **registration (sign-up)**, **log-in**, and **log-out** features.
- Allow users to create and customize their **profiles** with an **avatar, bio, and other relevant information**.

(The repository README must include a **demo account** — username and password — the marker can log in with; `BRIEF-07`.)

## Data persistence & synchronisation

- Implement full **CRUD (Create, Read, Update, Delete)** operations for relevant game data (e.g., **user profiles, game progress, leaderboard scores**).
- **Utilize one or more** of the following for data persistence, **justifying the choice in the report** (`BRIEF-06` §4): **Core Data (or SwiftData), Firebase, or UserDefaults**.
- Implement **user data synchronization** using a cloud service like **Firebase** to ensure a consistent experience **across multiple devices**.

## Marker-buildability consequence

Because the marker must build and run with zero configuration (`BRIEF-01`):

- **Commit `GoogleService-Info.plist`** (or the equivalent cloud-service configuration file) to the private repo and include it in the submission.
- No API keys to obtain, no configuration changes, no missing resources.

## What is open (team decision — `DEC-01`)

The brief mandates *that* persistence + CRUD + cloud sync exist, but the team chooses *which* combination (e.g., which local store, which data goes where, which cloud service) — and must **justify the assignment of particular data to each store** in the report (`BRIEF-06` §4).
