
import React from 'react';
import Transmit from 'react-transmit';
import {Link} from 'react-router';
import './導覽.css';
import 音檔 from './音檔';


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
            Kaxabu Muwalak Misa A Ahan Bizu<br/>
            噶哈巫語分類辭典
        </h1>
        <input id='關鍵字' placeholder='輸入關鍵字……'
          defaultValue={this.props.關鍵字} onKeyUp={this.更新詞.bind(this)} /> 
        <音檔 後端網址={this.props.後端網址} 語詞編號={this.props.語詞編號} 內容={this.props.內容}/>
       </div>
      );
  }
}

export default Transmit.createContainer(ToLam, { query: {} });
