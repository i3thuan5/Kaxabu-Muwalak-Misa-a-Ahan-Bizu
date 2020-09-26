import React, { useState } from 'react'
import { useTransition, animated } from 'react-spring'
import BunliPlayer from '../BunliPlayer'

const PlayerMenu = ({showPlayerMenu}) => {
  // const {toggle, setToggle} = useState(false)

  const transitions = useTransition(showPlayerMenu, null, {
      from: {
        opacity: 0.5
      },
      enter: {
      	opacity: 1
      },
      leave: {
      	opacity: 0
      }
  })

  // return (<div className='ui container'>
  // 	<BunliPlayer/>
  // </div>)
  return transitions.map(({item, key, props}) =>
  	item && <animated.div key={key}
		  		className="ui container" 
			  	style={props}
			>
        	<BunliPlayer/>
      		</animated.div>
	)
}

export default PlayerMenu