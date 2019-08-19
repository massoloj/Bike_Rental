# Bike Rental

## Author

Julián Massolo

## Project description

This project models a company's bike rental business. There are 3 types of rental:

* 1 - Rental by hour, charging $5 per hour
* 2 - Rental by day, charging $20 a day
* 3 - Rental by week, changing $60 a week
* 4 - Family Rental, is a promotion that can include from 3 to 5 Rentals (of any type) with a
discount of 30% of the total price

## Project structure
###### Bike_Rental
    |
    |-- app: contains the business logic
    |    |
    |    |-- models: contains the logic model of the application
    |    |-- managers: contains all the operations that can be performed over each model
    |    |-- utils: contains useful methods and classes for data validation and enumerations
    |
    |-- tests: contains the tests that validate the functionalities of the app
    |     |
    |     |-- models: tests for the models classes
    |     |-- managers: tests for the manager classes
    |     |-- run.py: file that executes all the tests
    |
    |-- requirements.txt: contains all the libraries that must be installed to test the project
    
## Requirements

In order to run the project's tests, install all the libraries detailed in the __requirements.txt__
file. For this task, it is recommended to create a virtual environment.
If more information about environments is needed, visit the conda website at https://docs.conda.io/en/latest/

## Running the tests

To run all the tests cases, go to tests directory and execute the __run.py__ file with the following command:

__pytest -s run.py__
