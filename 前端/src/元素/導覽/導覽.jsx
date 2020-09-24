
import React from 'react';
import Debug from 'debug';
import 音檔 from './音檔';
import './導覽.css';

var debug = Debug('kaxabu:導覽');

export default class 導覽 extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      關鍵字: '',
    };
  }

  componentWillReceiveProps(nextProps) {
    let 關鍵字 = nextProps.關鍵字;
    if (關鍵字 !== this.state.關鍵字) {
      this.setState({ 關鍵字 });
    }
  }

  搜尋(evt) {
    evt.preventDefault();
    this.props.跳到查詞(this.state.關鍵字);
    return;
  }

  輸入(e) {
    debug(e);
    this.setState({ 關鍵字: e.target.value });
  }

  render() {
    debug(this.props.關鍵字);
    debug(this.state.關鍵字);
    return (
        <div className="ui text container">
          <form onSubmit={this.搜尋.bind(this)}>
            <div className='ui action input'>
              <input id='關鍵字' placeholder='輸入關鍵字……'
                value={this.state.關鍵字 || ''}
                onChange={this.輸入.bind(this)}/>
              <button type='submit' className='ui button'>搜尋</button>
            </div>
          </form>
          <音檔 語詞編號={this.props.語詞編號} 內容={this.props.內容}/>
        </div>
      );
  }
}
