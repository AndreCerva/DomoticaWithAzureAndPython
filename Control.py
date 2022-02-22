from dotenv import load_dotenv #Librería para poder usar el archivo .env para más seguridad de nuestras keys
import os #Librería para procesos relacionados con nuestro sistema operativo
from flask import Flask,request,render_template #Librerias importantes para nuestra app web 
from azure.iot.hub import IoTHubRegistryManager #Libreria para enviar nuestros mensajes a IoT Hub

app=Flask(__name__)#Creamos objeto Flask al momento de ejecutar nuestro script, lo instanciamos en app
load_dotenv()#Cargamos los pares de claves que se tienen en el archivo .env
device = os.environ['DEVICEID'] #Se almacena en la variable device el valor del par DEVUCEID en .env
string=os.environ['CSTRING']#Se almacena en la variable string el valor del par CSTRING en .env

@app.route('/',methods=["GET"])#Definimos la ruta principal de nuestra aplicacion a donde se direccionara cuando el cliente solicite información mediante el metodo GET
def main():#Al dirigirse a esta ruta, entra en la función main
    return render_template('form.html')#Esta función main devuelve un template, el cual es el archivo form.html que se encuentra en la carpeta templates
@app.route('/',methods=["POST"])#Definimos la ruta cuando el cliente solicite información con POST
def welcome():#Al enviar el metodo POST se entra a la función welcome
    orden = request.form['options']#se recuperan los valores que se enviaron por el formulario html
    try:
        registry_manager = IoTHubRegistryManager(string)#Inicializamos un objeto de la clase para hacer uso del servicio de IoTHub
        registry_manager.send_c2d_message(device,orden)#Se envia un mensaje con parametros hacia que dispositivo se enviara y la orden que se puso en el formulario
    except Exception as ex:#Si sucede alguna exception
        print ( "Unexpected error {0}" % ex )#mensaje en consola de que no se pudo realizar el envio
        return
    except KeyboardInterrupt:#Cuando se detiene la ejecución del script en la terminal con ctrl+c
        print ( "IoT Hub C2D Messaging service sample stopped" )#mensaje en consola de que se detuvo la ejecución
    return render_template('welcome.html',orden=orden)#Al final, se envie o no el mensaje se regresa un template el cual recibe como parametro la orden que enviamos
app.run(debug=True)#Ejecutamos nuestra aplicación con el parametro debug true para modo de desarrollo