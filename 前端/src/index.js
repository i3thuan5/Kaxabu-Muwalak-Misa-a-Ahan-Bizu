
import React from 'react';
import {render} from 'react-dom';
// import Router, {Route, IndexRoute} from 'react-router';
import { BrowserRouter, Switch, Route } from "react-router-dom";
import 網站 from './網站/網站';
// import createBrowserHistory from 'history/lib/createBrowserHistory';
import './app.css';

import Debug from 'debug';
Debug.enable('kaxabu:*');

const root = document.getElementById('app');

// let history = createBrowserHistory();
// render(
//   <Router history={history}>
//           <Route path='/' component={網站}>
//               <IndexRoute/>
//               <Route path='/(:word)'/>
//           </Route>
//       </Router>, root
// );

render(
	<BrowserRouter>
		<Switch>
			<Route exact path='/'>
				<網站/>
			</Route>
			<Route path='/:word'>
				<網站/>
			</Route>
		</Switch>
	</BrowserRouter>, root
)