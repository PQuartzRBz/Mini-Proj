import RPi.GPIO as GPIO
from picamera import PiCamera
import json
import subprocess,time
import numpy as np

class LiceneseReading(object):

    def __init__(self):
        self.camera = PiCamera()

        self.camera.resolution = (2592, 1944)
        self.camera.framerate = 15

    def capture(self):
        # capture the next image
        self.camera.start_preview()
        img = self.camera.capture('/home/pi/Desktop/image.jpg')
        self.camera.stop_preview()
        return img

    def read(self,img):
        po3 = subprocess.Popen(['lxterminal','alpr'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=True)
        po3.stdin.write('3\n')
        po3.stdin.flush()
        po3.wait()
        output = po3.stdout.read()
        print(output)
        for o in output:
            if(o=='\t' ):
                o = ' '

        res = output.split()
        for r in res:
            try:
                res.remove('confidence:')
            except:
                continue

        for r in res:
            try:
                res.remove('-')
            except:
                continue
        res.pop(0)
        res.pop(0)
        res.pop(0)

        res = np.array(res)
        res.resize(int((len(res)/2)),2)

        max = res[0,1]
        for r in res[:,1]:
            if r.astype(np.float64) > max.astype(np.float64):
                max = r
        string = np.reshape(res[np.where(res == max)[0]],-1)[0]
        print(string)

        return string

