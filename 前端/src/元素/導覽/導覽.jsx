
import React from 'react';
import Transmit from 'react-transmit';
import {Link} from 'react-router';
import './導覽.css';

class ToLam extends React.Component {
  render () {
    return (
      <div className='app bar container'>
        <h1 className='title segment'>
          <Link to='/'>
            Kaxabu分類辭典
          </Link>
        </h1>
        <div></div>
      </div>
      );
  }
}

export default Transmit.createContainer(ToLam, { query: {} });
