import winput
import json
import time

list = {}

with open("coords.json", "r") as read_file:
    j = json.load(read_file)




winput.set_mouse_pos(0,0)
i = 0


for xy in j['xy']:
    print(j['xy'][1][2]-j['xy'][0][2])
    if i > 0:
        delay = xy[2] - j['xy'][i-1][2]
        time.sleep(delay/1000)

    winput.set_mouse_pos(xy[0], xy[1])
    i+=1
