# User Model 
### Proposal
```
{
    "email" : "string",
    "password" : {
        "type": "string", 
        "minLength": 4,
    },

    "details" : {
        "name" : "string",
        "surname" : "string",
        "gender" : "string",
        "profileImagePath" : "string",
        "birth" : "string",
        "age" : "number",
        "isAdult" : "boolean",
        "location" : "string",
        "description" : "string",
        "url" : "string",
        "friendsCount" : "number",
        "postsCount" : "number",
        "registerDate" : "string",
        "phone" : "number",
        "website" : "string",
        "friends" : {
            "type" : "nested"
        }
    }
    
}
```
### Example
```
{
    "email" : "testuser@test.com",
    "password" : "HQSfFrasQWER23",

    "details" : {
        "name" : "Test",
        "surname" : "User",
        "gender" : "Male",
        "profileImagePath" : "/usrs/testuser",
        "birth" : "30/10/1974",
        "age" : 44,
        "isAdult" : "True",
        "location" : "Barcelona, Spain",
        "description" : "Hi, I'm Test and I'm trying out this new social network",
        "url" : "http://www.faceduck.com/user/testuser",
        "friendsCount" : 2,
        "postsCount" : 0,
        "registerDate" : "24/09/2018",
        "phone" : "7777777777",
        "website" : "www.testwebsite.com",
        "friends" : [
            {
                "name" : "Madame",
                "surname" : "Test",
                "email" : "madametest@test.com"
            },
            {
                "name" : "Monsieur",
                "surname" : "Test",
                "email" : "monsieurtest@test.com"
            }
        ]
    }
}
```
