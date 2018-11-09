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
| 010      | Media is too big                  |

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

## Create Post

### Request

**POST** `/post`

#### - Request headers

| Property      | Required | Values                |
|---------------|:--------:|:---------------------:|
| Content-Type  | Yes      | application/json      |
| Authorization | Yes      | Bearer {access-token} |

*Examples:*

```
Content-Type: application/json
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOi
```

#### - Request body

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Create post",
    "type": "object",
    "properties": {
        "text": {"type": "string"},
        "author-id": {"type": "string"},
        "image-url": {"type": "string"}
    },
    "required": [
        "text",
        "author-id"
    ]
}
```

*Examples:*

```json
{
    "text": "Hello this is a post.",
    "author-id": "32",
    "image-url": "http://localhost:5000/media/1.jpg"
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
    "title": "Create post success",
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "text": {"type": "string"},
        "created-at": {"type": "string"},
        "image-url": {"type": "string"},
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
        "id",
        "text",
        "created-at",
        "author"
    ]
}
```

*Examples:*

```json
{
    "id": "42",
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
    },
    "image-url": "http://localhost:5000/media/1.jpg"
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
    "title": "Create post error",
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

## Get Post

### Request

**GET** `/post/{post_id}`

#### - Request headers

| Property      | Required | Values                |
|---------------|:--------:|:---------------------:|
| Authorization | Yes      | Bearer {access-token} |

*Examples:*

```
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOi
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
    "title": "Get post success",
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "text": {"type": "string"},
        "created-at": {"type": "string"},
        "image-url": {"type": "string"},
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
        },
        "reactions-count": {
            {
                "count": {"type": "integer"},
                "reaction": {"type": "string"}
            }
        },
        "user-reaction": {
            {
                "reaction": {"type": "string"},
                "user-id": {"type": "string"}
            }
        }
    },
    "required": [
        "id",
        "text",
        "created-at",
        "author"
    ]
}
```

*Examples:*

```json
{
    "id": "42",
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
    },
    "image-url": "http://localhost:5000/media/1.jpg",
    "reactions-count": [
        {
            "count": 1,
            "reaction": "love"
        },
        {
            "count": 1,
            "reaction": "like"
        }
    ],
    "user-reaction": [
        {
            "reaction": "like",
            "user-id": "32"
        },
        {
            "reaction": "love",
            "user-id": "42"
        }
    ]
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
    "title": "Get post error",
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

## Search user

### Request

**POST** `/user/search`

#### - Request headers

| Property      | Required | Values                |
|---------------|:--------:|:---------------------:|
| Content-Type  | Yes      | application/json      |
| Authorization | Yes      | Bearer {access-token} |

*Examples:*

```
Content-Type: application/json
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOi
```

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
    "title": "Search user error",
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

| Property      | Required | Values                |
|---------------|:--------:|:---------------------:|
| Content-Type  | Yes      | application/json      |
| Authorization | Yes      | Bearer {access-token} |

*Examples:*

```
Content-Type: application/json
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOi
```

#### - Request body

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Search post",
    "type": "object",
    "properties": {
        "query": {"type": "string"},
        "author-id": {"type": "string"}
    },
    "oneOf": [
        {
            "required": [
                "query"
            ]
        },
        {
            "required": [
                "author-id"
            ]
        }
    ]
}
```

*Examples:*

Search by post matching content:
```json
{
    "query": "hello"
}
```

Search by the author:
```json
{
    "author-id": "34"
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
    "title": "Search post success",
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
            },
            "reactions-count": {
            {
                "count": {"type": "integer"},
                "reaction": {"type": "string"}
            }
            },
            "user-reaction": {
                {
                    "reaction": {"type": "string"},
                    "user-id": {"type": "string"}
                }
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
        },
        "reactions-count": [
            {
                "count": 2,
                "reaction": "like"
            }
        ],
        "user-reaction": [
            {
                "reaction": "like",
                "user-id": "32"
            },
            {
                "reaction": "like",
                "user-id": "42"
            }
        ]
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
        },
        "reactions-count": [
            {
                "count": 2,
                "reaction": "love"
            }
        ],
        "user-reaction": [
            {
                "reaction": "love",
                "user-id": "32"
            },
            {
                "reaction": "love",
                "user-id": "42"
            }
        ]
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
    "title": "Search post error",
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

## Create Media (Upload)

### Request

**POST** `/media`

#### - Request headers

| Property      | Required | Values                |
|---------------|:--------:|:---------------------:|
| Content-Type  | Yes      | multipart/form-data   |
| Authorization | Yes      | Bearer {access-token} |

*Examples:*

```
Content-Type: multipart/form-data
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOi
```

#### - Request body

Multipart fields:
* `file`: type `file`, contains binary data of image.

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
    "title": "Create Media success",
    "type": "object",
    "properties": {
        "media-url": {"type": "string"}
    },
    "required": [
        "media-url"
    ]
}
```

*Examples:*

```json
{
    "media-url": "http://localhost:5000/media/1.jpg"
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
    "title": "Create media error",
    "type": "object",
    "properties": {
        "error-id": {
            "type": "integer",
            "enum": [
                "001",
                "010"
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
    "error-id": "010",
    "error-message": "Media is too big"
}
```

### Response: server error

`500 Internal Server Error`

## Create Friendship

### Request

**POST** `/user/friends`

