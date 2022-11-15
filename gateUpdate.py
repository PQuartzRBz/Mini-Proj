import Jetson.GPIO as GPIO

LED_Pin = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(LED_Pin, GPIO.OUT, initial=GPIO.LOW)

###  function start here ###
def update_gate_state(lp):
    # GPIO OUTPUT setting
    # NotImplemented
    return 

###  function end here ###