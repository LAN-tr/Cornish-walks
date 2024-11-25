# Cornish Walks
## Overview

### Purpose

A Cornish walks app would aim to solve several problems faced by residents, tourists, and outdoor enthusiasts in Cornwall. The key challenges the app would seek to address are:

- Difficulty finding suitable walking trails: The app will provide a searchable database of trails with filters for distance, difficulty level, terrain and scenic features.

- Lack of reliable maps and navigation tools: The app can include GPS-enabled maps for real-time navigation meaning that users do not need to rely on outdated or vague descriptions or drawings.

- Challenges with weather and tides: The app could integrate weather updates and forecasts for specific areas and tide times for beaches and coastal walks.

- Accessibility and inclusivity issues: The app could highlight accessible trails and could indicate suitability for various needs and details about elevation, terrain and rest points.

- Limited community and sharing features: Walkers can share their experiences and review the walks with a space for comments and a way to save walks that they enjoyed, or would like to try next.

This project's purpose is to make exploring Cornwall easier, safer and more enjoyable. It would cater to a diverse range of users; casual walkers, serious hikers, tourists and locals by offering practical tools, curated recommendations and engaging features.


## User Stories

### Must-Have User Stories
- **User Story 1:**  As a hiker I want to search for walking trails by location, difficulty, and distance,
so that I can find a route that suits my preferences and fitness level. 
 
  **Acceptance Criteria:** 
  - Search function for location, walk difficulty and distance.
  - Routes included that are suitable for proper hikers, not just short walks.

- **User Story 2:** As a casual walker, I want to see a list of easy walks,
so that I can enjoy a relaxing experience with my family.
 
  **Acceptance Criteria:** - 
  - Have categories of walks to search such as 'easy'.
  - Include shorter routes
  - Add other information e.g. nearby cafe, toilets, etc for family day out.

- **User Story 3:**  As a tourist, I want to find scenic and coastal walks in Cornwall,
so that I can enjoy the views and unique landmarks.

  **Acceptance Criteria:** 
  - Have categories such as Coastal so walkers can choose the type of walk they want
  - Have an image of some of the views from the walk so walkers can choose based on scenery if they want
  - Include other information about the local area that tourists might not know 

- **User Story 4:**  As a returning user, I want to save my favourite walks,
so that I can revisit them later. 
 
  **Acceptance Criteria:** 
  - User can login to their account
  - User can save walks so can quickly find the walks they have done
  
- **User Story 5:**  As a user, I want to view detailed maps of walking trails,
so that I can navigate the routes easily.

  **Acceptance Criteria:** 
  - Include maps of the route
  - Written directions/ descriptions of the route also

- **User Story 6:**  As a user, I want to leave reviews and ratings for walking routes,
so that I can help others decide which trails to explore.

  **Acceptance Criteria:** 
  - Users can leave reviews and ratings
  - Users can also edit their reviews or delete them if they want

- **User Story 7:**  As a user I can access a list of walks so that I can find out the details about them; distance, difficulty, route description, start and end points.
 
  **Acceptance Criteria:** 
  - Show list of walks with details about them
  - Clearly mark distance and difficulty
  - Have description of route including start and end points

- **User Story 8:**  As a user I can log in to an account. Logging in ensures users are authenticated, providing a layer of security and moderation for shared content.
 
  **Acceptance Criteria:** 
  - Have user accounts, and admin approved posts.

- **User Story 9:**  As a walker, I want to see weather forecasts for the area of my chosen trail,
so that I can prepare accordingly.
 
  **Acceptance Criteria:** 
  - Show relevant weather information for each route

- **User Story 10:**  As a walker I can search for certain types of walks so that I can choose the type of experience I have.
 
  **Acceptance Criteria:** 
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
- **User Story 1:** - **User Story 11:**  As a Site Admin I can create or update a blog so that I can offer users updates or tips.
 
  **Acceptance Criteria:** 
  - Create a blog feature
  - the site admin can update and add posts

  **Acceptance Criteria:** List the criteria that define the successful implementation of this user story.
