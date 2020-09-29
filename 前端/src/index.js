
import React from 'react';
import {render} from 'react-dom';
import { BrowserRouter, Switch, Route } from "react-router-dom";
import 網站 from './網站/網站';
import './app.css';

import Debug from 'debug';
Debug.enable('kaxabu:*');

const root = document.getElementById('app');

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
