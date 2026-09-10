

## COSC3062|COSC3063 iPhone Software Engineering
Assignment 2 - Group Project (40%)
Deadline: 5PM Friday of week 11

**Duration:** ~4 weeks

**Type:** Team of 5 students

**Feedback mode:** Not available because this is the second last assessment

**Late work:** A penalty of 10% per day is applied for up to 5 days late. After 5 days, the penalty is 100%. 

## Learning Objectives Assessed

- Describe the limitations and challenges of working in a mobile environment as well as the commercial and research opportunities presented by these technologies.

- Apply the different types of application models/frameworks used to develop mobile software applications

- Learn about the components and structure of the iPhone application development framework and know how and when to apply the different components to develop a working system.

- Describe and apply software patterns for the development of the application models described above.

- Apply critical analysis, problem solving, and team facilitation skills to mobile app software engineering scenarios.

## Ready for Life and Work

- Analyze and design a solution in Swift for a given problem.

- Implement the solution using Xcode.

- Test and debug using Xcode.

- Manage source code using GitHub.

- Work efficiently in team.

# Assessment Details

### The Hackathon Challenge

This final project simulates a **4******-**week technology hackathon** where you will work in a team to design and develop an innovative iOS game.

Vietnam has a rich and diverse cultural heritage shaped by generations of communities, regions, traditions, crafts, games, stories, performances, foodways, festivals, and everyday practices. However, cultural heritage remains meaningful not simply by being documented or displayed, but by being **experienced, understood, shared, adapted, and passed on to future generations**.

In this project, you will explore how mobile technology and game design can help a contemporary audience engage with Vietnamese cultural heritage in an interactive and meaningful way.

The theme for this game hackathon is:

## **"Living Heritage - Vietnam: Culture in Play"******

 

### Reimagining Vietnamese Living Heritage for the Digital Generation

**Your team's mission is to design and develop an educational iOS game inspired by an aspect of Vietnamese cultural heritage.**

Your game should allow players to **experience, understand, preserve, reinterpret, or engage with Vietnamese culture through gameplay**.

The objective is **NOT simply to create a game with Vietnamese graphics or cultural trivia**. Instead, the selected cultural knowledge, practice, process, rules, values, or traditions should meaningfully influence how the game is played.

### International Group Option

The default cultural context for this assignment is **Vietnam**.

However, if the **majority of members in a group are not Vietnamese**, the group may choose to base its project on the living cultural heritage of another country that is meaningfully connected to the backgrounds of its group members.

For example, a group whose majority of members come from **Indonesia **may choose to explore **Indonesian **living heritage instead of Vietnamese living heritage.

Changing the country does not change the nature or difficulty of the assessment. The project must still focus on **living cultural heritage** and must demonstrate how cultural knowledge can be transformed into meaningful gameplay.

Groups with a majority of Vietnamese members must use **Vietnamese living heritage** as the context for their project.

### Core Concept: An Educational Game App

Instead of developing a standard application, your team will build an educational iOS game. 

The game should be a:

- board game;

- card game;

- dice game;

- turn-based strategy game;

- resource-management game;

- puzzle or matching game with meaningful strategic mechanics;

- route-planning or exploration game;

- simulation game;

- or another simple, manageable** form of 2D game**. If your concept does not clearly fit one of the categories above, confirm it with your tutor before beginning development.

The game must be achievable within the project timeframe and within the technical scope of this course.

You are encouraged to think about the following question: **"What makes this Vietnamese cultural tradition playable?"**

For example, a traditional craft might contain decisions about materials, processes, timing, quality, resources, or techniques that can become gameplay mechanics.

A traditional game may already contain well-established rules, but your team could reinterpret those rules through new challenges, progression systems, educational elements, or strategic mechanics.

A festival might involve planning, timing, community participation, food, performances, rituals, and resource allocation.

A culinary tradition might involve ingredients, geography, seasonality, preparation techniques, and combinations that influence gameplay.

The cultural heritage should therefore be **embedded into the game system itself**, rather than added only as text, images, facts, or decoration.

#### Inspiration for Cultural Heritage Themes

Your game could tackle a variety of Vietnamese cultural heritage and translate important characteristics of that heritage into an interactive game system.

Possible areas include:

- Traditional Arts and Crafts.

- Music and Performing Arts.

- Festivals and Community Traditions.

- Vietnamese Foodways and Culinary Heritage.

- Folklore and Storytelling.

- Places, Architecture, and Regional Identity like focusing on the living practices attached to those places: village crafts, spatial customs, rituals, markets, and community life, rather than the buildings alone.

- Language and Everyday Cultural Practices.

These examples are intended as inspiration only.

**You are strongly encouraged to investigate and propose your own topic.**

Your chosen topic must have a meaningful relationship with the culture you have chosen and must be appropriately researched.

### Scope and Framework Restrictions

Keep your project scope manageable for completion within the allocated timeframe.

**Apple GameKit and SpriteKit are outside the taught scope of this course.**

You should therefore design your game primarily using SwiftUI and technologies covered in the course.

If your team chooses to independently learn SpriteKit, GameKit, or another advanced framework for a particularly ambitious idea, you may do so at your own risk. However, teaching staff may not be able to provide extensive technical support for frameworks outside the course scope.

### Technical Requirements

#### 1. Application Architecture & Core Functionality

- **Architecture:**

 - The app must be built using the **Model-View-ViewModel (MVVM)** design pattern.

 - 

Your project structure should clearly demonstrate appropriate separation between:

 - Models.

 - Views

 - ViewModels.

 - Persistence and data services.

 - Other supporting components.

- **User Management:**

 - Implement **registration (sign-up)**, **log-in**, and **log-out** features.

 - Allow users to create and customize their **profiles** with an avatar, bio, and other relevant information.

- **Data Persistence & Synchronisation:**

 - Implement full **CRUD (Create, Read, Update, Delete)** operations for relevant game data (e.g., user profiles, game progress, leaderboard scores).

 - **Utilize one or more** of the following for data persistence, justifying your choice in the report: **Core Data (or SwiftData), Firebase, or UserDefaults**.

 - Implement **user data synchronization** using a cloud service like **Firebase** to ensure a consistent experience across multiple devices.

