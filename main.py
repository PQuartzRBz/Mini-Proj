###  setup start here ###
import time
from carDetection import get_car
from gateUpdate import update_gate_state
from serverComm import validate_car
from licenseReading import get_license
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