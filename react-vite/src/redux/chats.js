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
    if (response.ok) {
        const chat = await response.json();
        dispatch(loadChat(chat));
    }
};

const initialState = { chats: {} };

function chatReducer(state = initialState, action) {
  switch (action.type) {
    default:
      return state;
  }
}

export default chatReducer;