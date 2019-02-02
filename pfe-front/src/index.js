import React from 'react';
import ReactDOM from 'react-dom';
import { createBrowserHistory } from "history";
import "assets/css/material-dashboard-react.css?v=1.5.0";
import App from './App';
import * as serviceWorker from './serviceWorker';

const hist = createBrowserHistory();

ReactDOM.render(<App />, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
serviceWorker.unregister();
