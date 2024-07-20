# Django Blog API
## Overview

This project is a simple blog application built with Django and Django REST Framework. It provides basic CRUD functionalities for blog posts and comments, along with user authentication using JSON Web Tokens (JWT). The application also includes functionality for liking posts.

## Features

- **Post Model**: Create, read, update, and delete blog posts.
- **Comment Model**: Add comments to posts.
- **Authentication**: Token-based authentication with JWT.
- **Like System**: Users can like or unlike posts.

## Prerequisites

- Python 3.8 or later
- Django 4.x
- Django REST Framework 3.x
- `djangorestframework-simplejwt`

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/django-blog-api.git
    cd django-blog-api
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use: env\Scripts\activate
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations**:
    ```bash
    python manage.py migrate
    ```


5.**Endpoints**:
### Register

- **POST** `/register/`
  - Request body: `{ "username": "your_username", "password": "your_password" }`

### Authentication

- **POST** `/api/token/`
  - Request body: `{ "username": "your_username", "password": "your_password" }`
- **GET** `/api/token/refresh/`


### Posts

- **GET** `/api/posts/` - List all posts
- **POST** `/api/posts/` - Create a new post
- **GET** `/api/posts/<id>/` - Retrieve a single post
- **PUT** `/api/posts/<id>/` - Update a post
- **DELETE** `/api/posts/<id>/` - Delete a post
- **POST** `/api/posts/<post_id>/like/` - Like a post


### Comments

- **GET** `/api/posts/<post_id>/comments/` - List comments for a post
- **POST** `/api/posts/<post_id>/comments/` - Add a comment to a post


