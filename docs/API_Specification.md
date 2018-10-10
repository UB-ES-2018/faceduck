# API Specification

- HTTP Codes used

| Code | Name                  |
|------|-----------------------|
| 200  | Ok                    |
| 204  | No Content            |
| 400  | Bad Request           |
| 403  | Forbidden             |
| 500  | Internal Server Error |

- 400 Error Ids

| Error Id | Error description                 |
|:--------:|-----------------------------------|
| 001      | Invalid data                      |
| 002      | Already existing username         |
| 003      | Already existing email            |
| 004      | This email or password is invalid |

## Sign up

### Request

**POST** `/user`

#### - Request headers

| Property     | Required | Values           |
|--------------|:--------:|:----------------:|
| Content-Type | Yes      | application/json |

#### - Request body

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Sign up",
    "type": "object",
    "properties": {
        "username": {"type": "string"},
        "email": {
            "type": "string",
            "format": "email"
        },
        "password": {"type": "string"},
        "name": {"type": "string"},
        "surname": {"type": "string"},
        "birthday": {"type": "string"},
        "gender": {"type": "string"}
    },
    "required": ["username", "email", "password", "name", "surname", "birthday", "gender"]
}
```

*Examples:*

```json
{
    "username": "test123",
    "email": "test@faceduck.com",
    "password": "12345",
    "name": "Scrum",
    "surname": "Master",
    "birthday": "1984-10-01",
    "gender": "male"
}
```

### Response: success

`204 No Content`

### Response: client error

`400 Bad Request`

#### - Response headers

| Property     | Values           |
|--------------|:----------------:|
| Content-Type | application/json |

#### - Response body

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Sign up error",
    "type": "object",
    "properties": {
        "error-id": {
            "type": "string",
            "enum": [
                "001",
                "002",
                "003"
            ]
        },
        "error-message": {"type": "string"}
    },
    "required": ["error-id", "error-message"]
}
```

*Examples:*

```json
{
    "error-id": "001",
    "error-message": "Invalid data",
}
```

### Response: server error

`500 Internal Server Error`

## Log in

### Request

**POST** `/session`

#### - Request headers

| Property     | Required | Values           |
|--------------|:--------:|:----------------:|
| Content-Type | Yes      | application/json |

#### - Request body

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Login",
    "type": "object",
    "properties": {
        "email": {
            "type": "string",
            "format": "email"
        },
        "password": {"type": "string"}
    },
    "required": ["email", "password"]
}
```

*Examples:*

```json
{
    "email": "test@faceduck.com",
    "password": "12345"
}
```

### Response: success

`200 Ok`

#### - Response headers

| Property     | Values           |
|--------------|:----------------:|
| Content-Type | application/json |

#### - Response body

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Login success",
    "type": "object",
    "properties": {
        "access-token": {"type": "string"},
        "user": {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "username": {"type": "string"},
                "email": {
                    "type": "string",
                    "format": "email"
                },
                "name": {"type": "string"},
                "surname": {"type": "string"},
                "birthday": {"type": "string"},
                "gender": {"type": "string"}
            },
            "required": [
                "id",
                "username", 
                "email",
                "name", 
                "surname", 
                "birthday", 
                "gender"
            ]
        }
    },
    "required": ["access-token", "user"]
}
```

*Examples:*

```json
{
    "access-token": "lfn1l324r0fcsanc031ekdjs",
    "user": {
        "id": "32",
        "username": "test123",
        "email": "test@faceduck.com",
        "name": "Scrum",
        "surname": "Master",
        "birthday": "1984-10-01",
        "gender": "male"
    }
}
```

### Response: client error

`400 Bad Request`

#### - Response headers

| Property     | Values           |
|--------------|:----------------:|
| Content-Type | application/json |

#### - Response body

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Login error",
    "type": "object",
    "properties": {
        "error-id": {
            "type": "integer",
            "enum": [
                "001",
                "004"
            ]
        },
        "error-message": {"type": "string"}
    },
    "required": ["error-id", "error-message"]
}
```

*Examples:*

```json
{
    "error-id": "004",
    "error-message": "This email or password is invalid",
}
```

### Response: server error

`500 Internal Server Error`

## Search user

### Request

**POST** `/user/search`

#### - Request headers

| Property     | Required | Values           |
|--------------|:--------:|:----------------:|
| Content-Type | Yes      | application/json |

#### - Request body

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Search user",
    "type": "object",
    "properties": {
        "query": {"type": "string"}
    },
    "required": ["query"]
}
```

