
import React from 'react';
import Debug from 'debug';
import 音檔 from './音檔';
import './導覽.css';

var debug = Debug('kaxabu:導覽');

export default class 導覽 extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      關鍵字: '',
    };
  }

  更新詞(evt) {
    if (evt.keyCode === 13) {
      let 關鍵字 = this.refs.Tshue.value;
      if (關鍵字 !== this.state.關鍵字) {
        debug('更新詞');
        this.setState({ 關鍵字 });
        this.props.跳到查詞(關鍵字);
      }
    }

    return;
  }

  render() {
    return (
      <div className='app bar container'>
        <h1 className='title'>
            Kaxabu Muwalak Misa A Ahan Bizu<br/>
            噶哈巫語分類辭典
        </h1>
        <div className='fixed'>
          <div className='ui input'>
          <input id='關鍵字' placeholder='輸入關鍵字……'
            defaultValue={this.props.關鍵字}
            onKeyDown={this.更新詞.bind(this)}
            ref='Tshue' />
          </div>
          <音檔 語詞編號={this.props.語詞編號} 內容={this.props.內容}/>
        </div>
        </div>
      );
  }
}
