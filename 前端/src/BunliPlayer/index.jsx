import React from 'react'
import ReactPlayer from 'react-player'
import Duration from './Duration'


class BunliPlayer extends React.Component {
  constructor(props){
    super(props)
    this.state = {
      isReady: false,
      playing: true,
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
  let { playing } = this.state
	console.log('onReady, playing=', playing)
  this.setState({isReady: true, playing: true})
}

handleDuration = (duration) => {
  // console.log('onDuration:', duration)
  this.setState({duration})
}

handleStart(){
	console.log('onStart')
}

handlePlay(){
	this.setState({playing: true})
}

handleProgress = state => {
  // console.log('onProgress:', state)
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

resizeProgress = () => {
  let { played } = this.state
  let width = played * 100 + 'vw'
  console.log('width=', width)
  return width
}

render () {
  let { handleClose, imtong } = this.props
  let { url, pianho, gi, lueiong } = imtong
	let { isReady, playing, duration, played, playedSeconds } = this.state
  console.log('imtong=',imtong )
  let width = this.resizeProgress()

    return (
    	<div className='player-wrapper'>
        <h2 className='ui inverted grey header'>{lueiong}
          <div className='sub header'>{pianho} {gi}</div>
        </h2>
        {
          isReady
            ? <div className='player-progress'
                  style={{width}}/>
            : null
        }
        {
        	isReady
          	? <div className='player-control'>
                <button
                  className={
                    `ui ${
                      playing
                        ? ''
                        : 'basic'
                    } pink huge circular icon button`}
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
                <button
                  className='ui inverted basic huge circular icon button'
                  onClick={handleClose}
                >
                  <i className='icon close'/>
                </button>
              </div>
        		:	<span>waiting...</span>
        }
        <ReactPlayer
          url={url}
          className='react-player'
          width={100}
          height={20}
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
