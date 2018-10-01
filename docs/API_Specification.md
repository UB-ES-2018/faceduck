# API Specification

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

### Response success

`200 OK`

### Response error

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
        "error-id": {"type": "integer"},
        "error-message": {"type": "string"}
    },
    "required": ["error-id", "error-message"]
}
```

*Examples:*

```json
{
    "error-id": "4567",
    "error-message": "Non valid email.",
}
```
