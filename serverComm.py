###  function start here ###
import requests
import json
url = "endpoint"
def validate_car(lp):
    # Sent str to server
    # NotImplemented
    payload = json.dumps(
        {
            "license_str": lp
            })
    # your code
    headers = {
            'Content-Type' : 'application/json'
            }
    response = requests.request("POST",url,headers = headers, data= payload)
    print(response.text)
    return True

###  function end here ###
