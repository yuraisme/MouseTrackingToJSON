## Mouse tracking to JSON

_This class helps to record coordinats to JSON object_
### Dependeses:
          - winput
          - json
  

#### Main usage:
	 
	  MouseTracking # main class
		start_tracking() - # begin loop with mouse/keyboard hook - until the Esc key will not be pressed
		stop_tracking() - # stop loop
		to_json()   - # convert main list with coordinates to JSON object 		
		
		JSON Object looks :
			 JSON object like
            		_{ 'xy_coord': [x,y,time]
              		  'lclick'  : [x,y,time]
              		  'rclick'  : [x,y,time]
              		  'drag'    : [x,y,time]
              		  'wheel'   : [x,y,wheel_direction,time]
              		  'mclick'  : [x,y,time]
              		 }_
