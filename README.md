# Flight Scheduling System

## Description
The Flight Scheduling System is a web-based application designed to manage flight operations effectively. It enables users to schedule flights, manage passenger bookings, update flight statuses, and monitor employee information in a streamlined manner. Built using modern technologies, the system connects an Oracle database with a Flask-based backend and provides APIs that can be tested and accessed using Postman. This system is aimed at improving operational efficiency for airlines or travel agencies by digitizing and automating core processes.

## Technologies Used
Backend Framework: Flask (Python)
A lightweight and powerful web framework for building RESTful APIs.
Database: Oracle Database XE
Reliable and scalable database for storing flight, passenger, and employee data.
Database Connectivity: OracleDB Python Library
Ensures secure and efficient communication between Python and Oracle.
API Testing Tool: Postman
Used to test and document the API endpoints.
Other Tools:
Environment configuration with os library for handling sensitive data like database credentials.

## Key Features
Flight Management

Add, view, and manage flights with essential details such as flight number, departure and arrival times, available seats, and flight status.
Update flight statuses dynamically.
Passenger Management

Manage passenger information, including names, emails, and contact details.
Book and associate passengers with flights.
Employee Management

Add, view, update, and delete employee information.
Access control using roles and permissions for employee actions.
Booking System

Seamless booking functionality that checks flight availability and assigns seats to passengers.
Prevent overbooking by dynamically updating available seats.
Role-Based Permissions

Enforce role-based access control to ensure only authorized users can perform certain actions (e.g., adding employees or updating flight status).
API Integration

Expose RESTful APIs for easy integration with frontend systems or third-party tools.
Test and interact with APIs using Postman.
Error Handling

Comprehensive error handling to display meaningful error messages for database or validation issues.
