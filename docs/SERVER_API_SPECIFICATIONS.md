
# Server API Specifications

## Authentication Endpoints

### Register
- **URL**: `/register`
- **Method**: `POST`
- **Form Data**:
  - `username` (required, 3-64 chars)
  - `email` (required, valid email)
  - `password` (required, min 6 chars)
  - `password2` (must match password)
- **Response**: Redirects to login page on success

### Login
- **URL**: `/login`
- **Method**: `POST`
- **Form Data**:
  - `username` (required)
  - `password` (required)
- **Response**: Redirects to memo page on success

### Logout
- **URL**: `/logout`
- **Method**: `GET`
- **Auth**: Required
- **Response**: Redirects to login page

## Memo Endpoints

### Get Memo
- **URL**: `/memo`
- **Method**: `GET`
- **Auth**: Required
- **Response**: Renders memo page with user's memo content

### Save Memo
- **URL**: `/api/save-memo`
- **Method**: `POST`
- **Auth**: Required
- **Content-Type**: `application/json`
- **Request Body**:
  ```json
  {
    "content": "string"
  }
  ```
- **Success Response**:
  ```json
  {
    "status": "success"
  }
  ```
- **Error Response**:
  ```json
  {
    "status": "error",
    "message": "error description"
  }
  ```

## Security
- CSRF protection via Flask-WTF
- Session-based authentication
- Required session cookies for authenticated routes
