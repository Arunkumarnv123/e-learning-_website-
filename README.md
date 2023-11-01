E-learning Website


Overview
This project is a simple e-learning platform built with Flask. It allows users to register for an account, log in, and view a list of available courses. Teachers can also add, update, and delete courses.

Features
User registration and login with OTP verification
Adding, updating, and deleting courses
Role-based access control (RBAC), with two roles: student and teacher
How to use
To use the application, follow these steps:

Clone the repository to your local machine.
Install the required dependencies: flask, flask-sqlalchemy, flask-mail, and bcrypt.
Create a database file called stutech.db.
Start the application by running the following command: flask run.
Accessing the application
The application will be running on http://localhost:5000 by default. You can access it using a web browser.

Creating an account
To create an account, go to the register page and enter your name, email address, phone number, address, password, and role. You will then receive an OTP to your email address. Enter the OTP on the validation page to complete your registration.

Logging in
To log in, go to the login page and enter your email address and password. If your login is successful, you will be redirected to the main page.

Viewing courses
To view the list of available courses, go to the main page. If you are a teacher, you can also add, update, and delete courses from this page.

Adding a course
To add a course, go to the add course page and enter the course name, instructor name, and course content. Click on the "Add Course" button to create the course.

Updating a course
To update a course, go to the add course page and select the course you want to update. Make the necessary changes and click on the "Update Course" button to save the changes.

Deleting a course
To delete a course, go to the add course page and select the course you want to delete. Click on the "Delete Course" button to delete the course.

Contributing
If you would like to contribute to this project, please feel free to fork the repository and submit a pull request.

License
This project is licensed under the MIT License.
