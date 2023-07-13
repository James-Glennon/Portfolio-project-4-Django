# Portfolio Project 4: Full-stack Frameworks: Django

by _James Glennon_

## About / Design

A business to consumer site for a small dublin restaurant.

The objective to provide information about the physical shop, and provide the opportunity to view and make reservations online.

_No payment options will be availible in the final product_

### CSS

A start bootstrap template was used to generate base html, css and js.

A coffee shop template was used due to meeting similiar demands.

_A B2C site, providing service(preparing food), but not accepting payment in advance_

### Data model design

Created using [Google Sheets](https://docs.google.com/spreadsheets/d/1SQwIpyVCUgvEL38z1gGeFQetknSybqHcXUJ7Namfhy4/edit?usp=sharing)

The basic premise of the data is that all available bookings are stored in the **tables** model.

These bookings must be generated in the table before a booking request can be made for these times.

a registered **user** submits a booking request into the **bookings** model.

The user may only choose from the bookings in **tables** that are currently set to _Availability = True_

The request is approved by a staff/admin, which changes the entry in **tables** matching the **bookings** date and time to _Availabilty = False_

The booking request is tied to a **User ID**, which has a matching _email_, allowing the staff to contact the user and confirm that the booking has been accepted.

## Features

**Project is incomplete**

## Development

Development was carried out using Django frameworks.

Progess was recorded using [GitHubBoards](https://github.com/users/James-Glennon/projects/4/views/1) Thou

### Resolved Issues

### Known Bugs / Unresolved Issues

I cannot seem to link my template to my css files present in my static files using the { static 'css/base.css'}. I don't know why.

When trying to visualise the model data as a query set in the front end as shown in the lessons, my Guest model seems not to have a .objects property. I don't know why.

### Testing

**Project is incomplete**

#### Validation and Lighthouse

**Project is incomplete**

## Deployment

Version control was enabled with [GitHub](https://github.com/James-Glennon/Portfolio-project-4-Django).

The project was remotely posted to [Heroku](https://dashboard.heroku.com/apps/portfolio4-django) using the Heroku CLI.

Static files, such as css and js required for the Start Bootstrap are to be hosted at cloudinary, however
the **Project is incomplete**

## Room for Improvement / Expansion

**The Ability to Pay** using something like [Stripe](https://stripe.com/en-ie/payments) for expanded services, like delivery or a small booking fee.

**Automation**: 
The current model design requires a staff member to manually accept booking requests and to email manually to confirm.

Accepting requests could be handled automatically in the back end (*in theory*) and email confirmation could be handled with [Zapier](https://zapier.com/).

## Credits

### Media

[Start Bootstrap](https://startbootstrap.com/theme/business-casual)

**Business Casual** bootstrap compatible template and images.

### Code

[Cloud With Django](https://www.youtube.com/watch?v=HQ1kfJpWdRI)

**Deploy static files to Cloudinary from a Django app**

A video I consulted to try get a better grasp on using cloudinary
