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
| GET /api/auth/login | On initial load and subsequent refreshes, confirms if a user is authenticated and returns logged in user if there is one. | {<br/>&nbsp;&nbsp;"id": INT,<br/>&nbsp;&nbsp;"username": STRING,<br/>&nbsp;&nbsp;"email": STRING,<br/>&nbsp;&nbsp;"conversations": [ARRAY of INT]<br/>} | 200 |

<!-- ## Connect With Us! -->