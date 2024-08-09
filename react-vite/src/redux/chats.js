const LOAD_CHAT = 'chats/LOAD_CHAT';
const START_CHAT = 'chat/START_CHAT';
const DELETE_CHAT = 'chat/DELETE_CHAT';
const SEND_MESSAGE = 'chat/SEND_MESSAGE';

const loadChat = (chat) => ({
    type: LOAD_CHAT,
    payload: chat
});

const startChat = (chat) => ({
    type: START_CHAT,
    payload: chat
});

const deleteChat = (chatId) => ({
    type: DELETE_CHAT,
    payload: chatId
});

const sendMessage = (message) => ({
    type: SEND_MESSAGE,
    payload: message
});

export const thunkLoadChat = (chatId) => async (dispatch) => {
    const response = await fetch(`/api/chats/${chatId}`);
    const data = await response.json();
    if (response.ok) {
        dispatch(loadChat(data.conversation));
    }
    return data;
};

export const thunkStartChat = (systemInstructions) => async (dispatch) => {
    const response = await fetch(`/api/chats/new`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ system_instructions: systemInstructions })
    });
    const data = await response.json();
    if (response.ok) {
        dispatch(startChat(data.conversation));
    }
    return data;
};

export const thunkDeleteChat = (chatId) => async (dispatch) => {
    const response = await fetch(`/api/chats/${chatId}`, {
        method: 'DELETE'
    });
    const data = await response.json();
    if (response.ok) {
        dispatch(deleteChat(chatId));
    }
    return data;
}

export const thunkSendMessage = (text) => async (dispatch) => {
    const response = await fetch(`/api/chats/${text.chat_id}/send`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(text)
    });
    const data = await response.json();
    if (response.ok) {
        dispatch(sendMessage(data));
    }
    return data;
}

const initialState = {};

function chatReducer(state = initialState, action) {
  switch (action.type) {
    case LOAD_CHAT: {
      return { ...state, [action.payload.id]: action.payload };
    }
    case START_CHAT: {
        return { ...state, [action.payload.id]: action.payload };
    }
    case DELETE_CHAT: {
        const newState = { ...state };
        delete newState[action.payload];
        return newState;
    }
    case SEND_MESSAGE: {
        const chatId = action.payload.conversation_id;
        const messages = [...state[action.payload.conversation_id].messages, ...action.payload.messages];
        const newState = { 
            ...state, 
            [chatId]: { ...state[chatId], messages} 
        };
        return newState;
    }
    default:
      return state;
  }
}

export default chatReducer;