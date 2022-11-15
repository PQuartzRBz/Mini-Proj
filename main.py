###  import start here ###
import time
from carDetection import Detect
from gateUpdate import update_gate_state
from serverComm import validate_car
from licenseReading import get_license
# connect to server API
###  import end here ###

### Pins setup start here ###
input_metal = 11
input_optic = 12
output_led = 13
output_open = 14
output_close = 15
### Pins setup end here ###

###  system setup start here ###
work = True
state_gate = False # init as close/False
state_metal = False
state_optic = False
timer_metal = 200
timer_optic = 200
dt = 0

mySensor = Detect(output_led,input_metal,input_optic)
###  system setup end here ###


###  main start here ###
while(work):
    timeAtStartLoop = time.time_ns()

    if(mySensor.get_car()):
        licenseNumber = get_license() # AI
        if(validate_car(licenseNumber)): # API
            state_gate = True
            print('Welcome')
        else:
            print("You didn't registered for ALPR System")
    work = False
    update_gate_state(state_gate,dt) # GPIO
    
    dt = time.time_ns()-timeAtStartLoop
    print(dt)
###  main end here ###