
import React from 'react';
import {後端網址} from '../../後端';

export default class 音檔 extends React.Component {

  componentDidUpdate()
  {
    let 音檔 = document.getElementById('音檔');
    if (音檔) {
      音檔.load();
    }
  }

  render () {
    let { 語詞編號, 內容 } = this.props;
    console.log('語詞編號, 內容:', 語詞編號, 內容)
    if (語詞編號 != '' && 內容 != '')
    {
      return (
        <audio id='音檔' controls autoPlay>
           <source src={後端網址 + '聽?語詞編號=' + 語詞編號 + '&內容=' + 內容} type="audio/wav"/>
        </audio>
      );
    }
    return null
  }
}