#### 2. Game Structure and Views

The game must consist of at least the following five core views:

- 

##### **Menu View (Welcome View):**

 - The initial screen with navigation to other views.

 - Must include options to **Start New Game**, **Continue** (for saved games), **Leaderboard**, **How To Play**, and **Settings**.

 - Should display login/logout status and provide access to the user's profile.

- 

##### **Game View:**

 - The primary screen where the 2D game is played.

 - Must display the current score, game status, and other relevant information.

 - Incorporate **animations** for player actions and game events at minimum three distinct animations, for example a move or placement action, a scoring or feedback event, and a view transition..

 - Display a "Game Over" screen upon completion.

- 

##### **Leaderboard View:**

 - Display a list of high scores with corresponding usernames.

 - Feature **achievement badges** (name and image) that users earn for reaching educational or gameplay milestones.

 - Include **interactive graphs** (e.g., bar charts, line charts) to visualize player statistics like win percentage, score trends, or games played.

- 

##### **How To Play View:**

 - Provide clear, concise instructions on the game's rules and objectives.

 - Implement an **interactive tutorial** with visual aids, animations, and prompts to guide new players through the mechanics and strategies.

- 

##### **Game Settings View:**

 - Allow users to adjust game **difficulty** (e.g., Easy, Medium, Hard) with descriptions for each level.

 - You could offer different **game variations** or rule sets to enhance replayability for each difficulty.

 - Include a **theme switcher** to toggle between custom light and dark themes for the app.

 - Implement **multi-language support** (at least English and one other language, e.g., Vietnamese) via a picker or dropdown menu.

#### 3. Gameplay and User Experience Features

- **Game Progression and Levels:** Structure the game with levels or stages of increasing difficulty to keep the gameplay engaging and progressively introduce new educational elements.

- **Sound and UI:**

 - **Background Music:** Include appropriate background music for the Menu, How To Play, and Leaderboard views.

 - **Sound Effects:** Implement sound effects for key user interactions and game events (e.g., taking an action, winning/losing, game result).

- **Animated Splash Screen:** Design a professional, animated splash screen that appears when the app launches.

- **Search and Filter (Contextual):** Implement search or filter functionality where it adds value, such as searching for a specific rule in the "How To Play" view or filtering the leaderboard by achievements.

#### 4. Device and System Compatibility

- **Device Support:** The UI must be responsive and function correctly on **iPhone 17, 17 Pro, 17 Pro Max, and 11-inch iPad Air**.

- **System Theme Support:** The app must look appealing and be fully functional in both the system's light and dark modes, without UI glitches.

#### 5. Industry Requirements from the Week 7 Guest Lecture

As part of this assessment, each team must implement **two industry requirements** introduced and discussed during the Week 7 Guest Lecture.

These requirements are intended to expose you to current industry expectations, professional development practices, and considerations that may not be fully covered in the regular weekly course content.

**Students are strongly expected to sign up for and attend the Week 7 Guest Lecture posed in the Canvas annoucement.**

**Your team should use the lecture to identify suitable requirements that can be meaningfully incorporated into your iOS project.**

If your implementation differs from the best-practice approach presented during the guest lecture, you should clearly explain and justify the reason for that decision.

#### 6. Optional Advanced Features

- **AI Game Opponent (not applicable to all game types)**: For games involving an opponent, consider implementing a simple rule-based AI using conditional logic to create a more challenging single-player experience.

- **Local Notifications:** Implement in-app or local notifications to remind users of saved games, new challenges, or to share interesting facts related to your chosen cultural heritage.

- **Accessibility:** Implement accessibility features like **VoiceOver support, dynamic type, and sufficient color contrast** to make the app usable for people with disabilities.

- **Save and Resume:** Allow players to save their progress in an ongoing game and resume it later, even after fully closing the app.

 - When user exit from the app, it does not mean they press home button or swipe up as the app is still in the memory.

 - It does mean they need to hold and swipe up to totally remove the app from the memory. You can refer to this video:
https://www.youtube.com/watch?v=abjFdj7yexI [https://www.youtube.com/watch?v=abjFdj7yexI] .

### Aesthetic and User-Centric Design

Your app will be evaluated on its visual appeal and usability based on professional standards like Apple's Human Interface Guidelines.

- **Visual Appeal:** The app must have a unique, polished, and visually engaging design, with well-chosen color schemes, fonts, and layouts for both light and dark themes.

- **Intuitive User Interface:** The interface should be intuitive and easy to navigate, even for first-time users.

- **Consistency:** Maintain a consistent design language (fonts, colors, imagery, component styles) throughout the app for a professional user experience.

- **User-Centered Design:** The design philosophy must prioritize the user's needs, creating a smooth and frictionless journey.

### Documentation and Presentation

#### 1. The Report (PDF Document)

Your report should be professionally formatted (cover page, table of contents, page numbers) and be a maximum of 30 pages (excluding the cover page, table of contents, references, and appendices). Per-feature screenshots may be placed in an appendix and referenced from the body. It must include:

1. **Introduction & Context:**

 - Application name, purpose, and target audience.

 - Inspiration for the topic and how it relates to the assignment theme.

 - Justification of the topic's relevance and originality within your chosen cultural context.

 - Explanation of why the heritage is worth understanding, experiencing, preserving, or reinterpreting.

 - Explanation of the game's rules and educational goals.

 - In short, you must clearly explain your game's "Cultural Element → Gameplay Mechanic → Player Learning" relationship.

2. **Research and Cultural Representation**

 - How your team researched the selected heritage;

 - Important information discovered during the research process;

 - regional, historical, linguistic, or community-specific considerations where relevant;

 - how you attempted to represent the selected heritage responsibly and accurately;

 - which aspects are authentic;

 - which aspects have been simplified for gameplay;

 - which elements are creative reinterpretations.****

