import RPi.GPIO as GPIO

class Detect(object):

    def __init__(self, led,metal,light):
        self.LED_Pin = led
        self.in_metal = metal
        self.in_light = light

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup(self.LED_Pin, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.in_metal, GPIO.IN)
        GPIO.setup(self.in_light, GPIO.IN)
    
    ###  function start here ###
    def get_car(self):
        if(GPIO.input(self.in_metal) == GPIO.HIGH and GPIO.input(self.in_light) == GPIO.HIGH):
            GPIO.output(self.LED_Pin, GPIO.HIGH)
            return True
        else:
            GPIO.output(self.LED_Pin, GPIO.LOW)
            return False

    ###  function end here ###

    def kill(self):
        GPIO.output(self.LED_Pin, GPIO.LOW)
        GPIO.output(self.in_metal, GPIO.LOW)
        GPIO.output(self.in_light, GPIO.LOW)
