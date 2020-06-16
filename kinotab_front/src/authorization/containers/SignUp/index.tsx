import * as React from "react";
import { PureComponent } from 'react';
import { connect } from 'react-redux';
import { AnyAction, bindActionCreators, Dispatch } from 'redux';
import { iAuthorizationDomain } from '../../interfaces';
import { iStore } from '../../../interface';
import {
    changeUserName,
    changePassword,
    checkConfirmPassword,
    changeConfirmPassword,
    clearInput
} from '../../actions';
import { Registration } from '../../components/Registration/index';

const mapStateToProps = (state: iStore): iAuthorizationDomain => ({
    usernameInput: state.authorization.usernameInput,
    passwordInput: state.authorization.passwordInput,
    confirmPasswordInput: state.authorization.confirmPasswordInput,
});

interface iRegistrationDispatchProps {
    changeUserName: (value: string) => void;
    changeConfirmPassword: (value: string) => void;
    changePassword: (value: string) => void;
    checkConfirmPassword: () => void;
    clearInput: () => void;
}

const mapDispatchToProps = (dispatch: Dispatch<AnyAction>): iRegistrationDispatchProps =>
  bindActionCreators(
    {
        changeUserName,
        changePassword,
        changeConfirmPassword,
        checkConfirmPassword,
        clearInput
    },
    dispatch
  );

class SignUp extends PureComponent<ReturnType<typeof mapStateToProps> & ReturnType<typeof mapDispatchToProps>, {}> {
    public componentWillMount() {
        this.props.clearInput();
    }
    public render() {
        return (
            <div className="forms">
                <Registration {...this.props}/>
            </div>
        )
    }
}

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(SignUp);