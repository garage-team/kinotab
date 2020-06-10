import * as React from 'react';
import { iAuthorizationProps } from '../../interfaces';

interface iRegistrationProps extends iAuthorizationProps {
    checkConfirmPassword: () => void;
    confirmPasswordInput: string;
    changeConfirmPassword: (value: string) => void;
}

export class Registration extends React.Component<iRegistrationProps> {
    public render() {
        const { usernameInput, passwordInput, checkConfirmPassword, changeUserName, changePassword, confirmPasswordInput, changeConfirmPassword } = this.props;
        return (
            <div>
                <h1>Registration</h1>
                <form
                    onSubmit={(e) => {
                          e.preventDefault();
                          checkConfirmPassword();
                      }}>
                    <input placeholder="Your name" required type="text"
                           value={usernameInput}
                           onChange={(e) => changeUserName((e.target as HTMLInputElement).value)}/>
                    <input placeholder="Your password" required type="password"
                           value={passwordInput}
                           onChange={(e) => changePassword((e.target as HTMLInputElement).value)}/>
                    <input placeholder="Confirm password" required type="password"
                           value={confirmPasswordInput}
                           onChange={(e) => changeConfirmPassword((e.target as HTMLInputElement).value)}/>
                    <button>Sign up</button>
                </form>
            </div>
        )
    }
}