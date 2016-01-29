
import React from 'react';
import {render} from 'react-dom';
import Router, {Route, IndexRoute} from 'react-router';
import 網站 from './網站/網站';
import 查 from './頁/查/查';
import createBrowserHistory from 'history/lib/createBrowserHistory';
import './app.css';

import Debug from 'debug';
Debug.enable('kaxabu:*');

const root = document.getElementById('app');

//if (window.location.pathname === '/') {
//render(<HuanGing/>, root)
//} else {
let history = createBrowserHistory();
render(
  <Router history={history}>
          <Route path='/' component={網站}>
              <IndexRoute component={查}/>
              <Route path='/(:word)' component={查}/>
          </Route>
      </Router>, root);

//}
