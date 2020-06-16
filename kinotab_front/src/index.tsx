import * as React from "react";
import * as ReactDOM from "react-dom";
import { Provider } from 'react-redux';
import thunk from "redux-thunk";
import { BrowserRouter as Router, Route, Switch, Link } from 'react-router-dom';
import { applyMiddleware, createStore, compose, combineReducers } from 'redux';
import { mainPage } from './mainPage/reducers';
import { authorization } from './authorization/reducers';
import MainPage from './mainPage/containers/MainPage/index';
import SignUp from './authorization/containers/SignUp/index';
import SignIn from './authorization/containers/SignIn/index';
import './styles';

const AllReducers = combineReducers({
    mainPage,
    authorization
});

const store = createStore(AllReducers, compose(
    applyMiddleware(thunk)
));

ReactDOM.render(
    <Provider store={store}>
        <Router>
            <main className="app">
                <header className="header">
                    <Link to="/sign-up">SignUp</Link>
                    <Link to="/sign-in">SignIn</Link>
                </header>
                <Switch>
                    <Route exact path="/" component={MainPage} />
                    <Route exact path="/sign-up" component={SignUp} />
                    <Route path="/sign-in" component={SignIn} />
                </Switch>
            </main>
        </Router>
    </Provider>,
    document.getElementById("app")
);