- **User Story 2:** Briefly describe the could-have feature.  
  **Acceptance Criteria:** List the criteria that define the successful implementation of this user story.

(Include any could-have features considered for future enhancements)  
**Guidance:** Document any optional features that are nice to have but not essential.

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

## Design Decisions

### Wireframes
Include wireframes for key sections of your website.  
Briefly describe the design choices, including layout, colour schemes, and fonts.  
**Guidance:** Start this section during Phase 1: Ideation & Initial Setup and update it throughout Phase 2 and Phase 3. Include digital wireframes created in Phase 1. Document the reasoning behind your layout choices, colour schemes, and font selections.

### Accessibility Considerations
Discuss how accessibility guidelines were adhered to, including colour contrast and alt text for images.  
**Guidance:** Outline how you've incorporated accessibility into your design, ensuring that your project adheres to guidelines such as WCAG.

## AI Tools Usage

### DALL-E
Describe how DALL-E was used for image generation, including examples of successes and challenges.  
**Guidance:** Specifically mention how you used DALL-E for image generation and the impact this had on your design process.

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

## AI Tools Usage

### GitHub Copilot
Describe how GitHub Copilot assisted in coding, including any challenges or adjustments needed.  
**Guidance:** Reflect on how GitHub Copilot assisted in coding, particularly any challenges or adjustments that were needed to align with project goals.

## Testing and Validation

### Testing Results
Summarize the results of testing across different devices and screen sizes.  
Mention any issues found and how they were resolved.  
**Guidance:** Summarize the results of your testing across various devices using tools like Chrome DevTools, as outlined in Phase 2. Mention any issues found and how they were resolved.

### Validation
Discuss the validation process for HTML and CSS using W3C and Jigsaw validators.  
Include the results of the validation process.  
**Guidance:** Document your use of W3C and Jigsaw validators to ensure your HTML and CSS meet web standards. Include any errors or warnings encountered and how they were resolved.

## AI Tools Usage

### GitHub Copilot
Brief reflection on the effectiveness of using AI tools for debugging and validation.  
**Guidance:** Reflect on how GitHub Copilot assisted with debugging and validation, particularly any issues it helped resolve.

## Deployment

### Deployment Process
Briefly describe the deployment process to GitHub Pages or another cloud platform.  
Mention any specific challenges encountered during deployment.  
**Guidance:** Describe the steps you took to deploy your website during Phase 4: Final Testing, Debugging & Deployment, including any challenges encountered.

## AI Tools Usage

### Reflection
Describe the role AI tools played in the deployment process, including any benefits or challenges.  
**Guidance:** Reflect on how AI tools assisted with the deployment process, particularly how they streamlined any tasks or presented challenges.

## Reflection on Development Process

### Successes
Effective use of AI tools, including GitHub Copilot and DALL-E, and how they contributed to the development process.

### Challenges
Describe any challenges faced when integrating AI-generated content and how they were addressed.

### Final Thoughts
Provide any additional insights gained during the project and thoughts on the overall process.  
**Guidance:** Begin drafting reflections during Phase 1 and update throughout the project. Finalize this section after Phase 4. Highlight successes and challenges, particularly regarding the use of AI tools, and provide overall insights into the project.

## Code Attribution
Properly attribute any external code sources used in the project (excluding GitHub Copilot-generated code).  
**Guidance:** Document any external code sources used throughout the entire project, especially during Phase 2 and Phase 3. Exclude GitHub Copilot-generated code from attribution.

## Future Improvements
Briefly discuss potential future improvements or features that could be added to the project.  
**Guidance:** Reflect on potential enhancements that could be made to the project after Phase 4: Final Testing, Debugging & Deployment. These could be Could user story features you didn’t have time to implement or improvements based on testing feedback.