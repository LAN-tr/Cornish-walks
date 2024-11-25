# Cornish Walks
## Overview

### Purpose

A Cornish walks app would aim to solve several problems for walkers in cornwall. The key challenges the app would seek to address are:

- Difficulty finding suitable walking trails: The app will provide a searchable database of trails with filters for distance, difficulty level, terrain and scenic features.

- Lack of reliable maps and navigation tools: The app can include GPS-enabled maps for real-time navigation meaning that users do not need to rely on outdated or vague descriptions or drawings.

- Challenges with weather and tides: The app could integrate weather updates and forecasts for specific areas and tide times for beaches and coastal walks.

- Accessibility and inclusivity issues: The app could highlight accessible trails and could indicate suitability for various needs and details about elevation, terrain and rest points.

- Limited community and sharing features: Walkers can share their experiences and review the walks with a space for comments and a way to save walks that they enjoyed, or would like to try next.

This project's purpose is to make exploring Cornwall easier, safer and more enjoyable. It would cater to a diverse range of users; casual walkers, serious hikers, tourists and locals by offering practical tools, curated recommendations and engaging features.


## User Experience (UX)

### User Stories
- **User Story, Hiker:**  As a hiker I want to search for walking trails by location, difficulty, and distance,
so that I can find a route that suits my preferences and fitness level. 
 
-  **Acceptance Criteria:** 
    - Search function for location, walk difficulty and distance.
    - Routes included that are suitable for proper hikers, not just short walks.

- **User Story, Casual walker:** As a casual walker, I want to see a list of easy walks,
so that I can enjoy a relaxing experience with my family.
 
-  **Acceptance Criteria:** - 
    - Have categories of walks to search such as 'easy'.
    - Include shorter routes
    - Add other information e.g. nearby cafe, toilets, etc for family day out.
  
- **User Story, Tourist:**  As a tourist, I want to find scenic and coastal walks in Cornwall,
so that I can enjoy the views and unique landmarks.

-  **Acceptance Criteria:** 
    - Have categories such as Coastal so walkers can choose the type of walk they want
    - Have an image of some of the views from the walk so walkers can choose based on scenery if they want
    - Include other information about the local area that tourists might not know 

  - **User Story, Admin can add, edit and delete:** As an admin, I want to add, edit, and delete walks from the database, so that I can manage the content of the site.
 
-  **Acceptance Criteria:** - 
    - Admins should be able to create new walk entries.
    - Admins must be able to edit walk information.
    - Admins must have the facility to delete walks and their associated data.


- **User Story, Saving walks:**  As a returning user, I want to save my favourite walks,
so that I can revisit them later. 
 
-  **Acceptance Criteria:** 
    - User can login to their account
    - User can save walks so can quickly find the walks they have done
  
- **User Story, Mapping and navigation:**  As a user, I want to view detailed maps of walking trails,
so that I can navigate the routes easily.

-  **Acceptance Criteria:** 
    - Include maps of the route
    - Written directions/ descriptions of the route also

- **User Story, Reviews and ratings:**  As a user, I want to leave reviews and ratings for walking routes,
so that I can help others decide which trails to explore.

-  **Acceptance Criteria:** 
    - Users can leave reviews and ratings
    - Users can also edit their reviews or delete them if they want

- **User Story, List of walks:**  As a user I can access a list of walks so that I can find out the details about them; distance, difficulty, route description, start and end points.
 
-  **Acceptance Criteria:** 
    - Show list of walks with details about them
    - Clearly mark distance and difficulty
    - Have description of route including start and end points

- **User Story, Login:**  As a user I can log in to an account. Logging in ensures users are authenticated, providing a layer of security and moderation for shared content.
 
-  **Acceptance Criteria:** 
    - Have user accounts, and admin approved posts.

- **User Story, Weather information:**  As a walker, I want to see weather forecasts for the area of my chosen trail,
so that I can prepare accordingly.
 
-  **Acceptance Criteria:** 
    - Show relevant weather information for each route

- **User Story, Categories of walks:**  As a walker I can search for certain types of walks so that I can choose the type of experience I have.
 
-  **Acceptance Criteria:** 
    - Have categories for walks; coastal, woodland, historical, 
    

(Include all prioritized must-have features)  
**Guidance:** Draft the user stories during Phase 1: Ideation & Initial Setup and update them as you complete Phase 2: Must User Stories Implementation & Testing. Document each must-have feature here along with its acceptance criteria.

### Should-Have User Stories
- **User Story 1:** Briefly describe the should-have feature.  
  **Acceptance Criteria:** List the criteria that define the successful implementation of this user story.
- **User Story 2:** Briefly describe the should-have feature.  
  **Acceptance Criteria:** List the criteria that define the successful implementation of this user story.

(Include all prioritized should-have features)  
**Guidance:** Document the secondary features that you aim to implement in Phase 3: Should User Stories Implementation & Any Advanced Features. Include clear acceptance criteria for each.

### Could-Have User Stories
- **User Story, Blog:** As a Site Admin I can create or update a blog so that I can offer users updates or tips.
 
  **Acceptance Criteria:** 
  - Create a blog feature
  - the site admin can update and add posts

  **Acceptance Criteria:** List the criteria that define the successful implementation of this user story.
- **User Story 2:** Briefly describe the could-have feature.  
  **Acceptance Criteria:** List the criteria that define the successful implementation of this user story.

