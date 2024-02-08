# Back-End FastAPI wihth Supabase

## .env

```env
SUPABASE_URL=""
SUPABASE_KEY=""
```

- SUPABASE_URL and SUPABASE_KEY get at [https://supabase.com/dashboard/project/](https://supabase.com/dashboard/project/)

## Endpoint

### ` POST http://127.0.0.1:8000/signup`

```json
{
  "email": "string",
  "password": "string"
}
```

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/signup' \
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

### `POST http://127.0.0.1:8000/signin`

```json
{
  "email": "string",
  "password": "string"
}
```

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/signin' \
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

## `GET http://127.0.0.1:8000/profile`

````

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/profile' \
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

## `GET http://127.0.0.1:8000/logout`

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/logout' \
  -H 'accept: application/json'
```

- if success

```json
{
  "status": "ok",
  "data": "Sign out successfully"
}
```

##
