import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';

window.CONFS = {
	apiServer: process.env.REACT_APP_WEB_API_SERVER
}
console.log('Use confs', window.CONFS);

ReactDOM.render(<App />, document.getElementById('root'));
registerServiceWorker();
