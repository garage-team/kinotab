import * as React from "react";
import { PureComponent } from 'react';
import { connect } from 'react-redux';
import { AnyAction, bindActionCreators, Dispatch } from 'redux';
import { iMainPageDomain } from '../../interfaces';
import { iStore } from '../../../interface';
import {
    logOut,
    checkLocalStorage,
    deleteMessage
} from '../../actions';

const mapStateToProps = (state: iStore): iMainPageDomain => ({
    statusMessage: state.mainPage.statusMessage,
    currentToken: state.mainPage.currentToken,
});

interface iMainPageDispatchProps {
    logOut: () => void;
    deleteMessage: () => void;
    checkLocalStorage: () => void;
}

const mapDispatchToProps = (dispatch: Dispatch<AnyAction>): iMainPageDispatchProps =>
  bindActionCreators(
    {
        logOut,
        deleteMessage,
        checkLocalStorage
    },
    dispatch
  );

class MainPage extends PureComponent<ReturnType<typeof mapStateToProps> & ReturnType<typeof mapDispatchToProps>, {}> {
    public render() {
        return (
            <div>
                <h1>Kino Tab</h1>
                {/* {this.props.children} */}
            </div>
        )
    }
}

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(MainPage);