
import React from 'react';
import Transmit from 'react-transmit';
import {Link} from 'react-router';
import superagent from 'superagent-bluebird-promise';
import Debug from 'debug';

var debug = Debug('kaxabu:詞條標題');

class 詞條標題 extends React.Component {

  componentWillMount () { this.props.setQueryParams(this.props); }

  componentWillReceiveProps (nextProps) {
    if (nextProps.params === this.props.params) return;
    this.props.setQueryParams(nextProps);
  }

  render () {
    return (
        <tr>
            <th>語詞編號</th>
            <th>噶哈巫語教材標記法</th>
            <th>噶哈巫語潘永歷標記法</th>
            <th>中文譯解</th>
            <th>臺語譯解</th>
            <th>備註</th>
            <th>出處</th>
        </tr>
      );
  }
}

export default Transmit.createContainer(詞條標題, {
  queries: {
  },
});
