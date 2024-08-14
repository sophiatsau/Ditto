# DITTO
Practice your English with an AI chatbot!

## Live Link
https://ditto-wur4.onrender.com

<!-- ## Tech Stack -->

## Index
<!-- [Feature Lists]
[Database Schema]
[Store Shape]
[User Stories]
[Screenshots] -->
[Endpoints](github.com/sophiatsau/Ditto?tab=readme-ov-file#endpoints)

<!-- ## Screenshots -->

## Endpoints
### Auth
| Request | Purpose | Return Value | Status |
| :------ | :------ | :----------- | :----- |
| GET /api/auth/ | On initial load and subsequent refreshes, confirms if a user is authenticated and returns logged in user if there is one. | {<br/>&nbsp;&nbsp;"id": INT,<br/>&nbsp;&nbsp;"username": STRING,<br/>&nbsp;&nbsp;"email": STRING,<br/>&nbsp;&nbsp;"conversations": [ARRAY of INT]<br/>} | 200 |
| POST /api/auth/login | Logs user in and returns current user. | {<br/>&nbsp;&nbsp;"id": INT,<br/>&nbsp;&nbsp;"username": STRING,<br/>&nbsp;&nbsp;"email": STRING,<br/>&nbsp;&nbsp;"conversations": [ARRAY of INT]<br/>} | 200 |
| GET /api/auth/logout | Logs current user out. | {<br/>&nbsp;&nbsp;"message": "User logged out"<br/>} | 200 |
| POST /api/auth/signup | Creates a new user, logs them in, and returns newly created current user. | {<br/>&nbsp;&nbsp;"id": INT,<br/>&nbsp;&nbsp;"username": STRING,<br/>&nbsp;&nbsp;"email": STRING,<br/>&nbsp;&nbsp;"conversations": [ARRAY of INT]<br/>} | 201 |

### Chats
| Request | Purpose | Return Value | Status |
| :------ | :------ | :----------- | :----- |
| GET /api/chats/:chatId | Queries for and returns conversation by id. | ```json
{
"conversation": INT,<br/>&nbsp;&nbsp;"username": STRING,<br/>&nbsp;&nbsp;"email": STRING,<br/>&nbsp;&nbsp;"conversations": [ARRAY of INT]<br/>
}
``` | 200 |

<!-- ## Connect With Us! -->