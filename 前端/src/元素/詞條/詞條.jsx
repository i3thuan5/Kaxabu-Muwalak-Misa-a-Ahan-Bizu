import React from 'react';

export default class 詞條 extends React.Component {
  
  點音檔(內容, c)
  {
    this.props.換音檔(this.props.資料.語詞編號, 內容);
  }

  render () {
    let { 資料 } = this.props;

    return (
        <tr>
            <td>{資料.語詞編號}</td>
            <td className="selectable">
              <a href='#!' onClick={this.點音檔.bind(this, '噶哈巫')}
              >{資料.噶哈巫語教材標記法}</a></td>
            <td className="selectable">
              <a href='#!' onClick={this.點音檔.bind(this, '噶哈巫')}
              >{資料.噶哈巫語潘永歷標記法}</a></td>
            <td className="selectable">
              <a href='#!' onClick={this.點音檔.bind(this, '華語')}
              >{資料.中文譯解}</a></td>
            <td className="selectable">
              <a href='#!' onClick={this.點音檔.bind(this, '臺語')}
              >{資料.臺語譯解}</a></td>
            <td>{資料.備註}</td>
            <td>{資料.出處}</td>
        </tr>
      );
  }
}