3. **Competitor Analysis:**

 - Identify relevant existing products.

 - Describe your app's "killer feature(s)" that make it stand out.

 - A killer feature is a distinctive functionality, gameplay mechanic, educational approach, cultural integration, or user experience that provides a strong reason for a user to choose your application over comparable alternatives.

4. **Implementation Details:**

 - Detailed explanation of all implemented features (core and advanced).

 - For each feature: provide a UI screenshot, a brief technical explanation of its implementation.

 - Justify your choice of cloud service and any local persistence mechanisms used, including why you assigned particular data to each (Core Data, Firebase, UserDefaults).

5. **Application of Industry Best Practice**

 - 

Explain whether your implementation follows the recommended best practices discussed during the **Week 7 Guest Lecture.**

 - 

Your discussion should identify specific recommendations from the lecture and explain how they influenced your design or implementation.

 - Do not simply state that your implementation "follows best practice." Provide evidence and explanation.

6. **Application Flow Diagram:** A diagram illustrating how different views and components interact, designed with the MVVM architecture in mind.

7. **Technologies Used:** A list of all Swift/SwiftUI components and any external libraries used.

8. **Design and User Experience:** Explain your design choices (colors, fonts, layout) and how you achieved an intuitive, consistent, and user-centered design.

9. **Known Bugs/Problems:** A list of any unresolved issues.

10. **Conclusion:** Reflection on what was learned and potential future improvements.

11. **Project Responsibilities**: a table of **each member's actual responsibilities** and **workload (%)** in relation to the project subtasks, based on your task breakdown. **Percentages must total 100%.** Identify which member served as Project Manager and which as Technical Lead. This table must be discussed and agreed by the whole team and finalised by the Project Manager.

12. **References & Appendices.**

#### 2. The Video Presentation

Create a single video (max **10 minutes**) and upload it to YouTube as an "**unlisted**" video. The video must include **two parts** as following:

1. **Project Presentation:** A slide-based presentation where all team members explain the project's analysis, design, and implementation, reflecting the report's structure.

2. **Application Demo:** A live demonstration of the app showcasing all implemented features. This part should be prioritized.

The time allocation of these two parts is up to you as long as the whole video must be within the time limit while **the actual application demo is more important and should be more prioritized, which showcases all of the required features of your app.**

All group members must appear and speak in the recorded video. Any member who does not appear, or whose contribution is not meaningful, will receive a mark of zero for the presentation component. Introduce yourself by name at the start of your segment so that markers can identify each speaker. It is also an excellent opportunity for each team member to improve their presentation skills and gain experience working in a group. I would encourage each team member to review their work and prepare well before the demo to make the best impression.

## Deliverables

- Each source code file must have the following header at the top of the file.

/*
  RMIT University Vietnam
 Course: COSC3062|COSC3063 iPhone Software Engineering
 Semester: 2026B 
 Assessment: Assignment 2
  Author: Your name (e.g. Nguyen Van Minh)
  ID: Your student id (e.g. 1234567)
 Created  date: dd/mm/yyyy (e.g. 31/07/2026)
 Last modified: dd/mm/yyyy (e.g. 05/08/2026)
  Acknowledgement: Acknowledge the resources that you use here. 
*/

- **Test your app carefully in one of the iMac computers in the lab to resolve any unforeseen issues before submitting it. **

- **Your app will be tested in the simulator of Xcode 26.4.1 and the target of iOS 26.4.1 on the iPhone 17 Pro Simulator in a Mac computer similar to that.**

 - If you develop your app on an older version of Xcode on a personal MacBook, compile and run your app on a lab iMac before submitting.

## Project Deliverables 

- Your submission must include all of the following:

1. 

 1. **Complete Xcode project and source code**

 - Include the complete Xcode project, Swift source files, asset catalogues, bundled JSON data, images, and all other resources required to compile and run the app.

 - The submitted source code must be identical to the source code in the final commit of your assigned private GitHub repository.

 - Commit GoogleService-Info.plist (or the equivalent configuration file) to your private repository and include it in your submission, so that the marker can build and run without obtaining credentials.

 - The project must compile and run without requiring the marker to repair file references, download missing resources, obtain API keys, or change the project configuration.

 2. **Document.pdf**

 - This is the required project report.

 - The filename must be exactly Document.pdf.

 3. **GitHub.txt******

 - The file must contain **only the complete URL of the private GitHub repository** assigned to your team by the teaching team.

 - Do not include other information in this file.

 - **For example**: https://github.com/rmit-vietnam-computing-technologies/2026b-COSC3062-a2-sg-my-group-name

 4. **Youtube.txt******

 - The file must contain only the URL of your YouTube demo presentation video.

 - Do not include other information in this file.

 - For example: https://youtu.be/AbCdEfGhIjk


## Submission Instructions

- Compress your submission using the following filename format: iOS_Assignment2_NameOfYourApp_YourGroupName.zip

 - 

Replace NameOfYourApp and YourGroupName with your actual app and group names. For example: iOS_Assignment2_LangNghe_TeamPhoenix.zip

- 

**Your submission MUST follow this ZIP structure:**

