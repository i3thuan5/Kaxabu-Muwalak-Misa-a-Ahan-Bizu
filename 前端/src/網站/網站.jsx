import React from 'react';
import Transmit from 'react-transmit';
import Router from 'react-router';

import 導覽 from '../元素/導覽/導覽';
import 全部詞條 from '../元素/詞條/全部詞條';

class 網站 extends React.Component {

  constructor (props) {
    super(props);
    this.state = {
      後端網址: 'http://localhost:8000/',
      關鍵字:props.params.word || '',
    };
  }

  跳到查詞 (關鍵字) {
    this.setState({ 關鍵字 });
    this.props.history.replaceState(null,    '/' + 關鍵字);
  }

  render () {
    return (
        <div className='app background'>
          <header className='app header'>
            <導覽 跳到查詞={this.跳到查詞.bind(this)} 關鍵字={this.state.關鍵字}/>
          </header>
          <全部詞條 後端網址={this.state.後端網址} 關鍵字={this.state.關鍵字}/>
          <footer className='app footer inverted'>
            <ul className='ui menu container inverted'>
              <li className='item'><a href='https://github.com/Taiwanese-Corpus/kaxabu_muwalak_misa_a_ahan_bizu'>GitHub</a></li>
            </ul> 
                                                                                                                                                                                                                                                                                                                                </footer>
        </div>
      );
  }
}

export default Transmit.createContainer(網站, { queries: {} });
