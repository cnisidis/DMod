import bpy 
import socket
import subprocess
import threading 
from struct import unpack


class DmodThread(threading.Thread):
 
    data = None
    running = False
    sock = None

    def __init__(self):
        threading.Thread.__init__(self)
        self.data = None
        
    def start(self):

        # Run an external client that sends position
        # and orientation of the device through the
        # network (port 3000).
        #subprocess.call(['./razer_client.exe', '3000'])

        # Start the thread.
        print('Starting Dmod thread')
        self.running = True
        threading.Thread.start(self)

    def stop(self):

        # Stop the thread.
        print('Stopping DMod thread')
        self.running = False

    def run(self):

        # Setup the network socket.
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.settimeout(1)
        self.sock.bind(('127.0.0.1', 5555))

        # Receive new data from the client.
        while self.running:
            try:
                self.data = struct.unpack('7f', sock.recv(4096))
            except socket.timeout:
                self.sock.close()
                pass

class DMOD(bpy.types.Operator):
    bl_idname = "dmod.udp"
    bl_label = "DMod Receive"
    bl_options = {'REGISTER'}

    thread = None
    timer = None
    wm = bpy.context.window_manager
    


    def modal(self, context, event):

        # Stop the thread when ESCAPE is pressed.
        if event.type == 'ESC':
            self.thread.stop()
            context.window_manager.event_timer_remove(self.timer)
            return {'CANCELLED'}

        # Update the object with the received data.
        if event.type == 'TIMER':
            #bpy.data.objects['cube'].location = self.thread.data[:2]
            #bpy.data.objects['cube'].rotation_quaternion = self.thread.data[3:]
            print(self.thread.data)
            return {'PASS_THROUGH'}
 

    def invoke(self, context):
        self.thread = DmodThread()
        self.thread.start()
        self.timer = context.window_manager.event_timer_add(0.05, context.window)
        context.window_manager.modal_handler_add(self)
        return {"RUNNING_MODAL"}

    
