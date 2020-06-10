import { Action } from "redux";
import { iMainPageDomain } from './mainPage/interfaces';
import { iAuthorizationDomain } from './authorization/interfaces';

export interface iStore {
    mainPage: iMainPageDomain;
    authorization: iAuthorizationDomain;
}

export interface iPayloadedAction extends Action {
    payload?: any;
}