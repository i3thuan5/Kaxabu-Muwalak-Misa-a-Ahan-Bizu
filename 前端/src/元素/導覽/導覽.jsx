
import React from 'react';
import Transmit from 'react-transmit';
import {Link} from 'react-router';
import './導覽.css';

class ToLam extends React.Component {
  更新詞(e)
  {
    let 關鍵字 = e.target.value;
    this.props.跳到查詞(關鍵字);
  }

  render () {
    return (
      <div className='app bar container'>
        <h1 className='title'>
          <Link to='/'>
            Kaxabu分類辭典
            </Link>
        </h1>
        <input id='關鍵字' placeholder='輸入關鍵字……'
          defaultValue={this.props.關鍵字} onKeyUp={this.更新詞.bind(this)} /> 
                                                                                                                                                                                                </div>
      );
  }
}

export default Transmit.createContainer(ToLam, { query: {} });
