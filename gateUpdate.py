import RPi.GPIO as GPIO

class Gate(object):
    def __init__(self,open,close):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        self.DI8 = open
        self.DI9 = close

        GPIO.setup(self.DI8, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.DI9, GPIO.OUT, initial=GPIO.LOW)


    def open(self):
        GPIO.output(self.DI8, GPIO.HIGH)
        GPIO.output(self.DI9, GPIO.LOW)

    def close(self):
        GPIO.output(self.DI9, GPIO.HIGH)
        GPIO.output(self.DI8, GPIO.LOW)

    def kill(self):
        GPIO.output(self.DI9, GPIO.LOW)
        GPIO.output(self.DI8, GPIO.LOW)
