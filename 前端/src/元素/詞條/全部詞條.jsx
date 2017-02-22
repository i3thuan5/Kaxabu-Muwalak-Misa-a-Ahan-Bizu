
import React from 'react';
import Transmit from 'react-transmit';
import superagent from 'superagent-bluebird-promise';
import Debug from 'debug';
import 詞條 from './詞條';
import 詞條標題 from './詞條標題';

var debug = Debug('kaxabu:全部詞條');

class 全部詞條 extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      全開: this.預設顯示幾个(),
    };
  }

  componentWillMount() {
    this.props.transmit.forceFetch(this.props);
  }

  componentWillReceiveProps (nextProps) {
    if (nextProps.關鍵字 === this.props.關鍵字) return;
    this.props.transmit.forceFetch(nextProps);
    this.setState({ 全開: this.預設顯示幾个() });
  }

  預設顯示幾个() {
    return 200;
  }

  看閣較濟全開() {
    let { 全開 } = this.state;
    全開 += this.預設顯示幾个();
    this.setState({ 全開 });
  }

  看閣較濟() {
    if (this.props.辭典資料.符合資料.length > this.state.全開)
    return (
          <button onClick={this.看閣較濟全開.bind(this)}
            className='ui icon button'>
            再顯示多一點
          </button>
      );
  }

  render () {
    let { 全開 } = this.state;
    let 詞條陣列 = this.props.辭典資料.符合資料.slice(0, 全開).map((資料)=>(
     <詞條 key={資料.語詞編號} 資料={資料} 換音檔={this.props.換音檔}/>)
    );
    return (
        <div className='main container'>
            <table>
                <tbody>
                  <詞條標題/>
                  {詞條陣列}
                </tbody>
            </table>
            {this.看閣較濟()}
        </div>
          );
  }
}

export default Transmit.createContainer(全部詞條, {
  initialVariables: {
    後端網址: undefined,
    關鍵字: null,
  },
  fragments: {
    辭典資料({ 後端網址, 關鍵字 }) {
      if (後端網址 === undefined) {
        return Promise.resolve({ '符合資料':[{ '語詞編號':'載入中……' }] });
      }

      return superagent.get(後端網址 + '查')
          .query({ 關鍵字 })
          .then(({ body }) => (
            body
          ))
          .catch((err) => ({ '符合資料':[] }));
    },
  },
});
