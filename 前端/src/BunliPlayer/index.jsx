import React from 'react'
import ReactPlayer from 'react-player'
import Duration from './Duration'


class BunliPlayer extends React.Component {
  constructor(props){
    super(props)
    this.state = {
      isReady: false,
      playing: false,
      duration: 0,
      played: 0,
      playedSeconds: 0,
      loaded: 0,
    }
    this.handleReady = this.handleReady.bind(this)
    this.handleStart = this.handleStart.bind(this)
    this.handlePlay = this.handlePlay.bind(this)
    this.togglePlayPause = this.togglePlayPause.bind(this)
  }

handleReady(){
	console.log('onReady')
  this.setState({isReady: true})
}

handleDuration = (duration) => {
  console.log('onDuration:', duration)
  this.setState({duration})
}

handleStart(){
	console.log('onStart')
}

handlePlay(){
	this.setState({playing: true})
}

handleProgress = state => {
  console.log('onProgress:', state)
  this.setState(state)
}

handleEnded = () => {
  console.log('onEnded')
  this.setState({playing: false})
}


togglePlayPause(e){
	e.preventDefault()
	this.setState({playing: !this.state.playing})
}

render () {
	let { isReady, playing, duration, played, playedSeconds } = this.state
  
    return (
    	<div className='player-wrapper'>
        {
        	isReady 
          	? <div>
                <button
                  className='ui basic circular icon button'
                  onClick={this.togglePlayPause}
                >
                  <i className={
                    `icon ${
                            playing
                              ? 'pause'
                              : 'play '
                    }`}
                  />
                </button>
                <Duration seconds={playedSeconds}/>
                <progress max={1} value={played} />
                <Duration seconds={duration}/>
              </div>
        		:	<span>waiting...</span>
        }
        <ReactPlayer
          url='https://dbkaxabu.xn--v0qr21b.xn--kpry57d/%E8%81%BD?%E8%AA%9E%E8%A9%9E%E7%B7%A8%E8%99%9F=01A-001&%E5%85%A7%E5%AE%B9=%E8%8F%AF%E8%AA%9E'
          className='react-player'
          onReady={this.handleReady}
          onStart={this.handleStart}
          onBuffer={()=>{console.log('onBuffer')}}    
          onBufferEnd={()=>{console.log('onBufferEnd')}}
          onDuration={this.handleDuration}
          onPlay={this.handlePlay}
          onEnded={this.handleEnded}
          onProgress={this.handleProgress}
          progressInterval={150}
          playing={playing}
          config={{
            file: {
              forceVideo: false,
              forceAudio: true,
            }
          }}
        />
      </div>
    )
  }
}

export default BunliPlayer
