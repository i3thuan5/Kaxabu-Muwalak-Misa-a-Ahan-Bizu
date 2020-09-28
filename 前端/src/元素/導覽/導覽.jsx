import React from 'react';
import './導覽.css';

export default class 導覽 extends React.Component {
  constructor(props) {
    super(props);
    this.textInput = React.createRef();
  }

  搜尋(e) {
    e.preventDefault()
    let kuankianji = this.textInput.current.value
    this.props.跳到查詞(kuankianji)
    return;
  }

  render() {
    let { kuankianji } = this.props

    return (
        <div className="ui text container padded basic segment">
          <form onSubmit={this.搜尋.bind(this)}>
            <div className='ui fluid action input'>
              <input
                id='關鍵字'
                placeholder='輸入關鍵字……'
                defaultValue={kuankianji}
                ref={this.textInput}
              />
              <button type='submit' className='ui button'>查辭典</button>
            </div>
          </form>
        </div>
      );
  }
}
