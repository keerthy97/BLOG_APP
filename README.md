# Django Blog API

## Endpoints

### Authentication

- **POST** `/api/token/`
  - Request body: `{ "username": "your_username", "password": "your_password" }`

### Posts

- **GET** `/api/posts/` - List all posts
- **POST** `/api/posts/` - Create a new post
- **GET** `/api/posts/<id>/` - Retrieve a single post
- **PUT** `/api/posts/<id>/` - Update a post
- **DELETE** `/api/posts/<id>/` - Delete a post

### Comments

- **GET** `/api/posts/<post_id>/comments/` - List comments for a post
- **POST** `/api/posts/<post_id>/comments/` - Add a comment to a post
