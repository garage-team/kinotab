import { iPayloadedAction, iStore } from '../interface';
import { REQUEST_STATUS, DELETE_MESSAGE, ADD_CURRENT_TOKEN } from './constants';

export const statusMessage = (message: any): iPayloadedAction => ({
    type: REQUEST_STATUS,
    payload: message
});

export const deleteMessage = (): iPayloadedAction => ({
    type: DELETE_MESSAGE
});

const addCurrentToken = (token: string): iPayloadedAction => ({
    type: ADD_CURRENT_TOKEN,
    payload: token
});

export const redirect = (path: string) =>
    (dispatch: Function): void => {
       
    };

export const checkLocalStorage = () =>
    (dispatch: Function, getState: () => iStore): void => {
   
    };

export const logOut = () =>
    (dispatch: Function): void => {
 
    };

export const addToken = (token: string) =>
    (dispatch: Function): void => {
   
    };


