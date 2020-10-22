import Mousetracking as mt

mouse = mt.MouseTracking()

print("Start Tracking")
print("Press escape to quit")

mouse.start_tracking()
# after is not active while we are "catching the events"

mouse.stop_tracking()

f = open('coords.json', 'w')

print('End tracking and wrote  to file')
f.write(mouse.to_json())
f.close()
