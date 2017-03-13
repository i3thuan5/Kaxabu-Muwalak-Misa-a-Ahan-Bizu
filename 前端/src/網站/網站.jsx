import React from 'react';
import Router from 'react-router';
import 導覽 from '../元素/導覽/導覽';
import 全部詞條 from '../元素/詞條/全部詞條';
import Debug from 'debug';

var debug = Debug('kaxabu:網站');

export default class 網站 extends React.Component {

  constructor (props) {
    super(props);
    this.state = {
      關鍵字:props.params.word || '',
      語詞編號: '',
      內容:'',
    };
  }

  跳到查詞 (關鍵字) {
    this.setState({ 關鍵字:關鍵字, 語詞編號:'', 內容:'' });
    this.props.history.replaceState(null,    '/' + 關鍵字);
  }

  換音檔(語詞編號, 內容)
  {
    this.setState({ 語詞編號, 內容 });
  }

  render () {
    return (
        <div className='app background'>
          <header className='app header'>
            <導覽
              跳到查詞={this.跳到查詞.bind(this)}
              關鍵字={this.state.關鍵字}
              語詞編號={this.state.語詞編號}
              內容={this.state.內容}/>
          </header>
          <全部詞條
            換音檔={this.換音檔.bind(this)}
            variables={{ 關鍵字: this.state.關鍵字 }}/>
          <footer className='app footer inverted'>
            <ul className='ui menu container inverted'>
              <li className='item'><a href='https://www.facebook.com/events/1662129040716123/'>新書發表會暨使用說明會</a></li>
              <li className='item'><a href='https://www.facebook.com/kaxabu/?fref=ts'>埔里四庄番-噶哈巫族FB</a></li>
              <li className='item'><a href='https://github.com/Taiwanese-Corpus/kaxabu-muwalak-misa-a-ahan-bizu/blob/master/README.md'>網站資訊</a></li>
              <li className='item'><a href='https://github.com/Taiwanese-Corpus/kaxabu-muwalak-misa-a-ahan-bizu'>Github</a></li>
            </ul>
          </footer>
        </div>
      );
  }
}
