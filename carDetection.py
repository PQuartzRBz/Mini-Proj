import Jetson.GPIO as GPIO

LED_Pin = 12



GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(LED_Pin, GPIO.OUT, initial=GPIO.LOW)

###  function start here ###
def get_car(im = None,io = None, dt = 0):
    if(im == None or io == None):
        GPIO.output(LED_Pin, GPIO.LOW)
        return False
    else:
        # sm = GPIO.input(im)
        # so = GPIO.input(io)
        # if(sm > 200 and so > 200):
        #     return 1
        GPIO.output(LED_Pin, GPIO.HIGH)
        return True

###  function end here ###