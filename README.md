# True Caller Django Application

This is a Django application designed to manage user registrations, contact lists, spam reports, and search functionalities. This guide will help you set up, test, and run the project in both development and production environments.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup](#setup)
  - [Development Environment](#development-environment)
  - [Production Environment](#production-environment)
- [Testing](#testing)
- [Running the Application](#running-the-application)
  - [Development](#development)
  - [Production](#production)
- [Environment Variables](#environment-variables)

## Prerequisites

- Python 3.9+
- Docker
- PostgreSQL (for production)

## Setup

### Development Environment

1. **Clone the repository:**

    ```sh
    git clone https://github.com/VirajAdiga/true-caller-django.git
    cd true-caller-django
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```sh
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

### Production Environment

1. **Clone the repository:**

    ```sh
    git clone https://github.com/VirajAdiga/true-caller-django.git
    cd true-caller-django
    ```

2. **Create a `.env` file:**

    ```sh
    touch .env
    ```

    Add the following content to the `.env` file:

    ```env
    SECRET_KEY=secret_key
    DEBUG=False
    DB_NAME=db_name
    DB_USER=db_user
    DB_PASSWORD=db_password
    DB_HOST=db_host
    DB_PORT=db_port
    ```

3. **Build and run the Docker container:**

    ```sh
    docker run -d -p 8000:8000 --env-file .env truecaller
    ```

## Testing

1. **Run tests using `pytest`:**

    ```sh
    pytest
    ```

## Running the Application

### Development

1. **Activate the virtual environment:**

    ```sh
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

### Production

1. **Build and run the Docker container:**

    ```sh
    docker run -d -p 8000:8000 --env-file .env truecaller
    ```

## Environment Variables

The following environment variables are used in this project:

- `SECRET_KEY`: The secret key for your Django application.
- `DEBUG`: Set to `False` for production.
- `DB_NAME`: The database name
- `DB_USER`: Database user
- `DB_PASSWORD`: Database password
- `DB_HOST`: Database host
- `DB_PORT`: Database port
