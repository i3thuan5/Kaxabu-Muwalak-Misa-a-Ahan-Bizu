import React, { useState } from 'react'
import { useTransition, animated } from 'react-spring'
import BunliPlayer from '../BunliPlayer'

const PlayerMenu = ({showPlayerMenu}) => {
  // const {toggle, setToggle} = useState(false)

  const transitions = useTransition(showPlayerMenu, null, {
      from: {
        opacity: 0, transform: 'translate3d(0,50px,0)'
      },
      enter: {
      	opacity: 1, transform: 'translate3d(0,0,0)'
      },
      leave: {
      	opacity: 0, transform: 'translate3d(0,50,0)'
      }
  })

   return transitions.map(({item, key, props}) =>
  	item && <animated.div key={key}
		  		className="ui bottom fixed menu" 
			  	style={props}
			>
        		<BunliPlayer/>
      		</animated.div>
	)
}

export default PlayerMenu