(Include any could-have features considered for future enhancements)  
**Guidance:** Document any optional features that are nice to have but not essential.

## Accessibility Considerations

Discuss how accessibility guidelines were adhered to, including colour contrast and alt text for images.  
**Guidance:** Outline how you've incorporated accessibility into your design, ensuring that your project adheres to guidelines such as WCAG.

## Design Decisions

### Colour scheme

Text - Slate Grey (#4b4b4b)

Background - Light Cream (f9f6f1)

Google fonts: Montserrat for Titles, Inter for walk descriptions and user reviews.

### Typography
### Imagery
### Wireframes
Include wireframes for key sections of your website.  
Briefly describe the design choices, including layout, colour schemes, and fonts.  
**Guidance:** Start this section during Phase 1: Ideation & Initial Setup and update it throughout Phase 2 and Phase 3. Include digital wireframes created in Phase 1. Document the reasoning behind your layout choices, colour schemes, and font selections.


### Existing Features
### Future Features

## User Flow diagrams

## User Flow Steps

### Entry Point

Users open the app and land on the homepage.

### Key Goals for Users
  - Discover walks (search or browse)
  - View walk details (distance, difficulty, location, etc)
  - Save favourite walks or plan their trip
  - Access GPS-enabled maps for navigation
  - Log in for personalized features (e.g. saved completed walks, making comments)
  - Review or share their experience of a walk

## User flow Outline

1. Start: Homepage

  - Options for:
      -  Search Walks (keyword, location, distance, difficulty, etc.).
      -  Browse Walks (featured, by category, nearby).
      -  Login/Sign Up for personalized features.
      -  About Section (app info, contact, etc.).

2. Search/Browse Walks

  -  Input search criteria or browse categories:
      -  Category (e.g., coastal walks, dog-friendly walks).
      -  Distance (short, medium, long).
      -  Difficulty (easy, moderate, challenging).

  -  View results (list/grid format with thumbnail, title, distance, etc.).
  -  Select a walk from the list to see detailed information.

3. Walk Details Page

  -  Details include:
      -  Title, description, distance, duration, difficulty.
      -  Interactive map (with GPS support).
      -  Reviews and ratings.
      -  Related walks or nearby attractions.
  -  User options:
      -  Save to favorites (requires login).
      -  Start navigation (open map/GPS).

4. Navigation/GPS View

  -  Display an interactive map with the selected walk's route.
  -  Include features like:
      -  Turn-by-turn instructions.
      -  Offline GPX download option.
      -  Nearby points of interest.

5. User Features

  -  Logged-in users can:
      -  Save favorite walks.
      -  Track completed walks.
      -  Add reviews/ratings for walks they've completed.
  -  Reviews/Community:
      -  Post comments or share tips/photos for a walk.

6. Post-Walk Options

  -  Review and rate the walk.
  -  Share the walk on social media.
  -  Plan the next walk.

7. Exit

  -  Users log out or close the app.

## Data Models

### Walk Model
### Category Model
### Review Model
### User Profile Model

### Relationships: 

## Entity Relationship Diagram

## Features Implementation

### Core Features (Must-Haves)
- **Feature 1:** Description of the implemented feature.
- **Feature 2:** Description of the implemented feature.

(Include all must-have features)  
**Guidance:** Use this section as you complete Phase 2: Must User Stories Implementation & Testing. Document all the must-have features you implemented, explaining how they align with the user stories and acceptance criteria.

### Advanced Features (Should-Haves)
- **Feature 1:** Description of the implemented feature.
- **Feature 2:** Description of the implemented feature.

(Include all should-have features)  
**Guidance:** Include any advanced features you implemented during Phase 3: Should User Stories Implementation & Any Advanced Features. Explain how these features enhance user experience and their alignment with the acceptance criteria.

### Optional Features (Could-Haves)
- **Feature 1:** Description of the implemented feature (if any).
- **Feature 2:** Description of the implemented feature (if any).

(Include any could-have features that were implemented or considered)  
**Guidance:** If any could-have features were implemented, describe them here. This is an opportunity to showcase extra work done beyond the initial scope. But remember - keep it simple! Focus on the Must stories first. Could user story features are commonly earmarked for future project iterations.


## Technologies Used

## Agile Methodology

## Deployment

### PostgreSQL Database
### Cloudinary API
### Heroku Deployemnt
### Local Deployment

## Testing and Validation
**Guidance:** Summarize the results of your testing across various devices using tools like Chrome DevTools, as outlined in Phase 2. Mention any issues found and how they were resolved.
**Guidance:** Document your use of W3C and Jigsaw validators to ensure your HTML and CSS meet web standards. Include any errors or warnings encountered and how they were resolved.
### Validation of HTML, CSS, JS and Python Code
### Manual Testing
### Responsive Design
### Cross-browser Compatibility Testing

## Reflection on Development Process

### Successes


### Challenges


### Final Thoughts


## Code Attribution
Properly attribute any external code sources used in the project (excluding GitHub Copilot-generated code).  
**Guidance:** Document any external code sources used throughout the entire project

## Future Improvements
Briefly discuss potential future improvements or features that could be added to the project.  
**Guidance:** Reflect on potential enhancements that could be made to the project after Phase 4: Final Testing, Debugging & Deployment. These could be Could user story features you didn’t have time to implement or improvements based on testing feedback.