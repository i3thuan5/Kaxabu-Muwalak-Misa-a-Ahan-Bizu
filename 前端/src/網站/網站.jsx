import React from 'react';
import { withRouter } from 'react-router-dom'
import superagent from 'superagent-bluebird-promise'
import 導覽 from '../元素/導覽/導覽';
import 全部詞條 from '../元素/詞條/全部詞條';
import 詞條區塊 from '../元素/詞條區塊/詞條區塊';
import PlayerMenu from '../PlayerMenu'
import { ImtongBangtsi, TshaBangTshi } from '../後端'

class BangTsam extends React.Component {

  constructor (props) {
    super(props);
    this.state = {
      關鍵字: this.props.match.params.word || '',
      辭典資料: [],
      imtong: {
        pianho: '',
        gi: '',
        lueiong:'',
        url: '',
      },
      showPlayerMenu: false,
    };
  }

  togglePlayerMenu = () => {
    this.setState({showPlayerMenu: !this.state.showPlayerMenu})
  }

  openPlayerMenu = () => {
    this.setState({showPlayerMenu: true})    
  }

  closePlayerMenu = () => {
    this.setState({showPlayerMenu: false, imtong: {
        pianho: '',
        gi: '',
        lueiong:'',
        url: '',
      }
    })
  }

  換音檔 = (pianho, gi, lueiong) => {
    let { imtong } = this.state
    if(pianho == imtong.pianho && lueiong == imtong.lueiong){
      this.togglePlayerMenu()
      return
    }
    this.openPlayerMenu()
    let url = ImtongBangtsi(pianho, gi)
    this.setState({imtong: {pianho, gi, lueiong, url}});
  }

  clearTshiauTshue = (關鍵字) => {
    this.setState({ 關鍵字 })
  }

  updateBangTsi = (關鍵字) => {
    this.props.history.push({pathname: '/' + 關鍵字});
  }

  getSutian = (關鍵字) => {
    superagent.get(TshaBangTshi())
      .query({ 關鍵字 })
      .then(({ body }) => (
        this.setState({辭典資料: body.符合資料})
      ))
      .catch((err) => ({ '符合資料':[] }));
  }

  tsha = (關鍵字) => {
    this.clearTshiauTshue(關鍵字)
    this.updateBangTsi(關鍵字)
    this.getSutian(關鍵字)
  }

  componentWillMount () {
    this.tsha(this.state.關鍵字)
  }

  render () {
    let { 關鍵字, 辭典資料, imtong, showPlayerMenu } = this.state

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

            <導覽
                kuankianji={關鍵字}
                跳到查詞={this.tsha}
            />
            <全部詞條
              pianho={imtong.pianho}
              換音檔={this.換音檔.bind(this)}
              辭典資料={辭典資料}
            />
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
            imtong={imtong}
            handleClose={this.closePlayerMenu}
          />
        </div>
      );
  }
}


export default withRouter(BangTsam)