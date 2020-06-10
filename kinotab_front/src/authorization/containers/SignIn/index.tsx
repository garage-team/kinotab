import * as React from "react";
import { PureComponent } from 'react';
import { connect } from 'react-redux';
import { AnyAction, bindActionCreators, Dispatch } from 'redux';
import { iAuthorizationDomain } from '../../interfaces';
import { iStore } from '../../../interface';
import {
    changeUserName,
    changePassword,
    loginRequest,
    clearInput
} from '../../actions';
import { Login } from '../../components/Login/index';

const mapStateToProps = (state: iStore): iAuthorizationDomain => ({
    usernameInput: state.authorization.usernameInput,
    passwordInput: state.authorization.passwordInput,
    confirmPasswordInput: state.authorization.confirmPasswordInput,
});

interface iAuthorizationDispatchProps {
    changeUserName: (value: string) => void;
    changePassword: (value: string) => void;
    loginRequest: () => void;
    clearInput: () => void;
}

const mapDispatchToProps = (dispatch: Dispatch<AnyAction>): iAuthorizationDispatchProps =>
  bindActionCreators(
    {
        changeUserName,
        changePassword,
        loginRequest,
        clearInput
    },
    dispatch
  );

class SignIn extends PureComponent<ReturnType<typeof mapStateToProps> & ReturnType<typeof mapDispatchToProps>, {}> {
    public componentWillMount() {
        this.props.clearInput();
    }

    public render() {
        return (
            <div className="forms">
                <Login {...this.props}/>
            </div>
        )
    }
}

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(SignIn);