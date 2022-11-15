'''
This is program for jetson nano to recieve signal 
from metal detection sensor and optic barrier to detect car
and then capture the car image using camera and AI to read License plate
it have function that if it failed to read Lp it will notify and then wait
but if it work it will send str to server and wait for respond
if server return yes then it will sent signal to Automatic Barrier Gate to open-state
and sent signal to close state when optic barrier is drop

Optional function is the OCD display
'''
###  setup start here ###
import time
# connect to server API
###  setup end here ###

### Pins setup start here ###
input_metal = 1
input_optic = 2
output_open = None
output_close = None
### Pins setup end here ###

###  system init start here ###
work = True
state_gate = False # init as close/False
state_metal = False
state_optic = False
timer_metal = 200
timer_optic = 200
dt = 0
###  system init end here ###

# input Buffering
# input Late Forgiveness
# NOT IMPLEMENTED YET
# def get_carV2(im = None,io = None, dt):
#     if(im == None or io == None):
#         return 0
#     else:
#         # sm = GPIO.input(im)
#         # so = GPIO.input(io)
#         return 1


###  function start here ###
def get_car(im = None,io = None, dt = 0):
    if(im == None or io == None):
        return True
    else:
        # sm = GPIO.input(im)
        # so = GPIO.input(io)
        # if(sm > 200 and so > 200):
        #     return 1
        return True

###  function end here ###

###  function start here ###
def get_license():
    # AI HERE
    # NotImplemented
    string = '' #
    return string

###  function end here ###

###  function start here ###
def validate_car(lp):
    # Sent str to server
    # NotImplemented
    lp = '' #
    return True

###  function end here ###
 
###  function start here ###
def update_gate_state(lp):
    # GPIO OUTPUT setting
    # NotImplemented
    return 

###  function end here ###

###  main start here ###
while(work):
    timeAtStartLoop = time.time_ns()

    isCar = get_car(input_metal, input_optic, dt) # GPIO
    if(isCar):
        lp = get_license() # AI
        if(validate_car(lp)): # API
            state_gate = True
            print('Welcome')
        else:
            print("You didn't registered for ALPR System")
    work = False
    update_gate_state(state_gate,dt) # GPIO
    
    dt = time.time_ns()-timeAtStartLoop
    print(dt)
###  main end here ###