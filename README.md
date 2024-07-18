# Tech Tackles- IT Support Ticketing System with Knowledge Base

# Table of Contents


## Project Overview

Welcome to Tech Tackles, your go-to IT Support Ticketing System designed to streamline and simplify your IT support processes. Our system is built to help organizations efficiently manage and resolve IT-related issues.

Our IT Support Ticketing System is crafted to provide a user-friendly platform for logging, tracking, and resolving IT support requests. Whether you're an IT professional seeking a reliable solution for ticket management or an end-user needing swift assistance, Tech Tackles is here to support you.

With an intuitive web interface, users can easily submit tickets, track progress, and communicate with IT specialists.

The project will include front-end development with HTML, CSS, and JavaScript, and back-end development using Python and Django

### Screenshots




### [Link to Live project](https://pp4-techtackles-by-hc-ed362e72006b.herokuapp.com/tickets/)

### Objective

## UX/UI
### The Strategy Plane

VISION
To create a user-friendly applicatopm that is designed to streamline and simplify and enhances the efficiency of IT support processes, improves user satisfaction, and reduces resolution times.

OBJECTIVES
- Streamline the process of ticket submission and management.
- Enhance collaboration among IT support staff for faster problem resolution.
- Enable administrators to manage the system efficiently with advanced tools and reporting capabilities.

USER NEEDS
- End-Users (Employees/Customers)
    - Easy Ticket Submission: Simple and quick process to submit support tickets.
    - Self-Service Solutions: Access to a comprehensive knowledge base for common issues and FAQs.
    - Feedback Mechanism: Ability to provide feedback on the support received.
      
- IT Support Staff
    - Efficient Ticket Management: Tools to prioritize and manage tickets effectively.
    - Access to Information: Quick access to Knowledge base and relevant information for troubleshooting.

- Administrators
    - User Management: Tools to manage users and roles effectively.
    - Ticket Management: Ability to update, assign and delete tickets


### The Scope Plane 
FUNCTIONS
- End User
  - Ticket Submission:
    - Simple form for submitting support tickets.
    - Fields: Issue Description, Category, Urgency, Attachments.
    - Auto-suggestions from the knowledge base while typing.

  - Knowledge Base Access:
    - Search functionality for finding articles.
    - Categories and tags for easy navigation.
    - Article ratings and feedback options.

  - Ticket Status Updates:
    - Dashboard showing submitted tickets and their statuses.
    - Real-time notifications for updates and resolutions.

- IT Support Staff
 - Ticket Management:
    - Dashboard with all tickets sorted by status (new, in-progress, resolved).
    - Filters for priority, category, date, and assigned staff.
  
  - Prioritization and Assignment:
    - Ability to prioritize tickets based on urgency and impact.
    - Assign tickets to specific team members.

- Internal Collaboration:
    - Internal notes and comments section within each ticket.
    - Notifications for ticket updates and collaboration messages.

- Knowledge Base Contributions:
    - Tools to create, edit, and categorize knowledge base articles.
    - Option to mark tickets as candidates for new knowledge base articles.

- Administrator
  - User Management:
    - Add, remove, and manage user roles and permissions.
    - Configure different access levels for end-users, support staff, and administrators.

  - System Configuration:
    - Customize ticket form templates.
    - Configure email notifications and templates.

CONTENTS
- Knowledge Base
  - Initial Articles
      - Common issues and resolutions
      - FAQ troubleshooting guides
  - Ongoing Contribution
    - Regular updates and additions based on new issues and solutions.
    - User feedback integration for improving existing articles.

- Documentation
  - End User Guides
     - How to search the knowledge base.
     - How to submit a ticket.
     - Understanding ticket status update
  - IT Support Staff Manuals
    - How to manage and prioritize tickets.
    - Using the internal collaboration tools.
    - Contributing to the knowledge base.
  - Administrator Manuals
    - Managing user roles and permissions.
    - System configuration and customization.


### The Structure Plane - defines the layout and navigation of your product, as well as the interaction patterns and feedback mechanisms that enable users to achieve their goals. how will your product work and how will users move through it?
- User Story/Acceptance Criteria
- User Story/Acceptance Criteria
- User Story/Acceptance Criteria
- User Story/Acceptance Criteria
- User Story/Acceptance Criteria
- EPICS

### The Skeleton Plane - defines the visual hierarchy and aesthetics of your product, as well as the typography, color, imagery, and icons that convey meaning and emotion. how will your product look and feel and how will users perceive it?
- Wireframe 
-	Flowchart/Database Schema - https://drawsql.app/ Entity Relationship Diagram

### The Surface Plane - the actual interface that users see and interact with
- Colour Scheme
-	Fonts Used
-	Images
- Features – Actual website
  - Function 1
  - Function 2
  - Function 3
