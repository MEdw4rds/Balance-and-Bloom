## Project 


# Table of Contents
1. <a href="#Lets Renovate - Home Decorating Blog">Introduction</a>
2. <a href="#overview">Overview</a>
3. <a href="#ux---user-experience">UX - User Experience</a>
4. <a href="#features">Features</a>
- <a href="#key-project-goals">Key project goals</a>
- <a href="#target-audience">Target Audience</a>
- <a href="#agile-methodologies">Agile Methodologies</a>
- <a href="#moscow-prioritization">MoSCoW Prioritization</a>
- <a href="#sprints">Sprints</a>
- <a href="#wireframes">Wireframes</a>
- <a href="#database-schema---entity-relationship-diagram">Database Schema - Entity Relationship Diagram</a>
5. <a href="#features">Features</a>
- <a href="#navigation-bar">Navigation bar</a>
- <a href="#home-page">Home Page</a>
- <a href="#Contact-page">contact Page</a>
- <a href="#about-page">About page</a>
- <a href="#bookings">Bookings</a>
- <a href="#food">Food</a>
- <a href="#crud-functionality-alerts">CRUD Functionality Alerts</a>
- <a href="#future-features">Future Features</a>
- <a href="#footer">Footer</a>
6. <a href="#technologies-&-languages-Used">Technologies & Languages Used</a>
7. <a href="#lets-renovate---home-decorating-blog">Libraries & Frameworks</a>
8. <a href="#bugs">Bugs</a>
9. <a href="#deployment">Deployment</a>
10. <a href="#credits">Credits</a>
11. <a href="#acknowledgements">Acknowledgements</a>

## Overview

# UX - User Experience

### Key project goals

### Target Audience

### Agile Methodologies

### MoSCoW Prioritization

### Sprints

- Sprint 1: Initial Setup - Project, repository, environment setup, Task destribution.
- Sprint 2: User Authentication, post & comment model, therapists_profile.
- Sprint 3: Design search & Appointment Booking System.
- Sprint 4: Static Pages & UI/UX Improvements.
- Sprint 5: Deployment & Testing

### User stories

### Typography

### Colour Scheme

## Wireframes

- ### Home Page Wireframes

- #### About Page:

- #### Food Page:

- Mobile View

![Logo](food/static/images/mob1.png)

- Desktop View

![Logo](food/static/images/desk1.png)

- #### Contact Page:

- #### Booking Page:

- Mobile View

![Logo](therapist_booking/static/images/wireframeloginmobile.png)

- Desktop View

![Logo](therapist_booking/static/images/wireframe_booking.png)


![Logo](therapist_booking/static/images/wireframeuserbookings.png)

- #### Profile Page:

### Database Schema - Entity Relationship Diagram

The ERD shown below illustrates the relationships between the users, therapists appointments, acontact page,food posts comments and ratings, and more. This is essential to demonstrate the relationships between the different models in the PostgreSQL database.

![Logo](food/static/images/erd.png)

# Features

- ### Navigation bar
A responsive navigation bar is in place. Concentrating on 'mobile first' design, the navigation bar incorporates a clickable burger icon with a drop down menu on mobile. There is a burger icon at tablet size too, but when moving to monitor size the burger disappears and a navigation bar appears with options to navigate to pages. See mobile and monitor screenshots below.

- ### Mobile Navb-bar with toggler

![Logo](food/static/images/navbarmob.png)

- ### Desktop Navbar

![Logo](food/static/images/navbar.png)

- ### About

- ### Contact

- ### Bookings

- ### Profiles

- ### Food Categories

- Recipies page

- CRUD Functionality of Comment and Rating Model

1. Create 
Users are automatically assigned a profile upon registration. They can create bookings and post comments.

2. Read
Users can view recipies and associated information, including Booking comments.

3. Update
Users have the ability to update their ratings and comments.

4. Delete
Users can delete comments at any time.

- ### Signup/signin Form

- ### Django Alert Messages

- ### Future Features

- ### Footer

# Technologies & Languages Used

- HTML5 - Markup language for structuring the website
- CSS3 - Styling language for designing the layout and visual aesthetics
- JavaScript - For interactivity and DOM manipulation on the frontend
- Python (Django) - Backend web framework for server-side logic and management
- PostgreSQL - Database management system for storing data
- Cloudinary - Cloud-based image storage solution
- Whitenoise - For serving static files directly from Django

# Libraries & Frameworks

- Django - Backend framework
- Django Crispy Forms - For elegant form rendering
- Cloudinary - Media storage
- Whitenoise - For serving static files

# Tools & Programs

- GitHub Projects - Project management and tracking
- Heroku - Deployment and hosting
- Balsamiq - Wireframes and design prototypes

# Testing

## Validation Testing

- ### HTML: W3C Markup Validator.

Every template in Apps was checked. Code was check through HTMl validator. Results for different page source are as followed:

- ### CSS: W3C CSS Validator.

- ### Python: PEP8 validation to ensure code quality.

# Bugs

# Deployment
All code for this project was written in Visual Studio/Gitpod as the integrated development environment. GitHub was used for version control, and the application was deployed to Heroku from GitHub.

## Creating Repository on GitHub

- First make sure you are signed into Github and go to the code institutes template, which can be found here.
- Then click on use this template and select Create a new repository from the drop-down. Enter the name for the repository and click Create repository from template.
- Once the repository was created, I clicked the green gitpod button to create a workspace in gitpod so that I could write the code for the site.

## Creating an app on Heroku

- After creating the repository on GitHub, head over to heroku and sign in.
- On the home page, click New and Create new app from the drop down.
- Give the app a name(this must be unique) and select a region I chose Europe as I am in Europe, Then click Create app

## Pre-Deployment

To ensure a successful deployment to Heroku, the following practices are to be followed (Experience from previous Django projects):

- Requirements File:  The requirements.txt file must be kept up to date to ensure all imported Python modules are configured correctly for Heroku.
- Procfile:  A Procfile was added to configure the application as a Gunicorn web app on Heroku.
- Allowed Hosts:  In settings.py, the ALLOWED_HOSTS list was configured to include the Heroku app name and localhost. Example format:

ALLOWED_HOSTS = ['your-app-name.herokuapp.com', 'localhost']

- Environment Variables:  All sensitive data such as the DATABASE_URL, CLOUDINARY_URL, and SECRET_KEY were added to the .env file, which is ignored by Git using .gitignore. These variables are added to Heroku manually through the Config Vars section.

## Deploying with Heroku

The steps for deploying to Heroku are as follows (Experience from previous Django projects):

1. Create New App: Log in to your Heroku account and click on the "Create New App" button.
2. App Name: Choose a unique name for your app.
3. Select Region: Choose the appropriate region (Europe was selected for this project).
4. Create App: Click the "Create App" button to proceed.
5. Deployment Method: In the "Deploy" tab, select GitHub as the deployment method.
6. Connect to GitHub: Search for the repository name and click "Connect".
7. Manual or Automatic Deployment: Select either manual or automatic deployment. Ensure the main branch is selected for deployment.
8. Config Vars: In the "Settings" tab, click "Reveal Config Vars" and input the required environment variables.
9. Buildpack: Select Node.js and Python as the buildpacks for your project.
10. Deploy: Once the configuration is complete, click the "Deploy Branch" button. After successful deployment, a "View" button will appear to take you to the live site.

# Credits

# Acknowledgements