*Examples:*

```json
{
    "query": "scrum master"
}
```

### Response: success

`200 Ok`

#### - Response headers

| Property     | Values           |
|--------------|:----------------:|
| Content-Type | application/json |

#### - Response body

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Search user success",
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "username": {"type": "string"},
            "email": {
                "type": "string",
                "format": "email"
            },
            "name": {"type": "string"},
            "surname": {"type": "string"},
            "birthday": {"type": "string"},
            "gender": {"type": "string"}
        },
        "required": [
            "id",
            "username", 
            "email",
            "name", 
            "surname", 
            "birthday", 
            "gender"
        ]
    }
}
```

*Examples:*

```json
[
    {
        "id": "32",
        "username": "test123",
        "email": "test@faceduck.com",
        "name": "Scrum",
        "surname": "Master",
        "birthday": "1984-10-01",
        "gender": "male"
    },
    {
        "id": "34",
        "username": "test2",
        "email": "test2@faceduck.com",
        "name": "Scrum",
        "surname": "Master2",
        "birthday": "1986-10-01",
        "gender": "female"
    }
]
```

### Response: client error

`400 Bad Request`

#### - Response headers

| Property     | Values           |
|--------------|:----------------:|
| Content-Type | application/json |

#### - Response body

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Login error",
    "type": "object",
    "properties": {
        "error-id": {
            "type": "integer",
            "enum": [
                "001"
            ]
        },
        "error-message": {"type": "string"}
    },
    "required": ["error-id", "error-message"]
}
```

*Examples:*

```json
{
    "error-id": "001",
    "error-message": "Invalid data"
}
```

### Response: server error

`500 Internal Server Error`

## Search post

### Request

**POST** `/post/search`

#### - Request headers

| Property     | Required | Values           |
|--------------|:--------:|:----------------:|
| Content-Type | Yes      | application/json |

#### - Request body

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Search post",
    "type": "object",
    "properties": {
        "query": {"type": "string"}
    },
    "required": ["query"]
}
```

*Examples:*

```json
{
    "query": "hello"
}
```

### Response: success

`200 Ok`

#### - Response headers

| Property     | Values           |
|--------------|:----------------:|
| Content-Type | application/json |

#### - Response body

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Search user success",
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "text": {"type": "string"},
            "created-at": {"type": "string"},
            "author": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "username": {"type": "string"},
                    "email": {
                        "type": "string",
                        "format": "email"
                    },
                    "name": {"type": "string"},
                    "surname": {"type": "string"},
                    "birthday": {"type": "string"},
                    "gender": {"type": "string"}
                },
                "required": [
                    "id",
                    "username", 
                    "email",
                    "name", 
                    "surname", 
                    "birthday", 
                    "gender"
                ]
            }
        },
        "required": [
            "text", 
            "created-at", 
            "author"
        ]
    }
}
```

*Examples:*

```json
[
    {
        "id": "45",
        "text": "Hello this is a post.",
        "created-at": "12-01-2018, 03:45:34",
        "author": {
            "id": "32",
            "username": "test123",
            "email": "test@faceduck.com",
            "name": "Scrum",
            "surname": "Master",
            "birthday": "1984-10-01",
            "gender": "male"
        }
    },
    {
        "id": "34",
        "text": "Hello this is another post.",
        "created-at": "13-01-2018, 03:45:34",
        "author": {
            "id": "34",
            "username": "test2",
            "email": "test2@faceduck.com",
            "name": "Scrum",
            "surname": "Master2",
            "birthday": "1986-10-01",
            "gender": "female"
        }
    }
]
```



### Response: client error

`400 Bad Request`

#### - Response headers

| Property     | Values           |
|--------------|:----------------:|
| Content-Type | application/json |

#### - Response body

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Login error",
    "type": "object",
    "properties": {
        "error-id": {
            "type": "integer",
            "enum": [
                "001"
            ]
        },
        "error-message": {"type": "string"}
    },
    "required": ["error-id", "error-message"]
}
```

*Examples:*

```json
{
    "error-id": "001",
    "error-message": "Invalid data"
}
```

### Response: server error

`500 Internal Server Error`
