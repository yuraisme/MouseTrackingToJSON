import winput
import json
import time
from winput.vk_codes import *
import sys

list = {}
print(sys.argv[1])




with open(sys.argv[1], "r") as read_file:
    j = json.load(read_file)

winput.set_mouse_pos(0,0)
i = 0
click_count = 0
print(len(j['lclick']))

for xy in j['xy']:

    if i > 0:
        delay = xy[2] - j['xy'][i-1][2]
        print(delay)
        time.sleep(delay/1000)
    
    if len(j['lclick']) > click_count:

        if xy[2]-100 >= j['lclick'][click_count][2]:
            winput.click_mouse_button()
            print(f'L - click! {click_count}')
            click_count += 1

    winput.set_mouse_pos(xy[0], xy[1])
    i+=1


print("Done!")