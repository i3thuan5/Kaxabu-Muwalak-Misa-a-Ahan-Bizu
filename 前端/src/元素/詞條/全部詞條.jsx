
import React from 'react';
import {Link} from 'react-router';
import Transmit from 'react-transmit';
import superagent from 'superagent-bluebird-promise';
import Debug from 'debug';
import 詞條 from '../../元素/詞條/詞條';

var debug = Debug('kaxabu:全部詞條');

class 全部詞條 extends React.Component {

  componentWillMount () { this.props.setQueryParams(this.props); }

  componentWillReceiveProps (nextProps) {
    if (nextProps.關鍵字 === this.props.關鍵字) return;
    this.props.setQueryParams(nextProps);
  }

  render () {
    debug(this.props.辭典資料)
    let 詞條陣列 = this.props.辭典資料.符合資料.map((a)=>(
        <詞條 後端網址={this.props.後端網址}/>)
      );
    return (
        <div className='main container'>
        {this.props.關鍵字}
        <br/>
         {詞條陣列}
        </div>
          );
  }
}

export default Transmit.createContainer(全部詞條, {
  queries: {
    辭典資料({ 後端網址, 關鍵字 }) {
      if (後端網址 === undefined)
        return Promise.resolve([]);
      return superagent.get(後端網址 + '查')
          .query({ 關鍵字 })
          .then(({ body }) => (
            body
          ))
          .catch((err) => (['發生錯誤']));
    },
  },
});
