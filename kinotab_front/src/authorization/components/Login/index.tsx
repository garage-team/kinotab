import * as React from 'react';
import { iAuthorizationProps } from '../../interfaces';

interface iLoginProps extends iAuthorizationProps {
    loginRequest: () => void;
}

export class Login extends React.Component<iLoginProps> {
    public render() {
        const { usernameInput, passwordInput, loginRequest, changeUserName, changePassword } = this.props;
        return (
            <div>
                <h1>Login</h1>
                <form
                    onSubmit={(e) => {
                          e.preventDefault();
                          loginRequest();
                      }}>
                    <input placeholder="You name" required type="text"
                           value={usernameInput}
                           onChange={(e) => changeUserName((e.target as HTMLInputElement).value)}/>
                    <input placeholder="You password" required type="password"
                           value={passwordInput}
                           onChange={(e) => changePassword((e.target as HTMLInputElement).value)}/>
                    <button>Sign in</button>
                </form>
            </div>
        )
    }
}