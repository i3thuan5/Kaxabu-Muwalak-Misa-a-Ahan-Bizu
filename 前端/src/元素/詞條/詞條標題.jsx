
import React from 'react';
import Debug from 'debug';

var debug = Debug('kaxabu:詞條標題');

export default class 詞條標題 extends React.Component {

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
