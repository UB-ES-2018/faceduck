# API Specification

## Table of contents

- [Summary of codes and ids](#summary-of-codes-and-ids)
- [Sign up](#sign-up)
- [Log in](#log-in)
- [Create Post](#create-post)
- [Get Post](#get-post)
- [Search user](#search-user)
- [Search post](#search-post)
- [Create Media (Upload)](#create-media-upload)
- [Create Friendship](#create-friendship)
- [Update Friendship](#update-friendship)
- [Get Friends](#get-friends)
- [Delete Friendship](#delete-friendship)
- [Add Comment](#add-comment)
- [Get Post Comments](#get-post-comments)
- [Delete Post Comment](#delete-post-comment)
- [Add Reaction](#add-reaction)
- [Delete Reaction](#delete-reaction)
- [Create Group](#create-group)
- [Get Group](#get-group)
- [Delete Group](#delete-group)
- [Create Group Post](#create-group-post)
- [Get Group Posts](#get-group-posts)
- [Get Group Post](#get-group-post)
- [Delete Group Post](#delete-group-post)
- [Add Member to Group](#add-member-to-group)
- [Get Group Members](#get-group-members)
- [Get Group Admins](#get-group-admins)
- [Update User Role](#update-user-role)
- [Get Group User](#get-group-user)
- [Delete Group User](#delete-group-user)

## Summary of codes and ids

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
            "type": "string",
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
        "image-url": {"type": "string"}
    },
    "required": [
        "text"
    ]
}
```

*Examples:*

```json
{
    "text": "Hello this is a post.",
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
            "type": "string",
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
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "count": {"type": "integer"},
                    "reaction": {"type": "string"}
                },
                "required": [
                    "count",
                    "reaction"
                ]
            }
        },
        "user-reaction": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "reaction": {"type": "string"},
                    "user-id": {"type": "string"}
                },
                "required": [
                    "reaction",
                    "user-id"
                ]
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
            "type": "string",
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
            "type": "string",
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
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "count": {"type": "integer"},
                        "reaction": {"type": "string"}
                    },
                    "required": [
                        "count",
                        "reaction"
                    ]
                }
            },
            "user-reaction": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "reaction": {"type": "string"},
                        "user-id": {"type": "string"}
                    },
                    "required": [
                        "reaction",
                        "user-id"
                    ]
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
            "type": "string",
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
            "type": "string",
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
        "state": {
            "type": "string",
            "enum": ["pending", "friends"]
        },
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
            "type": "string",
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
        "state": {
            "type": "string",
            "enum": ["pending", "friends"]
        },
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
            "type": "string",
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
    "title": "Get friends success",
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "state": {
                "type": "string",
                "enum": ["pending", "friends"]
            },
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
    "title": "Delete friendship",
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
    "title": "Delete friendship error",
    "type": "object",
    "properties": {
        "error-id": {
            "type": "string",
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

## Add Comment

### Request

**POST** `/post/{post_id}/comments`

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
    "title": "Add comment",
    "type": "object",
    "properties": {
        "text": {"type": "string"},
    },
    "required": [
        "text"
    ]
}
```

*Examples:*

```json
{
    "text" : "This is a test comment"
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
    "title": "Add comment success",
    "type": "object",
    "properties": {
        "comment_id": {"type": "string"},
        "text": {"type": "string"},
        "user_id": {"type": "string"},
    },
    "required": [
        "comment_id",
        "text",
        "user_id"
    ]
}
```

*Examples:*

```json
{
    "comment_id": "1",
    "text": "This is a test comment",
    "user_id": "42",
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
    "title": "Add comment error",
    "type": "object",
    "properties": {
        "error-id": {
            "type": "string",
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

## Get Post Comments

### Request

**GET** `/post/{post_id}/comments`

#### - Request headers

| Property      | Required | Values                |
|---------------|:--------:|:---------------------:|
| Content-Type  | Yes      | application/json      |


*Examples:*

```
Content-Type: application/json
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
    "title": "Get comments success",
    "type": "object",
    "properties": {
        "comment_id": {"type": "string"},
        "text": {"type": "string"},
        "user_id": {"type": "string"},
    },
    "required": [
        "comment_id",
        "text",
        "user_id"
    ]
}
```

*Examples:*

```json
[
    {
        "comment_id": "1",
        "text": "This is a test comment",
        "user_id": "42",
    },
    {
        "comment_id": "2",
        "text": "This is a test comment",
        "user_id": "34",
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
    "title": "Get comments error",
    "type": "object",
    "properties": {
        "error-id": {
            "type": "string",
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

## Delete Post Comment

### Request

**DELETE** `/post/{post_id}/comments`

#### - Request headers

| Property      | Required | Values                |
|---------------|:--------:|:---------------------:|
| Content-Type  | Yes      | application/json      |


*Examples:*

```
Content-Type: application/json
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
    "title": "Delete comment error",
    "type": "object",
    "properties": {
        "error-id": {
            "type": "string",
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
    "title": "Add reaction",
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
    "title": "Add reaction success",
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
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "count": {"type": "integer"},
                    "reaction": {"type": "string"}
                },
                "required": [
                    "count",
                    "reaction"
                ]
            }
        },
        "user-reaction": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "reaction": {"type": "string"},
                    "user-id": {"type": "string"}
                },
                "required": [
                    "reaction",
                    "user-id"
                ]
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
    "title": "Add reaction error",
    "type": "object",
    "properties": {
        "error-id": {
            "type": "string",
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
    "title": "Delete reaction error",
    "type": "object",
    "properties": {
        "error-id": {
            "type": "string",
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

## Create Group

### Request

**POST** `/group`

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
        "name": {"type": "string"},
        "image-url": {"type": "string"}
    },
    "required": [
        "name"
    ]
}
```

*Examples:*

```json
{
    "name": "Test Group",
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
        "name": {"type": "string"},
        "image-url": {"type": "string"},
        "admins": {
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
        },
        "users": {
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
    },
    "required": [
        "id",
        "name"
    ]
}
```

*Examples:*

```json
{
    "id": "300",
    "name": "Test Group",
    "image-url": "http://localhost:5000/media/1.jpg",
    "admins": [
        {
            "id" : "45",
            "username" : "test",
            "email" : "test@test.com",
            "name" : "Test",
            "surname" : "User",
            "birthday": "1984-10-01",
            "gender": "male"
        }
    ],
    "users": [
        {
            "id" : "45",
            "username" : "test",
            "email" : "test@test.com",
            "name" : "Test",
            "surname" : "User",
            "birthday": "1984-10-01",
            "gender": "male"
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
    "title": "Create group error",
    "type": "object",
    "properties": {
        "error-id": {
            "type": "string",
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


## Get Group

### Request

**GET** `/group/{group_id}`


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
        "name": {"type": "string"},
        "image-url": {"type": "string"},
        "admins": {
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
        },
        "users": {
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
        },
        "posts": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "text": {"type": "string"},
                    "created-at": {"type": "string"},
                    "image-url": {"type": "string"},
                    "author": {"type":"User"},
                    "reactions-count" : {"type":"array"},
                    "user-reaction":{"type":"array"}
                },
                "required": [
                    "id",
                    "text",
                    "created-at",
                    "author"
                ]
            }
        }
    },
    "required": [
        "id",
        "name",
        "admins",
        "users"
    ]
}
```

*Examples:*

```json
{
    "id": "300",
    "name": "Test Group",
    "image-url": "http://localhost:5000/media/1.jpg",
    "admins": [
        {
            "id" : "45",
            "username" : "test",
            "email" : "test@test.com",
            "name" : "Test",
            "surname" : "User",
            "birthday": "1984-10-01",
            "gender": "male"
        }
    ],
    "users": [
        {
            "id" : "45",
            "username" : "test",
            "email" : "test@test.com",
            "name" : "Test",
            "surname" : "User",
            "birthday": "1984-10-01",
            "gender": "male"
        },{
            "id" : "45",
            "username" : "test",
            "email" : "test@test.com",
            "name" : "Test",
            "surname" : "User",
            "birthday": "1984-10-01",
            "gender": "male"
        }
    ],
    "posts":[
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
    "title": "Get group error",
    "type": "object",
    "properties": {
        "error-id": {
            "type": "string",
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

## Delete Group

### Request

**DELETE** `/group/{group_id}`

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
    "title": "Delete group error",
    "type": "object",
    "properties": {
        "error-id": {
            "type": "string",
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

## Create Group Post

### Request

**POST** `/group/{group_id}/posts`

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
        "image-url": {"type": "string"}
    },
    "required": [
        "text"
    ]
}
```

*Examples:*

```json
{
    "text": "Hello this is a group post.",
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
    "title": "Create group post success",
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
    "text": "Hello this is a group post.",
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
    "title": "Create group post error",
    "type": "object",
    "properties": {
        "error-id": {
            "type": "string",
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


## Get Group Posts

### Request

**GET** `/group/{group_id}/posts`

#### - Request headers

| Property      | Required | Values                |
|---------------|:--------:|:---------------------:|
| Content-Type  | Yes      | application/json      |

*Examples:*

```
Content-Type: application/json
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
    "title": "Get group posts success",
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
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "count": {"type": "integer"},
                        "reaction": {"type": "string"}
                    },
                    "required": [
                        "count",
                        "reaction"
                    ]
                }
            },
            "user-reaction": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "reaction": {"type": "string"},
                        "user-id": {"type": "string"}
                    },
                    "required": [
                        "reaction",
                        "user-id"
                    ]
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
    "title": "Get group posts error",
    "type": "object",
    "properties": {
        "error-id": {
            "type": "string",
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

## Get Group Post

### Request

**GET** `/group/{group_id}/posts/{post_id}`

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
    "title": "Get group post success",
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
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "count": {"type": "integer"},
                    "reaction": {"type": "string"}
                },
                "required": [
                    "count",
                    "reaction"
                ]
            }
        },
        "user-reaction": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "reaction": {"type": "string"},
                    "user-id": {"type": "string"}
                },
                "required": [
                    "reaction",
                    "user-id"
                ]
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
    "text": "Hello this is a group post.",
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
    "title": "Get group post error",
    "type": "object",
    "properties": {
        "error-id": {
            "type": "string",
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

## Delete Group Post

### Request

**DELETE** `/group/{group_id}/posts/{post_id}`

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
    "title": "Delete group post error",
    "type": "object",
    "properties": {
        "error-id": {
            "type": "string",
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

## Add member to group

### Request

**POST** `/group/{group_id}/members`

#### - Request headers

| Property     | Required | Values           |
|--------------|:--------:|:----------------:|
| Content-Type | Yes      | application/json |

#### - Request body

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Add member to group",
    "type": "object",
    "properties": {
        "user_id": {"type": "string"},
        
    },
    "required": []
}
```
*if no user_id is provided it adds the current user*
*Examples:*

```json
{
    "user_id" : "47"
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
    "title": "Add user error",
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

## Get group members

### Request

**GET** `/group/{group_id}/members`


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
    "type": "array",
    "properties": {
        {
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
[
    {
        "id": "32",
        "username": "test123",
        "email": "test@faceduck.com",
        "name": "Scrum",
        "surname": "Master",
        "birthday": "1984-10-01",
        "gender": "male"
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
    "title": "Get members error",
    "type": "object",
    "properties": {
        "error-id": {
            "type": "string",
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
}
```

### Response: server error

`500 Internal Server Error`

## Get group admins

### Request

**GET** `/group/{group_id}/members/admins`


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
    "title": "Get group admins success",
    "type": "array",
    "properties": {
        {
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
[ 
    {
        "id": "32",
        "username": "test123",
        "email": "test@faceduck.com",
        "name": "Scrum",
        "surname": "Master",
        "birthday": "1984-10-01",
        "gender": "male"
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
    "title": "Get admins error",
    "type": "object",
    "properties": {
        "error-id": {
            "type": "string",
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
}
```

### Response: server error

`500 Internal Server Error`

## Update User Role

### Request

**PUT** `/group/{group_id}/members`

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
    "title": "Update user role",
    "type": "object",
    "properties": {
        "user_id": {"type": "string"},
        "admin":{"type": "boolean"}
    },
    "required": [
        "user_id",
        "admin"
    ]
}
```

*Examples:*

```json
{
    "user_id" : "23",
    "admin" : true
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
    "title": "update user role error",
    "type": "object",
    "properties": {
        "error-id": {
            "type": "string",
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

## Get group user

### Request

**GET** `/group/{group_id}/members/{user_id}`


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
    "title": "Get group user success",
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
```

*Examples:*

```json
{
    "id": "32",
    "username": "test123",
    "email": "test@faceduck.com",
    "name": "Scrum",
    "surname": "Master",
    "birthday": "1984-10-01",
    "gender": "male"
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
    "title": "Get group user error",
    "type": "object",
    "properties": {
        "error-id": {
            "type": "string",
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
}
```

### Response: server error

`500 Internal Server Error`

## Delete Group User

### Request

**DELETE** `/group/{group_id}/members/{user_id}`

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
    "title": "Delete group user error",
    "type": "object",
    "properties": {
        "error-id": {
            "type": "string",
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
