import React, { Component, PropTypes } from 'react';

export default class 詞條區塊 extends Component {
    constructor(props) {
      super(props);
    }

    render() {
      return (
          <div className='main container'>
              {this.props.children}
          </div>
      );
    }
}
