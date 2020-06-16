import { iStore, iPayloadedAction } from '../interface';
import {
    CHANGE_USER_NAME,
    CHANGE_PASSWORD,
    CHANGE_CONFIRM_PASSWORD,
    CLEAR_INPUT
} from './constants';
import { redirect } from '../mainPage/actions'
import { statusMessage } from '../mainPage/actions'
import { addToken } from '../mainPage/actions'

declare const fetch: any;

export const clearInput = (): iPayloadedAction => ({
    type: CLEAR_INPUT,
});

export const changeUserName = (userNameInput: string): iPayloadedAction => ({ 
    type: CHANGE_USER_NAME,
    payload: userNameInput
});

export const changePassword = (passwordInput: string): iPayloadedAction => ({
    type: CHANGE_PASSWORD,
    payload: passwordInput
});

export const changeConfirmPassword = (confirmPasswordInput: string): iPayloadedAction => ({
    type: CHANGE_CONFIRM_PASSWORD,
    payload: confirmPasswordInput
});

export const loginRequest = () =>
    (dispatch: Function, getState: () => iStore) => {

    };

const registrationRequest = () =>
    (dispatch: Function, getState: () => iStore) => {

    };

export const checkConfirmPassword = () =>
    (dispatch: Function, getState: () => iStore) => {

    };
