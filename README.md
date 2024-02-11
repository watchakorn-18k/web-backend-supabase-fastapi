# Back-End FastAPI wihth Supabase

## Front-end

Can you see the frontend code?

```
https://github.com/watchakorn-18k/web-frontend-supabase
```

## Getting Started

First, run the development server:

```bash
git clone https://github.com/watchakorn-18k/web-backend-supabase-fastapi
pip install -r requirements.txt
uvicorn main:app --reload
```

## .env

```env
SUPABASE_URL=""
SUPABASE_KEY=""
```

- SUPABASE_URL and SUPABASE_KEY get at [https://supabase.com/dashboard/project/](https://supabase.com/dashboard/project/)

## Endpoint

## user/

### ` POST http://127.0.0.1:8000/user/signup`

```json
{
  "email": "string",
  "password": "string"
}
```

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/user/signup' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "string",
  "password": "string"
}'
```

- if success return

```json
{
  "status": "ok",
  "data": {
    "user": {..........
    ......: ..........
    }
  }
```

### `POST http://127.0.0.1:8000/user/signin`

```json
{
  "email": "string",
  "password": "string"
}
```

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/user/signin' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "string",
  "password": "string"
}'
```

- if success return

```json
{
  "status": "ok",
  "data": {
    "user": {
      "id": ".....",
      "app_metadata": {
        "provider": "email",
        "providers": ["email"]
      },
      "user_metadata": {},
      "aud": "authenticated"
    }
  }
}
```

- else return

```json
{
  "status": "ok",
  "data": {
    "message": "Invalid login credentials",
    "name": "AuthApiError",
    "status": 400
  }
}
```

## `GET http://127.0.0.1:8000/user/profile`

````

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/user/profile' \
  -H 'accept: application/json'
````

- if after login return

```json
  "status": "ok",
  "data": {
    "access_token": ".....",
    "data_user": {
      ............
    }
  }
```

- else retern

```json
{
  "status": "fail",
  "data": "Please login"
}
```

## `GET http://127.0.0.1:8000/user/logout`

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/user/logout' \
  -H 'accept: application/json'
```

- if success

```json
{
  "status": "ok",
  "data": "Sign out successfully"
}
```

## course/

## `GET http://127.0.0.1:8000/course/get-course/-id-` # change `-id-` to course id

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/course/get-course/-id-' \
  -H 'accept: application/json'
```

- if success

```json
{
  "status": "ok",
  "data": [
    {
      "id": 1,
      "name": "Python-101",
      "created_at": "2024-02-09T16:57:12.126581+00:00",
      "price": 200,
      ..............]
    }
}
```

- else return

```json
{
  "status": "fail",
  "data": "Please login"
}
```

## `GET http://127.0.0.1:8000/course`

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/course' \
  -H 'accept: application/json'
```

- if success

```json
{
  "status": "ok",
  "data": [
    {
      "id": 1,
      "name": "Python-101",
      "created_at": "2024-02-09T16:57:12.126581+00:00",
      "price": 200,
      ..............]
    }
}
```

## `POST http://127.0.0.1:8000/course/add-course`

```json
{
  "name": "python-101",
  "price": 300,
  "details": "basic python"
}
```

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/course/add-course' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name":"python-101",
  "price":300,
  "details":"basic python"
}'
```

- if success

```json
{
  "status": "ok",
  "data": [
    {
      "id": 1,
      "name": "Python-101",
      "created_at": "2024-02-09T16:57:12.126581+00:00",
      "price": 200,
      ..............]
    }
}
```

- else return

```json
{
  "status": "fail",
  "data": "Please login"
}
```

## `PATCH http://127.0.0.1:8000/course/edit-course/-id-` # change `-id-` to course id

```json
{
  "name": "python-101",
  "price": 300,
  "details": "basic python"
}
```

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/course/edit-course/-id-' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name":"python-101",
  "price":300,
  "details":"basic python"
}'
```

- if success

```json
{
  "status": "ok",
  "data": [
    {
      "id": 1,
      "name": "Python-101",
      "created_at": "2024-02-09T16:57:12.126581+00:00",
      "price": 200,
      ..............]
    }
}
```

- else return

```json
{
  "status": "fail",
  "data": "Please login"
}
```

## `DELETE http://127.0.0.1:8000/course/delete-course/-id-` # change `-id-` to course id

```bash
curl -X 'DELETE' \
  'http://127.0.0.1:8000/course/delete-course/-id-' \
  -H 'accept: application/json'
```

- if success

```json
{
  "status": "ok",
  "data": [
    {
      "id": 1,
      "name": "Python-101",
      "created_at": "2024-02-09T16:57:12.126581+00:00",
      "price": 200,
      ..............]
    }
}
```

- case not found

```json
{
  "status": "fail",
  "data": ["1", "already deleted", "data not found"]
}
```

- else return

```json
{
  "status": "fail",
  "data": "Please login"
}
```
