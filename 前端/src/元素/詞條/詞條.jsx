
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

  render () {
    let 合成音檔 = document.getElementById('合成音檔')

    return (
        <div className='main container'>
        <h3>詞條：</h3>
        </div>
      );
  }
}

export default Transmit.createContainer(詞條, {
  queries: {
  },
});
