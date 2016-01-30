
import React from 'react';
import Transmit from 'react-transmit';
import {Link} from 'react-router';
import superagent from 'superagent-bluebird-promise';
import Debug from 'debug';

var debug = Debug('kaxabu:詞條');

class 詞條 extends React.Component {

  componentWillMount () { this.props.setQueryParams(this.props); }

  componentWillReceiveProps (nextProps) {
    if (nextProps.params === this.props.params) return;
    this.props.setQueryParams(nextProps);
  }
  點音檔(內容,c)
  {
    debug(內容)
    this.props.換音檔(this.props.資料.語詞編號,內容)
  }
  render () {
    let {資料} = this.props
// onClick={this.props.換音檔.bind(this)}
    return (
        <tr>
            <td><a href='javascript:void(0)' onClick={this.點音檔.bind(this,'語詞編號')}>{資料.語詞編號}</a></td>
            <td><a href='javascript:void(0)' onClick={this.點音檔.bind(this,'噶哈巫')}>{資料.噶哈巫語教材標記法}</a></td>
            <td><a href='javascript:void(0)' onClick={this.點音檔.bind(this,'噶哈巫')}>{資料.噶哈巫語潘永歷標記法}</a></td>
            <td><a href='javascript:void(0)' onClick={this.點音檔.bind(this,'華語')}>{資料.中文譯解}</a></td>
            <td><a href='javascript:void(0)' onClick={this.點音檔.bind(this,'臺語')}>{資料.臺語譯解}</a></td>
            <td>{資料.備註}</td>
            <td>{資料.出處}</td>
        </tr>
      );
  }
}

export default Transmit.createContainer(詞條, {
  queries: {
  },
});
