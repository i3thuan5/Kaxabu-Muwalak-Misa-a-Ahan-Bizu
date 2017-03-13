
import React from 'react';
import Debug from 'debug';
import {後端網址} from '../../後端';

var debug = Debug('kaxabu:音檔');

export default class 音檔 extends React.Component {

  componentDidUpdate()
  {
    let 音檔 = document.getElementById('音檔');
    音檔.load();
  }

  render () {
    let { 語詞編號, 內容 } = this.props;
    if (語詞編號 != '' && 內容 != '')
    {
      return (
        <audio id='音檔' controls autoPlay>
           <source src={後端網址 + '聽?語詞編號=' + 語詞編號 + '&內容=' + 內容} type="audio/wav"/>
        </audio>
      );
    } else
    {
      return (
        <div className="ui message">
          <i className='ui icon info'/>搜尋後，點擊你想聽的音標！！
        </div>
      );
    }
  }
}
