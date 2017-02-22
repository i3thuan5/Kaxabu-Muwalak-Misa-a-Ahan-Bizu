
import React from 'react';
import superagent from 'superagent-bluebird-promise';
import Debug from 'debug';

var debug = Debug('kaxabu:音檔');

class 音檔 extends React.Component {

  componentDidUpdate()
  {
    let 音檔 = document.getElementById('音檔');
    音檔.load();

    //音檔.play();
  }

  render () {
    let { 後端網址, 語詞編號, 內容 } = this.props;
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
        <div>請選擇音檔！！</div>
        );
    }
  }
}
