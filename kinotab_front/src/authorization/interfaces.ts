export interface iAuthorizationDomain {
    usernameInput: string;
    passwordInput: string;
    confirmPasswordInput: string;
}

export interface iAuthorizationProps {
    changeUserName: (value: string) => void;
    changePassword: (value: string) => void;
    usernameInput: string;
    passwordInput: string;
}