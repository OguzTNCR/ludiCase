# Project Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [Setup Instructions](#setup-instructions)

---

## Introduction
The project is a Django-based web application designed to manage and visualize user growth for different companies and their simulations. It includes functionalities for loading data from JSON files, displaying user growth charts, and managing company and user information.


## Setup Instructions

### Prerequisites
- Python 3.12
- Django 4.x
- SQLite (default database)

### Installation

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd ludiDashboard

    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

    pip install -r requirements.txt
    python manage.py makemigrations
    python manage.py migrate
    python manage.py load_data
    python manage.py runserver
    ```

### Open Your Web Browser

Open your preferred web browser and enter the following URL:
 http://127.0.0.1:8000/



### Navigating the Application

**Home Page:** The default page that loads when you access the application URL.

**User Growth Page:** To view the user growth chart, navigate to the specific URL configured in your Django application.

http://127.0.0.1:8000/user_growth/

**Company Page:** To view the company information, navigate to the specific URL configured in your Django application.

http://127.0.0.1:8000/company_users