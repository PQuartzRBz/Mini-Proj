import RPi.GPIO as GPIO
from picamera import PiCamera
import requests, base64, json
from openalpr import Alpr

class LiceneseReading(object):

    def __init__(self):
        self.camera = PiCamera()

        self.camera.resolution = (2592, 1944)
        self.camera.framerate = 15

        self.alpr = Alpr("us", "/etc/openalpr/openalpr.conf", "openalpr/runtime_data/")
        if not self.alpr.is_loaded():
            print("Error loading OpenALPR")
            return
        results = self.alpr.recognize_file("/path/to/image.jpg")
        print(json.dumps(results, indent=4))
        self.alpr.unload()


    def capture(self):
        
        # capture the next image
        self.camera.start_preview()
        img = self.camera.capture('/home/pi/Desktop/image.jpg')
        self.camera.stop_preview()
        return img

    def read(self,img):
        # detect objects in the image (with overlay)
        results1 = self.alpr.recognize_file("/path/to/image.jpg")
        results2 = self.alpr.recognize_ndarray(img)
        # print the detections
        print(results2)
        
        string = json.dumps(results1, indent=4)
        print(string)

        return string

