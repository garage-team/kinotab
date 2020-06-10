import { combineReducers } from 'redux';
import {
    CHANGE_USER_NAME,
    CHANGE_PASSWORD,
    CHANGE_CONFIRM_PASSWORD,
    CLEAR_INPUT
} from './constants';
import { REQUEST_STATUS } from '../mainPage/constants';
import { iPayloadedAction } from '../interface';

const usernameInput = (state = '', action: iPayloadedAction): string => {
    switch (action.type) {
        case CHANGE_USER_NAME:
            return action.payload;
        case CLEAR_INPUT:
            return state = '';
        default:
            return state;
    }
};
const passwordInput = (state = '', action: iPayloadedAction): string => {
    switch (action.type) {
        case CHANGE_PASSWORD:
            return action.payload;
        case CLEAR_INPUT:
            return state = '';
        case REQUEST_STATUS:
            return state = '';
        default:
            return state;
    }
};

const confirmPasswordInput = (state = '', action: iPayloadedAction): string => {
    switch (action.type) {
        case CHANGE_CONFIRM_PASSWORD:
            return action.payload;
        case CLEAR_INPUT:
            return state = '';
        case REQUEST_STATUS:
            return state = '';
        default:
            return state;
    }
};

export const authorization = combineReducers({
    usernameInput,
    passwordInput,
    confirmPasswordInput
});