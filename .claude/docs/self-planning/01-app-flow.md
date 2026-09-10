This is the app flow. Currently, we have:
Main App Screen
1.1. Auth (Login/Signup Page)
1.2. Home Page
1.3. Navigation
1.4. User Profiles (View/Edit)
1.5. Setting Page

Game Play
2.1. Art Selection
2.2. Chapter Selection
2.3. Difficulty Selection
2.4. Current Game View with Card Deck + loaded content from game_content.json
2.5. Save, Resume and Restart mechanism

Main Flow:
1.1 --> 1.2 (After Auth), being able to navigate to 1.4, 1.5. The 1.4 has the View and Update one, which will update to the Firebase as well.
From 1.2, user selects the "Choose Difficulty" or some to use the 2.3

- "Start Game" --> "Art Selection" --> "Chapter Selection" --> Load the game play to the view, swipeable
- In game, user could save & quit, restart or sum.
- In the Chapter Selction also has that feature to restart, resume, continue ...
