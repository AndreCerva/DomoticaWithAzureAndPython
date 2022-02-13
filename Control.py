from dotenv import load_dotenv
import os
from flask import Flask,request,render_template
from azure.iot.hub import IoTHubRegistryManager
app=Flask(__name__)
load_dotenv()
@app.route('/',methods=["GET"])
def main():
    return render_template('form.html')
@app.route('/',methods=["POST"])
def welcome():
    orden = request.form['menu']
    try:
        registry_manager = IoTHubRegistryManager(string)
        print ( 'Sending message... ' )
        registry_manager.send_c2d_message(device,orden)
    except Exception as ex:
        print ( "Unexpected error {0}" % ex )
        return
    except KeyboardInterrupt:
        print ( "IoT Hub C2D Messaging service sample stopped" )
    return render_template('welcome.html',orden=orden)
#------------------------------------------------------------------------------------
device = os.environ['DEVICEID']
string=os.environ['CSTRING']
#-------------------------------------------------------------------------------------
app.run(debug=True)