## Future Feature Considerations
## Testing
  - User Story Testing
  - Automated testing
  - CI Python Linter – 
  - Lighthouse
  - Mobile
  - Desktop
  - W3C CSS Validator
  - W3C HTML validator
  - JSHint for Javascript
  - Other Testing
    - Functionality Testing
    - Compatibility Testing – different devices
    - Crossbrowser testing
## Agile Development

To ensure the TECH TACKLES IT Support Ticketing System is developed effectively and efficiently, we will follow an agile approach. This will involve iterative development cycles (sprints) where we continuously build, test, and refine the system. Here's how we can break down the development process into iterations:

#### Iteration 0: Planning and Setup
- Goals:

Define project objectives, user stories, and initial requirements.
Set up the development environment.
Create initial project structure and repository.
T
- Tasks:

Create and initialize a Git repository.
Set up Django project and application.
Configure Django AllAuth for user authentication.
Create initial models for User, Ticket, and Comment.
Set up static files and templates structure.

#### Iteration 1: User Authentication and Role Management

- Goals:

  Implement user authentication.
  Define and implement user roles (Admin, User, Tech Support).
- Tasks:

  Implement login, signup, and logout functionality using Django AllAuth.
  Create user roles and permissions.
  Implement user management in the admin dashboard.
  Test user authentication and role management.
- Deliverables:

  Functional user authentication system.
  User roles and permissions implemented.
  Basic admin interface for user management.

#### Iteration 2: Ticket Management
- Goals:

  Implement ticket creation, viewing, and listing.
- Tasks:

  Create forms for ticket creation and updating.
  Implement views for creating, listing, and viewing tickets.
  Implement ticket status (Open, In Progress, Closed).
  Test ticket creation and viewing functionalities.
- Deliverables:

  Functional ticket creation form.
  List view of tickets with status filters.
  Detail view for individual tickets.

#### Iteration 3: Commenting and Interaction
- Goals:

  Implement ticket commenting system.
  Ensure interaction between users and tech support through comments.
- Tasks:

  Create comment model and forms.
  Implement views for adding and viewing comments.
  Restrict comment access based on user roles.
  Test commenting functionality.
- Deliverables:

  Functional commenting system.
  Users can add comments to their own tickets.
  Tech support can add comments to all tickets.
#### Iteration 4: Admin and Tech Support Features
- Goals:

  Implement additional features for admin and tech support users.
- Tasks:

  Allow tech support to edit and delete tickets.
  Enable admin to assign tickets to tech support.
  Implement admin dashboard for ticket management.
  Test admin and tech support features.
- Deliverables:

  Admin and tech support can manage tickets.
  Admin dashboard for user and ticket management.
#### Iteration 5: Notification System and UX Improvements
- Goals:

  Implement a notification system for success and error messages.
  Improve the user interface and experience.
- Tasks:

  Integrate Django messages framework for notifications.
  Create custom JavaScript for popup messages.
  Improve CSS for better layout and design.
  Test the notification system and UI.
- Deliverables:

  Functional notification system for user actions.
  Improved UI with responsive design.
#### Iteration 6: Testing and Bug Fixing
- Goals:

  Ensure the system is fully functional and bug-free.
- Tasks:

  Perform comprehensive testing of all features.
  Fix any bugs or issues found during testing.
  Ensure all user stories are met.
- Deliverables:

  Fully tested and functional IT support ticketing system.
  Documentation for testing procedures and results.
#### Iteration 7: Deployment and Documentation
- Goals:

  Deploy the application to a production environment.
  Create comprehensive documentation.
- Tasks:

  Set up and configure the production environment.
  Deploy the application.
  Write detailed documentation for installation, usage, and contribution.
  Create a README file with all necessary information.
- Deliverables:

  
  Deployed application.
  Comprehensive documentation and README.
#### Iteration 8: Feedback and Iteration
- Goals:

  Gather feedback from users and stakeholders.
  Implement improvements based on feedback.
- Tasks:

  Collect feedback through surveys or user testing sessions.
  Prioritize and implement changes based on feedback.
  Plan for future iterations or updates.
- Deliverables:

  Feedback report.
  Updated application with improvements based on feedback.
#### Continuous Improvement
Even after the initial development and deployment, continuous improvement is key. Regularly gather feedback, monitor the application's performance, and plan for future updates and new features to ensure TECH TACKLES continues to meet user needs effectively.

By following this agile approach with clear iterations, we ensure that the development of the TECH TACKLES IT Support Ticketing System is structured, efficient, and responsive to user needs.
## Bugs and Potential issues

## Technologies and language
## Development
## Deployment on Heroku
## Credits
## Acknowledgement
