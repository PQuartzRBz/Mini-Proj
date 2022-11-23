###  import start here ###
import time
from carDetection import Detect
from gateUpdate import Gate
from serverComm import validate_car
from licenseReading import LiceneseReading
# connect to server API
###  import end here ###

### Pins setup start here ###
input_metal = 17
input_optic = 26

output_open = 5
output_close = 6
### Pins setup end here ###

###  system setup start here ###
work = True
state_open = False
timer_time = 3000 # millisecond
dt = 0

mySensor = Detect(input_metal,input_optic)
myGate = Gate(output_open,output_close)
myReader = LiceneseReading
###  system setup end here ###


###  main start here ###
while(work):
    curr_time = round(time.time()*1000)

    if(state_open):
        if(timer > 0):
            timer -= dt
        else:
            myGate.close()
            state_open = False

    if(mySensor.get_car()):
        img = myReader.capture() # AI
        licenseNumber = myReader.read(img=img)
        if(validate_car(licenseNumber)): # API
            state_open = True
            timer = timer_time 
            myGate.open()
            print('Welcome')
        else:
            print("You didn't registered for ALPR System")
    
    dt = round(time.time()*1000)-curr_time
    
    print(timer)
###  main end here ###