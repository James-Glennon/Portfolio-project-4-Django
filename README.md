# Portfolio Project 4: Full-stack Frameworks: Django

by *James Glennon*

## About / Design

### CSS

A start bootstrap template was used to generate base html, css and js.

### Data model design

Created using [Google Sheets](https://docs.google.com/spreadsheets/d/1SQwIpyVCUgvEL38z1gGeFQetknSybqHcXUJ7Namfhy4/edit?usp=sharing)

The basic premise of the data is that all available bookings are stored in the **tables** model.

These bookings must be generated in the table before a booking request can be made for these times.

a registered **user** submits a booking request into the **bookings** model.

The user may only choose from the bookings in **tables** that are currently set to *Availability = True*

The request is approved by a staff/admin, which changes the entry in **tables** matching the **bookings** date and time to *Availabilty = False*

The booking request is tied to a **User ID**, which has a matching *email*, allowing the staff to contact the user and confirm that the booking has been accepted.

## Features

## Development

### Resolved Issues

### Known Bugs / Unresolved Issues

### Testing

#### Validation and Lighthouse

## Deployment

## Room for Improvement / Expansion

## Credits

### Media

### Code

[Start Bootstrap](https://startbootstrap.com/theme/business-casual)

**Business Casual** bootstrap compatible template and images.
