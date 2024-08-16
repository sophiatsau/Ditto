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
| GET /api/chats/:chatId | Queries for and returns conversation by id. | {<br/>&nbsp;&nbsp;"conversation": {<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"id": INT,<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"user_id": INT,<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"system_instructions": STRING,<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"history": [ARRAY of MESSAGE OBJ]<br/>&nbsp;&nbsp;}<br/>} | 200 |
| POST /api/chats/new | Creates a new conversation and returns the conversation. | {<br/>&nbsp;&nbsp;"conversation": {<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"id": INT,<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"user_id": INT,<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"system_instructions": STRING,<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"history": []<br/>&nbsp;&nbsp;}<br/>} | 200 |
| DELETE /api/chats/:chatId/delete | Deletes a conversation and returns a message if successfully deleted. | {<br/>&nbsp;&nbsp;"message": "Address successfully deleted."<br/>} | 200 |

### Messages
| Request | Purpose | Return Value | Status |
| :------ | :------ | :----------- | :----- |
| POST /api/chats/:chatId/send | Obtains a response from the model based on user's message. Creates two new messages in the conversation, one from the user's message and one from the model's response, and returns both. | {<br/>&nbsp;&nbsp;"messages": [{<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"id": INT,<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"role": "user",<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"parts": [STRING]<br/>&nbsp;&nbsp;}, {<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"id": INT,<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"role": "model",<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"parts": [STRING]<br/>&nbsp;&nbsp;}]<br/>} | 201 |

### Feedback Bots
| Request | Purpose | Return Value | Status |
| :------ | :------ | :----------- | :----- |
| GET /api/chats/grammar/:msgId | Check grammar for a specific message and return analysis of message's grammar. | {<br/>&nbsp;&nbsp;"errors_present": BOOL,<br/>&nbsp;&nbsp;"corrected_message": STRING,<br/>&nbsp;&nbsp;"explanation": STRING<br/>} | 200 |
| GET /api/chats/message/:msgId/definition/:word | Return definition of a specific word as used in the context of a message. | {<br/>&nbsp;&nbsp;"definition": STRING,<br/>&nbsp;&nbsp;"part_of_speech": STRING,<br/>&nbsp;&nbsp;"example_sentence": STRING<br/>} | 200 |
| GET /api/chats/:chatId/message/:msgId/social | Return analysis of social appropriateness of a specific message in the context of the conversation. | {"response": STRING<br/>} | 200 |
| GET /api/chats/:chatId/message/:msgId/response | Generate and return an example response for a specific message in context of the conversation. | {<br/>&nbsp;&nbsp;"example_response": STRING,<br/>&nbsp;&nbsp;"explanation": STRING<br/>} | 200 |

<!-- ## Connect With Us! -->
