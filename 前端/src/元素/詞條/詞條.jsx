
import React from 'react';
import Debug from 'debug';

var debug = Debug('kaxabu:詞條');

export default class 詞條 extends React.Component {

  點編號(編號) {
    let found = 編號.match(/([\dA-Z]+)-([\dA-Z]+)/i);
    debug(found);
    let index = found[1];
    if (index) {
      this.props.跳到查詞(index);
    }
  }

  點音檔(內容, c)
  {
    debug(內容);
    this.props.換音檔(this.props.資料.語詞編號, 內容);
  }

  render () {
    let { 資料 } = this.props;

    return (
        <tr>
            <td><a href='#!' onClick={this.點編號.bind(this, 資料.語詞編號)}>{資料.語詞編號}</a></td>
            <td><a href='#!' onClick={this.點音檔.bind(this, '噶哈巫')}>{資料.噶哈巫語教材標記法}</a></td>
            <td><a href='#!' onClick={this.點音檔.bind(this, '噶哈巫')}>{資料.噶哈巫語潘永歷標記法}</a></td>
            <td><a href='#!' onClick={this.點音檔.bind(this, '華語')}>{資料.中文譯解}</a></td>
            <td><a href='#!' onClick={this.點音檔.bind(this, '臺語')}>{資料.臺語譯解}</a></td>
            <td>{資料.備註}</td>
            <td>{資料.出處}</td>
        </tr>
      );
  }
}