#### - Request headers

| Property      | Required | Values                |
|---------------|:--------:|:---------------------:|
| Content-Type  | Yes      | application/json      |
| Authorization | Yes      | Bearer {access-token} |

*Examples:*

```
Content-Type: application/json
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOi
```

#### - Request body

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Create friendship",
    "type": "object",
    "properties": {
        "target_id": {"type": "string"},
    },
    "required": [
        "target_id"
    ]
}
```

*Examples:*

```json
{
    "target_id" : "23"
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
    "title": "Create friendship success",
    "type": "object",
    "properties": {
        "state": {"type": "string"},
        "target_id": {"type": "string"},
        "user_id": {"type": "string"},
    },
    "required": [
        "state",
        "target_id",
        "user_id"
    ]
}
```

*Examples:*

```json
{
    "state": "pending",
    "target_id": "34",
    "user_id": "23"
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
    "title": "Create friendship error",
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

## Update Friendship

### Request

**PUT** `/user/friends`

#### - Request headers

| Property      | Required | Values                |
|---------------|:--------:|:---------------------:|
| Content-Type  | Yes      | application/json      |
| Authorization | Yes      | Bearer {access-token} |

*Examples:*

```
Content-Type: application/json
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOi
```

#### - Request body

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Update friendship",
    "type": "object",
    "properties": {
        "target_id": {"type": "string"},
        "state":{
            "type": "string",
            "enum": ["pending", "friends"]
        }
    },
    "required": [
        "target_id",
        "state"
    ]
}
```

*Examples:*

```json
{
    "target_id" : "23",
    "state" : "friends"
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
    "title": "Update friendship success",
    "type": "object",
    "properties": {
        "state": {"type": "string"},
        "target_id": {"type": "string"},
        "user_id": {"type": "string"}
    },
    "required": [
        "state",
        "target_id",
        "user_id"
    ]
}
```

*Examples:*

```json
{
    "state": "friends",
    "target_id": "34",
    "user_id": "23"
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
    "title": "Create post error",
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

## Get Friends

### Request

**GET** `/user/friends/{user_id}`

#### - Request headers

| Property      | Required | Values                |
|---------------|:--------:|:---------------------:|
| Authorization | Yes      | Bearer {access-token} |

*Examples:*

```
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOi
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
    "title": "Get post success",
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "state": {"type": "string"},
        "target_id": {"type": "string"},
        "user_id": {"type": "string"}
    },
    "required": [
        "id",
        "state",
        "target_id",
        "user_id"
    ]
}
```

*Examples:*

```json
[
    {
        "id": "12345",
        "state": "friends",
        "target-id": "42",
        "user-id": "23"
    },
    {
        "id": "54321",
        "state": "friends",
        "target-id": "32",
        "user-id": "23"
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
    "title": "Get post error",
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


## Delete Friendship

### Request

**DELETE** `/user/friends`

#### - Request headers

| Property      | Required | Values                |
|---------------|:--------:|:---------------------:|
| Content-Type  | Yes      | application/json      |
| Authorization | Yes      | Bearer {access-token} |

*Examples:*

```
Content-Type: application/json
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOi
```

#### - Request body

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Create friendship",
    "type": "object",
    "properties": {
        "target_id": {"type": "string"}
    },
    "required": [
        "target_id"
    ]
}
```

*Examples:*

```json
{
    "target_id" : "23"
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
    "title": "Create post error",
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


## Add Reaction

### Request

**POST** `/post/{post_id}/reactions`

#### - Request headers

| Property      | Required | Values                |
|---------------|:--------:|:---------------------:|
| Content-Type  | Yes      | application/json      |
| Authorization | Yes      | Bearer {access-token} |

*Examples:*

```
Content-Type: application/json
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOi
```

#### - Request body

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Create friendship",
    "type": "object",
    "properties": {
        "reaction": {"type": "string"},
    },
    "required": [
        "reaction"
    ]
}
```

*Examples:*

```json
{
    "reaction" : "like"
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
    "title": "Get post success",
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "text": {"type": "string"},
        "created-at": {"type": "string"},
        "image-url": {"type": "string"},
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
        },
        "reactions-count": {
            {
                "count": {"type": "integer"},
                "reaction": {"type": "string"}
            }
        },
        "user-reaction": {
            {
                "reaction": {"type": "string"},
                "user-id": {"type": "string"}
            }
        }
    },
    "required": [
        "id",
        "text",
        "created-at",
        "author"
    ]
}
```

*Examples:*

```json
{
    "id": "42",
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
    },
    "image-url": "http://localhost:5000/media/1.jpg",
    "reactions-count": [
        {
            "count": 1,
            "reaction": "love"
        },
        {
            "count": 1,
            "reaction": "like"
        }
    ],
    "user-reaction": [
        {
            "reaction": "like",
            "user-id": "32"
        },
        {
            "reaction": "love",
            "user-id": "42"
        }
    ]
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
    "title": "Create friendship error",
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

## Delete Reaction

### Request

**DELETE** `/post/{post_id}/reactions`

#### - Request headers

| Property      | Required | Values                |
|---------------|:--------:|:---------------------:|
| Content-Type  | Yes      | application/json      |
| Authorization | Yes      | Bearer {access-token} |

*Examples:*

```
Content-Type: application/json
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOi
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
    "title": "Create post error",
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

