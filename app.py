from flask import Flask, request
import serial
import sys
import time
import apiai
import json


app = Flask(__name__)

ser = serial.Serial("COM3", 9600)

time.sleep(3)

application1 =  False

application2 =  False

@app.route('/app1', methods=["GET"])
def app1():

    global application1

    try:

        ser.write("L".encode())

        if not application1:

            application1 = not application1

            return "ON"

        else:

            application1 = not application1

            return "OFF"

    except serial.SerialException as e:
        #There is no new data from serial port
        print(str(e))
        sys.exit(1)
    except TypeError as e:
        print(str(e))
        ser.close()
        sys.exit(1)


@app.route('/app2', methods=["GET"])
def app2():

    global application2

    try:

        ser.write("F".encode())

        if not application2:

            application2 = not application2

            return "ON"

        else:

            application2 = not application2

            return "OFF"


    except serial.SerialException as e:
        #There is no new data from serial port
        print(str(e))
        sys.exit(1)
    except TypeError as e:
        print(str(e))
        ser.close()
        sys.exit(1)


@app.route('/app3/<text>', methods=["Get"])
def app3(text):
    print(text)
    ai= apiai.ApiAI("1a07551ce7a54835b19d319a2355d9a2")
    request = ai.text_request()
    request.query = text
    request.session ="lksdjifsd"
    request.lang = "en"
    response = request.getresponse()
    response = response.read()
    response = json.loads(response)
    print(response)

    params = response['response']['parameters']
    entity = params['lights']
    op = params['operation']
     if entity == "light1":

            global application1

    try:

        ser.write("L".encode())

        if not application1:

            application1 = not application1

            return "ON"

        else:

            application1 = not application1

            return "OFF"

    except serial.SerialException as e:
        #There is no new data from serial port
        print(str(e))
        sys.exit(1)
    except TypeError as e:
        print(str(e))
        ser.close()
        sys.exit(1)

elif entity == "light 2":
         global application2

    try:

        ser.write("F".encode())

        if not application2:

            application2 = not application2

            return "ON"

        else:

            application2 = not application2

            return "OFF"


    except serial.SerialException as e:
        #There is no new data from serial port
        print(str(e))
        sys.exit(1)
    except TypeError as e:
        print(str(e))
        ser.close()
        sys.exit(1)
    
         
if __name__ == "__main__":

    app.run(port=8000)

    

    
        

        
