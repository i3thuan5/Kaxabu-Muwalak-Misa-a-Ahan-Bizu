
import React from 'react';
import {Link} from 'react-router';
import Transmit from 'react-transmit';
import superagent from 'superagent-bluebird-promise';
import Debug from 'debug';
import 全部詞條 from '../../元素/詞條/全部詞條';

var debug = Debug('kaxabu:查');

class 查 extends React.Component {

  componentWillMount () { this.props.setQueryParams(this.props); }

  componentWillReceiveProps (nextProps) {
    if (nextProps.關鍵字 === this.props.關鍵字) return;
    this.props.setQueryParams(nextProps);
  }

  constructor (props) {
    super(props);
    this.state = {
      關鍵字:this.props.params.word || '',
    };
  }

  跳到查詞(e)
  {
    關鍵字 = e.target.value;
    debug(關鍵字)
    this.setState({ 關鍵字 });
    this.props.跳到查詞(關鍵字);
  }

  render () {
    let { 關鍵字 } = this.state;
    return (
        <div className='main container'>
        <input id='關鍵字' defaultValue={關鍵字} onKeyUp={this.跳到查詞.bind(this)} />
        <br/>
        <全部詞條 後端網址={this.props.後端網址} 關鍵字={關鍵字}/>
        </div>
          );
  }
}

export default Transmit.createContainer(查, {
  queries: {
  },
});
