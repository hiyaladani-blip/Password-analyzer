## *Password Analyzer* ##
A simple Python-based **Password Strength Analyzer** that evaluates the strength of a password based on common security criteria and provides suggestions for improving weak passwords.

## About the Project
The Password Analyzer is a beginner-friendly cybersecurity project developed in Python.
It checks a password against several basic security requirements, including:
* Password length
* Uppercase letters
* Lowercase letters
* Numbers
* Special characters
* Commonly used passwords
Based on these checks, the program classifies the password as **Very Weak, Weak, Medium, Strong, or Very Strong**.
It also provides specific suggestions to help improve the password.

## Features
* Checks password strength
* Detects commonly used passwords
* Checks minimum password length
* Checks for uppercase and lowercase letters
* Checks for numbers
* Checks for special characters
* Provides personalized improvement suggestions
* Simple command-line interface
* Built entirely using Python's standard library

## Technologies Used
* Python
* Regular Expressions (`re`)

## How It Works
The analyzer assigns a score based on five criteria:

At least 8 characters         -   +1 

Contains uppercase letter     -   +1 

Contains lowercase letter     -   +1 

Contains a number             -   +1 

Contains a special character  -   +1 

The final score determines the password strength: 

   0–2 -  Weak        
     3 - Medium      
     4 - Strong      
     5 - Very Strong 

### Common Password Detection
Before performing the regular strength checks, the program compares the password against a list of commonly used passwords such as:
* `123456`
* `password`
* `qwerty`
* `abc123`
* `admin`
* `welcome`
If a match is found, the password is immediately classified as **Very Weak**.

## Project Structure
```text
password-analyzer/
│
├── password_analyzer.py
└── README.md
```

## Learning Objectives
This project was created to practice:
* Python functions
* Conditional statements
* Sets
* Regular expressions
* String manipulation
* Input/output operations
* Basic cybersecurity concepts
* Writing user-friendly validation logic

##  Author
*Hiya Ladani*

Student | Computer Science Engineering
