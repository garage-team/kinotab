import { combineReducers } from 'redux';
import { iPayloadedAction } from '../interface';
import { REQUEST_STATUS, DELETE_MESSAGE, ADD_CURRENT_TOKEN } from './constants';

const statusMessage = (state = '', action: iPayloadedAction): string => {
    switch (action.type) {
        case REQUEST_STATUS:
            return state = action.payload;
        case DELETE_MESSAGE:
            return state = '';
        default:
            return state;
    }
};

const currentToken = (state = '', action: iPayloadedAction): string => {
    switch (action.type) {
        case ADD_CURRENT_TOKEN:
            return state = action.payload;
        default:
            return state;
    }
};

export const mainPage = combineReducers({
    statusMessage,
    currentToken
});