| 
**iOS_Assignment2_NameOfYourApp_YourGroupName.zip**
**└── iOS_Assignment2_NameOfYourApp_YourGroupName/**
**    ├── SourceCode/     *(Inside this folder is exactly the copy of your project in your private Github repo)***
**    │   └── NameOfYourApp/                                      **
**    │       ├── Your whole Xcode project here**
**    ├── Document.pdf**
**    ├── GitHub.txt**
**    └── Youtube.txt** | 

The following names must otherwise be used exactly:

- SourceCode

- Document.pdf

- GitHub.txt

- Youtube.txt


Inside SourceCode/NameOfYourApp/, preserve a complete and working Xcode project.

Failure to follow the required structure or filenames will be treated as submission non-compliance and will be assessed under the Code Quality, GitHub Repository and Submission Organisation criterion in the marking rubric attached on Canvas.

Submit the ZIP file to Canvas before the due date and time. You may submit more than once, but only the latest submission will be graded.

### Assigned GitHub Repository

- For this assignment, each team will be provided with an individual private GitHub repository in the following GitHub organization: **rmit-vietnam-computing-technologies**

- The teaching team will create the repository and add each member of your team as a collaborator. You do not need to create the repository yourself.

- 

Your repository name will follow this format: **<year>-<course>-<assignment>-<campus>-<your-group-name>**

- 

For example: **2026b-COSC3062-a2-sg-your-group-name**

### Accepting Your Repository Invitation

After your repository has been created:

1. GitHub will send a collaborator invitation to the email address associated with your GitHub account.

2. Open the invitation email and accept the invitation.

3. You must accept the invitation within **seven days**. GitHub invitations expire after this period. 

4. After accepting the invitation, confirm that you can access the private repository in the **rmit-vietnam-computing-technologies** organization. The link for the organization is https://github.com/rmit-vietnam-computing-technologies/. [https://github.com/rmit-vietnam-computing-technologies/] 

5. You should see your private repository in our organization.

6. Clone/Setup the assigned repository to your computer/Xcode and use it for all development work for this assignment.

Check your spam or junk-mail folder if you cannot find the invitation. If the invitation has expired, your GitHub username is incorrect, or you cannot access the repository, contact the teaching team as soon as possible.

### Repository Requirements

- All project code must be committed and pushed to the private GitHub repository assigned to you by the teaching team.

- Do not create or use a personal public repository for this assignment.

- Do not upload, duplicate, mirror, or share your project code in another repository or elsewhere on the internet.

- Work stored outside the assigned private repository may not be accepted for marking.

- The source code in your Canvas ZIP file must be identical to the source code in the final commit of the assigned repository.

- Include the complete URL of the assigned repository in** GitHub.txt**.

### Development-History Requirements

Your GitHub history is part of the assessment evidence. Markers will examine:

- the number of branches;

- the purpose of each branch;

- branch names;

- the number of commits;

- commit dates and timestamps;

- whether commits are reasonably distributed across the approximately four-week development period;

- whether the development appears incremental or was rushed into a short period immediately before submission;

- the clarity and meaning of commit messages;

- whether branches were merged logically;

- whether the repository shows an understandable progression from initial setup to the final application.

Commit and branch counts will be considered in relation to the scope and quality of the work. A large number of empty, trivial, duplicated, or artificially divided commits will not receive additional credit.

Use branches appropriately for separate features, fixes, refactoring work, or development stages.

Students are not expected to create a separate branch for every small change. Branches should have a clear purpose and should represent meaningful units of work.

As a guide, a project of this scope would be expected to show roughly one branch per feature or development stage, and regular commits from every team member across the full four weeks, rather than a small number of large uploads.

### README Requirement

The repository must contain a comprehensive README.md that includes:

- the project name;

- a concise project description;

- The cultural heritage the game is based on, and a short summary of your Cultural Element → Gameplay Mechanic → Player Learning relationship;

- setup and build instructions;

- instructions for running and using the app, including a demo account (username and password) that the marker can log in with.

- the required Xcode and iOS versions;

- any known issues or limitations;

- any additional information required by the marker.

Before submitting, confirm that:

- all relevant branches have been pushed;

- the intended final work has been merged into the default branch;

- the final project builds from a fresh clone;

- all required assets and JSON resources are tracked;

- no required source file exists only on your local computer;

- the source code in the Canvas ZIP matches the final repository commit.

Remember important points:

- **All project code must be hosted within the private repository in our GitHub Organization instead of your personal public Github repository**. **Please do not use personal public GitHub repositories for this project. **

- **Storing code in personal repositories could expose it to copying by other teams, which would lead to serious issues of plagiarism. These problems have happened in the past.**

- **Otherwise, your project code will not be marked! Also, please ensure your project code is not leaked or duplicated in other public Github repo or anywhere on the internet to avoid plagiarism!**

## Teamwork

Each team must nominate a Project Manager and a Technical Lead, and record both roles in the Project Responsibilities table of the report.

The Project Manager is responsible for planning and controlling tasks, chairing meetings, and building good team spirit. The Technical Lead is responsible for evaluating and making major technical decisions, and acts as gatekeeper of the team's GitHub repository, determining what is accepted into the default branch.

The Technical Lead may also coach other members on specific technical tasks such as design, coding, debugging, and testing. Holding a role does not reduce a member's expected development contribution. Contribution is assessed overall: initiative (helping manage the project, contributing strong ideas), amount of work, quality of work, and support given to other members.

## Plagiarism

Plagiarism is a form of cheating. It is the presentation of the work, idea or creation of other people's as though it is your own.  

This is a team assessment thus everything must be done by your team members. Do not help or collaborate with people outside of your team. If you use any resources, write an acknowledgment in the file where the resources were used. Any submission found in whole or in part plagiarized will be considered as plagiarism. Please ask your Lecturer if you are in doubt. 

The penalty for plagiarism is extremely severe at RMIT. If you are found to plagiarize, you will receive no marks for an assessment or even an entire course. Repeated plagiarism will lead to exclusion from RMIT. 

For more information, visit RMIT’s website for Academic integrity information and policy [https://www.rmit.edu.au/students/student-essentials/assessment-and-exams/academic-integrity] . 

## Support Resources

This assessment requires that you meet RMIT's expectations for academic integrity. More information and advice on how to avoid plagiarism are available in the Getting Started module.

- Open the Academic Integrity [https://www.rmit.edu.au/students/student-essentials/assessment-and-results/academic-integrity] page

 

 
 1789120800
 09/11/2026
 05:00pm
 

 

 
 
 
- File Upload [#submit_online_upload_form] 
 
- Echo360 Homework Embed [#submit_from_external_tool_form_177980] 
 
- Google Drive [#submit_from_external_tool_form_326] 
 
- Microsoft Education [#submit_from_external_tool_form_200833] 
 
- Microsoft OneDrive [#submit_from_external_tool_form_126138] 
 
- Studio [#submit_from_external_tool_form_38] 
 

 

 
 
 
 

 
| 
 
 Upload a file, or choose a file you've already uploaded.
 

 

 | 
 
| 
 
 File:
 
 **
 Add Another File
 
 
 
 **remove empty attachment [#] 
 
 This file type is not allowed. Accepted file types are: zip
 
 
 | 
 
 
| 
 
 Click here to find a file you've already uploaded

 
 | 
 
 
| 
 
 
 
 

 
 
 
 
 | 
 
 
 
| 
 All comments are sent to the whole group.
 
 | 

 

 

 
| 
 
 Cancel
 Submit Assignment
 
 | 
 
 

 

 
 
 
 
 
 

 

 
 
 
 
 

## 
 Rubric
 
 
 
 
 
 Title:
 
 
 
 ![](https://du11hjcvx0uqb.cloudfront.net/dist/images/find-6164443e2a.png) Find Rubric
 [https://rmit.instructure.com/search/rubrics?q=] 
 
 *
 Please include a title
 *
 
 

 
 
 Find a Rubric
 [https://rmit.instructure.com/search/rubrics?q=] 
 

 
 iOS Rubric Assignment 2
 
 
 You've already rated students with this rubric. Any major changes could affect their assessment results.
 

 
 ** [/courses/172067/rubrics/680963?rubric_association_id=1005181] 
 ** [https://rmit.instructure.com/search/rubrics?q=] 
 ** [/courses/172067/rubric_associations/1005181] 
 
 true
  
  
  
  
 1005181
  
 
   [/courses/172067/rubric_associations/1005181/assessments/%7B%7B%20assessment_id%20%7D%7D] 
   [/courses/172067/rubrics/%7B%7B%20rubric_id%20%7D%7D] 
   [/courses/172067/rubric_associations/%7B%7B%20association_id%20%7D%7D] 
 
 
 
 Can't change a rubric once you've started using it.
   [/courses/172067/rubric_associations/%7B%7B%20association_id%20%7D%7D] 
 
 

 

 
 
 iOS Rubric Assignment 2
 
 
 
 
| 
 Criteria | 
 Ratings | 
 
 Pts
 | 
 
 
 
 

| 
 
 
 
 
 **
 This criterion is linked to a Learning Outcome
 
 
 Creativity, Innovation & Cultural Relevance
 
 blank
 
 The originality of the game concept and the depth of its connection to the chosen living heritage. This criterion assesses whether the cultural element genuinely shapes how the game is played, rather than appearing as setting, artwork, or trivia layered onto a generic game. Depth and specificity of cultural research are assessed here, alongside the significance of the heritage chosen and the team's understanding of why it is worth experiencing, preserving, or reinterpreting.

For approved international groups, "Vietnamese" below refers to the group's approved heritage context.
 
 
 threshold:
 pts
 
 
 
 
 
 
 
 Range
 
 
 
 
 

 
 **Edit criterion description [#] 
 
 
 | 
 
 
 
 
 
 
 
 6
 to >4.5 pts
 
 Excellent
 The concept is highly original and could not be transferred to an unrelated subject without the game breaking. A specific, well-researched aspect of Vietnamese living heritage, such as its rules, processes, values, constraints, seasonality, or decision-making, directly generates the core gameplay mechanic. The cultural logic is visible in how the player thinks and decides, not only in what they see and read. The team demonstrates deep understanding of the heritage's significance and genuine insight into why it is worth passing on.
 
 384872_4226
 
 
 **
 [#] 
 
 **
 [#] 
 
 
 
 ** [#] 
 
 
 
 
 
 
 
 
 4.5
 to >3.0 pts
 
 Very Good
 The concept is original and the chosen heritage is well researched and clearly represented. Cultural knowledge meaningfully shapes significant parts of the gameplay, though one or more core mechanics remain generic or could be transferred to an unrelated theme without much loss. The heritage-to-play connection is clear and deliberate, but not sustained across the whole game system.
 
 384872_7405
 
 
 **
 [#] 
 
 **
 [#] 
 
 
 
 ** [#] 
 
 
 
 
 
 
 
 
 3
 to >1.5 pts
 
 Good
 The concept is workable but conventional, closely resembling a familiar game type. The heritage is present mainly through setting, artwork, names, or factual content, with limited influence on the rules or on the decisions the player actually makes. Research is basic and engages the heritage broadly rather than specifically. Educational value depends largely on text the player reads rather than on play.
 
 384872_9752
 
 
 **
 [#] 
 
 **
 [#] 
 
 
 
 ** [#] 
 
 
 
 
 
 
 
 
 1.5
 to >0 pts
 
 Need improvement
 The concept shows little originality. The heritage appears only as decoration, such as visuals, labels, or trivia attached to a generic game, or it is represented superficially, inaccurately, or in a way that reduces the tradition to stereotype. There is little evidence of research, or of understanding why the heritage is significant.
 
 384872_3705
 
 
 **
 [#] 
 
 **
 [#] 
 
 
 
 
 
 
 This area will be used by the assessor to leave comments related to this criterion.
 
 | 
 
 
 
 pts
 

 
 
 
 
   /
 
 6 pts

 
 
 
 -- 
 
 
 
 ![Additional Comments](https://du11hjcvx0uqb.cloudfront.net/dist/images/rubric_comment-ddae8546ab.png)
 [#] 
 
 
 | 

 

| 
 
 
 
 
 **
 This criterion is linked to a Learning Outcome
 
 
 Technical Requirements
 
 _2699
 
 Your code should get all required features correctly in all use cases.
 
 
 threshold:
 pts
 
 
 
 
 
 
 
 Range
 
 
 
 
 

 
 **Edit criterion description [#] 
 
 
 | 
 
 
 
 
 
 
 
 8
 to >6.4 pts
 
 Excellent
 All criteria fully met and functionally correct with no improvements identified.
 
 _6233
 
 
 **
 [#] 
 
 **
 [#] 
 
 
 
 ** [#] 
 
 
 
 
 
 
 
 
 6.4
 to >4.8 pts
 
 Very Good
 Almost all criteria fully met and functionally correct with 1 improvements identified.
 
 _5879
 
 
 **
 [#] 
 
 **
 [#] 
 
 
 
 ** [#] 
 
 
 
 
 
 
 
 
 4.8
 to >3.2 pts
 
 Good
 Some criteria fully met and functionally correct with 2 improvements identified.
 
 384872_9006
 
 
 **
 [#] 
 
 **
 [#] 
 
 
 
 ** [#] 
 
 
 
 
 
 
 
 
 3.2
 to >1.6 pts
 
 Fair
 Some criteria fully met and functionally correct with 3 improvements identified.
 
 477073_6303
 
 
 **
 [#] 
 
 **
 [#] 
 
 
 
 ** [#] 
 
 
 
 
 
 
 
 
 1.6
 to >0 pts
 
 Need improvement
 Few criteria met and functionally correct with 4 or more improvements identified.
 
 _2377
 
 
 **
 [#] 
 
 **
 [#] 
 
 
 
 
 
 
 This area will be used by the assessor to leave comments related to this criterion.
 
 | 
 
 
 
 pts
 

 
 
 
 
   /
 
 8 pts

 
 
 
 -- 
 
 
 
 ![Additional Comments](https://du11hjcvx0uqb.cloudfront.net/dist/images/rubric_comment-ddae8546ab.png)
 [#] 
 
 
 | 

 

| 
 
 
 
 
 **
 This criterion is linked to a Learning Outcome
 
 
 Optional Advanced Features
 
 576884_8354
 
 Your code should get all required features correctly in all use cases.
 
 
 threshold:
 pts
 
 
 
 
 
 
 
 Range
 
 
 
 
 

 
 **Edit criterion description [#] 
 
 
 | 
 
 
 
 
 
 
 
 6
 to >4.8 pts
 
 Excellent
 All criteria fully met and functionally correct with no improvements identified.
 
 576884_4663
 
 
 **
 [#] 
 
 **
 [#] 
 
 
 
 ** [#] 
 
 
 
 
 
 
 
 
 4.8
 to >3.6 pts
 
 Very Good
 Almost all criteria fully met and functionally correct with 1 improvements identified.
 
 576884_9069
 
 
 **
 [#] 
 
 **
 [#] 
 
 
 
 ** [#] 
 
 
 
 
 
 
 
 
 3.6
 to >2.4 pts
 
 Good
 Some criteria fully met and functionally correct with 2 improvements identified.
 
 576884_242
 
 
 **
 [#] 
 
 **
 [#] 
 
 
 
 ** [#] 
 
 
 
 
 
 
 
 
 2.4
 to >1.2 pts
 
 Fair
 Some criteria fully met and functionally correct with 3 improvements identified.
 
 576884_7866
 
 
 **
 [#] 
 
 **
 [#] 
 
 
 
 ** [#] 
 
 
 
 
 
 
 
 
 1.2
 to >0 pts
 
 Need improvement
 Few criteria met and functionally correct with 4 or more improvements identified.
 
 576884_7726
 
 
 **
 [#] 
 
 **
 [#] 
 
 
 
 
 
 
 This area will be used by the assessor to leave comments related to this criterion.
 
 | 
 
 
 
 pts
 

 
 
 
 
   /
 
 6 pts

 
 
 
 -- 
 
 
 
 ![Additional Comments](https://du11hjcvx0uqb.cloudfront.net/dist/images/rubric_comment-ddae8546ab.png)
 [#] 
 
 
 | 

 

| 
 
 
 
 
 **
 This criterion is linked to a Learning Outcome
 
 
 Aesthetic and User-Centric Design
 
 384872_2830
 
 This aspect evaluates the overall visual appeal and usability of the mobile app. Key points of consideration include: Visual Appeal, Intuitive User Interface, Consistency, User-Centered Design.
 
 
 threshold:
 pts
 
 
 
 
 
 
 
 Range
 
 
 
 
 

 
 **Edit criterion description [#] 
 
 
 | 
 
 
 
 
 
 
 
 5
 to >4.0 pts
 
 Excellent
 All criteria fully met and functionally correct with no improvements identified.
 
 384872_7647
 
 
 **
 [#] 
 
 **
 [#] 
 
 
 
 ** [#] 
 
 
 
 
 
 
 
 
 4
 to >3.0 pts
 
 Very Good
 Almost all criteria fully met and functionally correct with 1 improvements identified.
 
 384872_3361
 
 
 **
 [#] 
 
 **
 [#] 
 
 
 
 ** [#] 
 
 
 
 
 
 
 
 
 3
 to >2.0 pts
 
 Good
 Some criteria fully met and functionally correct with 2 improvements identified.
 
 477073_1570
 
 
 **
 [#] 
 
 **
 [#] 
 
 
 
 ** [#] 
 
 
 
 
 
 
 
 
 2
 to >1.0 pts
 
 Fair
 Some criteria fully met and functionally correct with 3 improvements identified.
 
 384872_9057
 
 
 **
 [#] 
 
 **
 [#] 
 
 
 
 ** [#] 
 
 
 
 
 
 
 
 
 1
 to >0 pts
 
 Need improvement
 Few criteria met and functionally correct with 4 or more improvements identified.
 
 384872_3300
 
 
 **
 [#] 
 
 **
 [#] 
 
 
 
 
 
 
 This area will be used by the assessor to leave comments related to this criterion.
 
 | 
 
 
 
 pts
 

 
 
 
 
   /
 
 5 pts

 
 
 
 -- 
 
 
 
 ![Additional Comments](https://du11hjcvx0uqb.cloudfront.net/dist/images/rubric_comment-ddae8546ab.png)
 [#] 
 
 
 | 

 

| 
 
 
 
 
 **
 This criterion is linked to a Learning Outcome
 
 
 Report (Written Document)
 
 384872_6478
 
 Professional & clean format, clear and detailed description, easy to read and follow, helpful visuals aids (image, screenshots, diagram, gifs, video), English writing quality, fulfill requirements of the report.
 
 
 threshold:
 pts
 
 
 
 
 
 
 
 Range
 
 
 
 
 

 
 **Edit criterion description [#] 
 
 
 | 
 
 
 
 
 
 
 
 6
 to >4.8 pts
 
 Excellent
 All criteria fully met and functionally correct with no improvements identified.
 
 384872_9202
 
 
 **
 [#] 
 
 **
 [#] 
 
 
 
 ** [#] 
 
 
 
 
 
 
 
 
 4.8
 to >3.6 pts
 
 Very Good
 Almost all criteria fully met and functionally correct with 1 improvements identified.
 
 384872_3820
 
 
 **
 [#] 
 
 **
 [#] 
 
 
 
 ** [#] 
 
 
 
 
 
 
 
 
 3.6
 to >2.4 pts
 
 Good
 Some criteria fully met and functionally correct with 2 improvements identified.
 
 384872_7876
 
 
 **
 [#] 
 
 **
 [#] 
 
 
 
 ** [#] 
 
 
 
 
 
 
 
 
 2.4
 to >1.2 pts
 
 Fair
 Some criteria fully met and functionally correct with 3 improvements identified.
 
 477073_7853
 
 
 **
 [#] 
 
 **
 [#] 
 
 
 
 ** [#] 
 
 
 
 
 
 
 
 
 1.2
 to >0 pts
 
 Need improvement
 Few criteria met and functionally correct with 4 or more improvements identified.
 
 384872_2087
 
 
 **
 [#] 
 
 **
 [#] 
 
 
 
 
 
 
 This area will be used by the assessor to leave comments related to this criterion.
 
 | 
 
 
 
 pts
 

 
 
 
 
   /
 
 6 pts

 
 
 
 -- 
 
 
 
 ![Additional Comments](https://du11hjcvx0uqb.cloudfront.net/dist/images/rubric_comment-ddae8546ab.png)
 [#] 
 
 
 | 

 

| 
 
 
 
 
 **
 This criterion is linked to a Learning Outcome
 
 
 Video Demonstration & Presentation
 
 384872_5821
 
 - Explain clearly how the system is developed.

- The demo demonstrates exactly the app functionalities.

- Professional & clean format, easy to listen and follow.

- Each team member take turn to present their part.

- Present with visual aids.

- Video length is within the length limit.
 
 
 threshold:
 pts
 
 
 
 
 
 
 
 Range
 
 
 
 
 

 
 **Edit criterion description [#] 
 
 
 | 
 
 
 
 
 
 
 
 5
 to >4.0 pts
 
 Excellent
 All criteria fully met and functionally correct with no improvements identified.
 
 384872_9124
 
 
 **
 [#] 
 
 **
 [#] 
 
 
 
 ** [#] 
 
 
 
 
 
 
 
 
 4
 to >3.0 pts
 
 Very Good
 Almost all criteria fully met and functionally correct with 1 improvements identified.
 
 384872_3015
 
 
 **
 [#] 
 
 **
 [#] 
 
 
 
 ** [#] 
 
 
 
 
 
 
 
 
 3
 to >2.0 pts
 
 Good
 Some criteria fully met and functionally correct with 2 improvements identified.
 
 384872_2663
 
 
 **
 [#] 
 
 **
 [#] 
 
 
 
 ** [#] 
 
 
 
 
 
 
 
 
 2
 to >1.0 pts
 
 Fair
 Some criteria fully met and functionally correct with 3 improvements identified.
 
 477073_1450
 
 
 **
 [#] 
 
 **
 [#] 
 
 
 
 ** [#] 
 
 
 
 
 
 
 
 
 1
 to >0 pts
 
 Need improvement
 Few criteria met and functionally correct with 4 or more improvements identified.
 
 384872_5161
 
 
 **
 [#] 
 
 **
 [#] 
 
 
 
 
 
 
 This area will be used by the assessor to leave comments related to this criterion.
 
 | 
 
 
 
 pts
 

 
 
 
 
   /
 
 5 pts

 
 
 
 -- 
 
 
 
 ![Additional Comments](https://du11hjcvx0uqb.cloudfront.net/dist/images/rubric_comment-ddae8546ab.png)
 [#] 
 
 
 | 

 

| 
 
 
 
 
 **
 This criterion is linked to a Learning Outcome
 
 
 Well-formatted, Organized Code & Github Repository
 
 384872_6391
 
 - Code follows consistent style guidelines, is well-organized, and includes comments where necessary. Best practices are followed.; Nice code format (consistent indent code, blank line between two code sections, etc).

- Have the required header at the top of all source code files.

- Descriptive comment your code.

- Descriptive names that follow the Swift naming convention in the course.

- Well-organized folder structures, etc.

- Commits in Github repo are made frequently and regularly, demonstrating consistent progress.

- Branches in Github repo are used appropriately for different features or fixes, with clear and logical naming conventions.

- ReadMe file in Github repo is comprehensive, including project description, setup instructions, usage examples.
 
 
 threshold:
 pts
 
 
 
 
 
 
 
 Range
 
 
 
 
 

 
 **Edit criterion description [#] 
 
 
 | 
 
 
 
 
 
 
 
 4
 to >3.2 pts
 
 Excellent
 All criteria fully met and functionally correct with no improvements identified.
 
 384872_1928
 
 
 **
 [#] 
 
 **
 [#] 
 
 
 
 ** [#] 
 
 
 
 
 
 
 
 
 3.2
 to >2.4 pts
 
 Very Good
 Almost all criteria fully met and functionally correct with 1 improvements identified.
 
 384872_4373
 
 
 **
 [#] 
 
 **
 [#] 
 
 
 
 ** [#] 
 
 
 
 
 
 
 
 
 2.4
 to >1.6 pts
 
 Good
 Some criteria fully met and functionally correct with 2 improvements identified.
 
 384872_9816
 
 
 **
 [#] 
 
 **
 [#] 
 
 
 
 ** [#] 
 
 
 
 
 
 
 
 
 1.6
 to >0.8 pts
 
 Fair
 Some criteria fully met and functionally correct with 3 improvements identified.
 
 477073_587
 
 
 **
 [#] 
 
 **
 [#] 
 
 
 
 ** [#] 
 
 
 
 
 
 
 
 
 0.8
 to >0 pts
 
 Need improvement
 Few criteria met and functionally correct with 4 or more improvements identified.
 
 384872_1443
 
 
 **
 [#] 
 
 **
 [#] 
 
 
 
 
 
 
 This area will be used by the assessor to leave comments related to this criterion.
 
 | 
 
 
 
 pts
 

 
 
 
 
   /
 
 4 pts

 
 
 
 -- 
 
 
 
 ![Additional Comments](https://du11hjcvx0uqb.cloudfront.net/dist/images/rubric_comment-ddae8546ab.png)
 [#] 
 
 
 | 

 

| 
 
 
 
 
 **
 This criterion is linked to a Learning Outcome
 
 
 Description of criterion
 
 
 
 
 
 
 threshold:
 5 pts
 
 
 
 
 
 
 
 Range
 
 
 
 
 

 
 **Edit criterion description [#] 
 **Delete criterion row [#] 
 
 
 | 
 
 
 
 
 
 
 
 5
 to >0 pts
 
 Full Marks
 
 
 blank
 
 
 **
 [#] 
 
 **
 [#] 
 
 
 
 ** [#] 
 
 
 
 
 
 
 
 
 0
 to >0 pts
 
 No Marks
 
 
 blank_2
 
 
 **
 [#] 
 
 **
 [#] 
 
 
 
 
 
 
 This area will be used by the assessor to leave comments related to this criterion.
 
 | 
 
 
 
 pts
 

 
 
 
 
   /
 
 5 pts

 
 
 
 -- 
 
 
 
 ![Additional Comments](https://du11hjcvx0uqb.cloudfront.net/dist/images/rubric_comment-ddae8546ab.png)
 [#] 
 
 
 | 

 
 

 
 
 
 
 
 Total Points:
 40 out of 40
 
 
 
 
 
 
 
 
 
 I'll write free-form comments when assessing students
 
 
 
 
 
 Remove points from rubric
 
 
 
 
 
 Don't post Outcomes results to Learning Mastery Markbook
 
 
 
 
 
 Use this rubric for assignment marking
 
 
 
 
 
 Hide score total for assessment results
 
 
 
 
 Cancel
 Create Rubric
 
 
 
 

 
 
 
 
 
 

 
 
 
 Description
 
 
 *
 Please include a description
 *
 
 
 Long Description
 
 
 
 
 Cancel
 Update Criterion
 
 
 
 
 
 
 

 
 
 
 Additional Comments:
 
 
 
 Cancel
 Update Comments
 
 
 
 Additional Comments:
 
 
 

 
 
 
 
 
 
 Rating Score
 Rating max score
 
 to >
 
 pts
 
 
 Rating Title
 
 *
 Please include a rating title
 *
 
 
 Rating Description
 
 
 
 Cancel
 Update Rating
 
 
 

 
 
 
 
 

## 
 Rubric
 
 
 
 
 
 Title:
 
 
 
 ![](https://du11hjcvx0uqb.cloudfront.net/dist/images/find-6164443e2a.png) Find Rubric
 [https://rmit.instructure.com/search/rubrics?q=] 
 
 *
 Please include a title
 *
 
 

 
 
 Find a Rubric
 [https://rmit.instructure.com/search/rubrics?q=] 
 

 
 Title
 
 
 You've already rated students with this rubric. Any major changes could affect their assessment results.
 

 
 ** [/courses/172067/rubrics/%7B%7B%20id%20%7D%7D] 
 ** [https://rmit.instructure.com/search/rubrics?q=] 
 ** [/courses/172067/rubric_associations/%7B%7B%20rubric_association_id%20%7D%7D] 
 
  
  
  
  
  
  
  
 
   [/courses/172067/rubric_associations/%7B%7B%20rubric_association_id%20%7D%7D/assessments/%7B%7B%20assessment_id%20%7D%7D] 
   [/courses/172067/rubrics/%7B%7B%20rubric_id%20%7D%7D] 
   [/courses/172067/rubric_associations/%7B%7B%20association_id%20%7D%7D] 
 
 
 
 Can't change a rubric once you've started using it.
   [/courses/172067/rubric_associations/%7B%7B%20association_id%20%7D%7D] 
 
 

 

 
 
 Title
 
 
 
 
| 
 Criteria | 
 Ratings | 
 
 Pts
 | 
 
 
 
 

| 
 
 
 
 
 **
 This criterion is linked to a Learning Outcome
 
 
 Description of criterion
 
 
 
 
 
 
 threshold:
 5 pts
 
 
 
 
 
 
 
 Range
 
 
 
 
 

 
 **Edit criterion description [#] 
 **Delete criterion row [#] 
 
 
 | 
 
 
 
 
 
 
 
 5
 to >0 pts
 
 Full Marks
 
 
 blank
 
 
 **
 [#] 
 
 **
 [#] 
 
 
 
 ** [#] 
 
 
 
 
 
 
 
 
 0
 to >0 pts
 
 No Marks
 
 
 blank_2
 
 
 **
 [#] 
 
 **
 [#] 
 
 
 
 
 
 
 This area will be used by the assessor to leave comments related to this criterion.
 
 | 
 
 
 
 pts
 

 
 
 
 
   /
 
 5 pts

 
 
 
 -- 
 
 
 
 ![Additional Comments](https://du11hjcvx0uqb.cloudfront.net/dist/images/rubric_comment-ddae8546ab.png)
 [#] 
 
 
 | 

 
 

 
 
 
 
 
 Total Points:
 5 out of 5
 
 
 
 
 
 
 
 
 
 I'll write free-form comments when assessing students
 
 
 
 
 
 Remove points from rubric
 
 
 
 
 
 Don't post Outcomes results to Learning Mastery Markbook
 
 
 
 
 
 Use this rubric for assignment marking
 
 
 
 
 
 Hide score total for assessment results
 
 
 
 
 Cancel
 Create Rubric
 
 
 
 

 

 

 
 
 
 
 

 
 
 
 
 

 
 19b7f827-5e19-4610-8ab7-467f406fbd86
 
 
 
 

 

 

 

 

