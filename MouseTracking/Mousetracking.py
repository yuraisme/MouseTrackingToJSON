"""
This class allow to pack mouse events to JSON obejct

"""
import winput
import json


class MouseTracking:

    def __init__(self):
        """
         :type Constructor


         init variables and main event collector:
         xy_list{['events']} as

         xy_list['xy'] = []

         xy_list['lclick'] = []

         xy_list['rclick'] = []

         xy_list['drag'] = []

         xy_list['wheel'] = []

         xy_list['mclick'] = []


         stop_key :   use from winput.WM_xxx  keys
            default is winput.VK_ESCAPE

         WAIT_FOR_DRAG_STARTING - delay in msec to start record of dragging

        """
        self.xy_list = {}
        self.xy_list['xy'] = []
        self.xy_list['lclick'] = []
        self.xy_list['rclick'] = []
        self.xy_list['drag'] = []
        self.xy_list['wheel'] = []
        self.xy_list['mclick'] = []
        self.ldown = False
        self.count_before_drag = 0
        self.stop_key = winput.VK_ESCAPE
        self.WAIT_FOR_DRAG_STARTING = 50
        self.silent = False

    def mouse_callback(self, event):  # mouse events looking
        """
        Function is hooking
        mouse moving and pressing
        collect to  list xy_list {['some_events']}
        as array
        ---
        nothing return
        event- as main argument
        """

        if event.action == winput.WM_LBUTTONDOWN:
            # print("Left mouse button press at {}".format(event.position))

            self.xy_list['lclick'].append(
                [event.position[0], event.position[1], event.time])  # write xy coord + time from system start in ms
            self.ldown = True

        if event.action == winput.WM_LBUTTONUP:
            if self.ldown:
                print('drop')
            self.ldown = False
            self.count_before_drag = 0

        if event.action == winput.WM_MOUSEWHEEL:
            self.xy_list['wheel'].append([event.position[0], event.position[1], event.additional_data[0], event.time])

        if event.action == winput.WM_RBUTTONDOWN:
            self.xy_list['rclick'].append([event.position[0], event.position[1], event.time])

        if event.action == winput.WM_MOUSEMOVE:
            # print("Mouse move to {}".format(event.position))

            if self.ldown and self.count_before_drag > self.WAIT_FOR_DRAG_STARTING:  # try to understand - we already drag or not
                print('drag')
                self.xy_list['drag'].append([event.position[0], event.position[1], event.time])
            else:
                self.count_before_drag += 1
                self.xy_list['xy'].append([event.position[0], event.position[1], event.time])

        if event.action == winput.WM_MBUTTONDOWN:
            self.xy_list['mclick'].append([event.position[0], event.position[1], event.time])

    def keyboard_callback(self, event):
        """
         Function is hooking
         key pressing

         ---
         nothing return
         event- as main argument
        """

        if event.vkCode == self.stop_key:  # quit on pressing escape
            winput.stop()

    def start_tracking(self):
        """
         Start hooking for
         mouse and keyboard
         nothing return
        """
        winput.hook_mouse(self.mouse_callback)
        winput.hook_keyboard(self.keyboard_callback)

        # enter message loop
        winput.wait_messages()

    def stop_tracking(self):
        """
         Stop hooking for
         mouse and keyboard
         nothing return
        """
        # remove input hook
        winput.unhook_mouse()
        winput.unhook_keyboard()

    def to_json(self):
        """
        Convert list xy_coord{['events']}
        to JSON Format
        :type JSON

        :return:
        JSON object like
            { 'xy_coord': [x,y,time]
              'lclick'  : [x,y,time]
              'rclick'  : [x,y,time]
              'drag'    : [x,y,time]
              'wheel'   : [x,y,time]
              'mclick'  : [x,y,time]
            }
        with indent = 1
        """

        j = json.dumps(self.xy_list, indent=1)
        return j


if __name__ == '__main__':
    print('hey! it\'s the library!')
