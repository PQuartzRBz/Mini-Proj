import RPi.GPIO as GPIO

class Detect(object):

    def __init__(self,metal,light):

        self.in_metal = metal
        self.in_light = light

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)


        GPIO.setup(self.in_metal, GPIO.IN)
        GPIO.setup(self.in_light, GPIO.IN)
    
    ###  function start here ###
    def get_car(self):
        if(GPIO.input(self.in_metal) == GPIO.HIGH and GPIO.input(self.in_light) == GPIO.HIGH):
            return True
        else:
            return False

    ###  function end here ###

    def kill(self):
        GPIO.output(self.in_metal, GPIO.LOW)
        GPIO.output(self.in_light, GPIO.LOW)
