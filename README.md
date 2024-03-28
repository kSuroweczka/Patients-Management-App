# Patients-Management-App
The Patients application is a simple tool for managing a patient database. It allows users to add, view, update, and delete patient records. Additionally, it enables searching for patients based on various criteria.

## Features
### Adding Patients
Users can add new patient records by providing the patient's first name, last name, PESEL (Personal Identification Number), address (street, city, zip code), and a URL for the patient's photo.

### Viewing Patients
The application displays a list of patients with the ability to view their details, including first name, last name, PESEL, address, and photo.

### Updating Patients
Users can edit existing patient records by modifying their personal or address details, as well as the URL of their photo.

### Deleting Patients
The application allows for the removal of unnecessary patient records from the database.

### Searching Patients
Users can search for patients based on various criteria, such as first name, last name, city, or even the full name. Additionally, they can specify the sorting order (ascending or descending) for the search results.


## Technologies Used
The Patients application is built using the following technologies:

    Python: Flask framework for the backend logic and SQLite for database management.
    HTML/CSS: Frontend user interface design.
    Jinja2: Template engine for integrating Python logic into HTML templates.

## Getting Started

To run the Patients application locally, follow these steps:

    Clone the repository to your local machine.
    make sure you have Python, Flask installed
    Run the application using `python app.py`.
    Access the application in your web browser at http://localhost:5000.

## Usage

Once the application is running, you can perform the following actions:

    Add new patients by filling out the provided form.
    View the list of patients and their details.
    Update existing patient records by clicking on the "Update" button next to each patient.
    Delete patient records by clicking on the "Delete" button next to each patient.
    Search for patients using the search bar, specifying sorting criteria and order if needed.
