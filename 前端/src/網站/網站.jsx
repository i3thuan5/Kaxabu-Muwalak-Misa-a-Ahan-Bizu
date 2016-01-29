import React from 'react';
import Transmit from 'react-transmit';
import Router from 'react-router';

import ToLam from '../元素/導覽/導覽';

class 網站 extends React.Component {

  constructor (props) {
    super(props);
    this.state = {
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
            <ToLam/>
          </header>
          {React.cloneElement(this.props.children,
            { 後端網址: 'http://localhost:8000/',
            跳到查詞: this.跳到查詞.bind(this),
            關鍵字: this.state.關鍵字,
            }
          )}
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
