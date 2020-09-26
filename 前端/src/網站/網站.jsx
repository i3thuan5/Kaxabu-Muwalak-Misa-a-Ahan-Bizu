import React from 'react';
import { withRouter } from 'react-router-dom'
import { useTransition, animated } from 'react-spring' 
import 導覽 from '../元素/導覽/導覽';
import 全部詞條 from '../元素/詞條/全部詞條';
import 詞條區塊 from '../元素/詞條區塊/詞條區塊';
import PlayerMenu from '../PlayerMenu'
import { ImtongBangtsi } from '../後端';


class BangTsam extends React.Component {

  constructor (props) {
    super(props);
    this.state = {
      關鍵字: this.props.match.params.word || '',
      語詞編號: '',
      內容:'',
      url: '',
      showPlayerMenu: false,
    };
  }

  togglePlayer = () => {
    console.log('togglePlayer')
    this.setState({showPlayerMenu: !this.state.showPlayerMenu})
  }

  openPlayer = () => {
    this.setState({showPlayerMenu: true})    
  }

  closePlayer = () => {
    this.setState({showPlayerMenu: false})
  }

  換音檔(語詞編號, 內容)
  {
    console.log('語詞編號, 內容=', 語詞編號, 內容)
    if(語詞編號 == this.state.語詞編號 && 內容 == this.state.內容){
      this.togglePlayer()
      return
    }
    this.openPlayer()
    let url = ImtongBangtsi(語詞編號, 內容)
    console.log('url=', url)
    this.setState({語詞編號, 內容, url});
  }

  render () {
    let { showPlayerMenu, url } = this.state

    return (
        <div className='app site'>
          <div className='app main'>
          <header className='ui text container padded basic segment'>
            <h1 className='ui header'>
              Kaxabu Muwalak Misa A Ahan Bizu
              <div className='sub header'>噶哈巫語分類辭典</div>
            </h1>
            <div className="ui message">
            <i className='ui icon info'/>搜尋後，點擊你想聽的音標！！
            </div>
          </header>
          {/*<button onClick={this.togglePlayer}>Toogle</button>*/}

          <導覽
              關鍵字={this.state.關鍵字}
              語詞編號={this.state.語詞編號}
              內容={this.state.內容}/>
          <全部詞條
            換音檔={this.換音檔.bind(this)}
            variables={{關鍵字: this.state.關鍵字}}
            renderLoading={<詞條區塊/>}/>
          </div>

          <footer>
            <ul className='ui stackable inverted menu'>
              <li className='item'><a href='https://www.facebook.com/events/1662129040716123/'>新書發表會暨使用說明會</a></li>
              <li className='item'><a href='https://www.facebook.com/kaxabu/?fref=ts'>埔里四庄番-噶哈巫族FB</a></li>
              <li className='item'><a href='https://github.com/Taiwanese-Corpus/kaxabu-muwalak-misa-a-ahan-bizu/blob/master/README.md'>網站資訊</a></li>
              <li className='item'><a href='https://github.com/Taiwanese-Corpus/kaxabu-muwalak-misa-a-ahan-bizu'>Github</a></li>
            </ul>
          </footer>

          <PlayerMenu 
            showPlayerMenu={showPlayerMenu}
            handleClose={this.closePlayer}
            url={url}
          />
        </div>
      );
  }
}


export default withRouter(BangTsam)