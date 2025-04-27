# Project Name

A Django-based GraphQL/API service managing courses, users, enrollments, and appointments.

## Project Overview

The code is organized into two main directories:

- **`src/`** – project configuration (ASGI, WSGI, settings, URLs, schema).  
- **`courses/`** – your main Django app with models, queries, mutations (Graphene-Django), serializers, utils, enums, managers, middlewares, and tests.

## Prerequisites

- Python 3.12+  
- pip  
- (Optional) virtualenv or venv  

## Installation

1. **Clone the repo**  
   ```bash
    git clone https://github.com/lawalgodwin/voltis-academy.git
    cd voltis-academy
   ```
2. **Create and activate a virtual environment**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate        # Linux/macOS
    .venv\Scripts\activate           # Windows
    ```
3. **Install dependencies**
    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
4. **Apply migrations**
    ```bash
    python manage.py migrate
    ```
5. **(Optional) Load initial data**
    ```bash
    python manage.py loaddata initial_data.json
    ```
6. **Running the Development Server**
    ```bash
    python manage.py runserver
    ```

### Accessing the API

- The api is accessible on the host <http://localhost:8000/graphql> by default
- Visit [samples api requests](apidocs.md) to see samples of queries and mutations