import serial
import time
import requests
from datetime import datetime

ser = serial.Serial('COM3',9600)
ser.flushInput()


payload_key_list = ['plant_id','environmental_dimension','environmental_value']
url = "https://pauls-garden.herokuapp.com/api/plant_measurement/"
files = []
headers= {}



while True:
    try:
        ser.flushInput()
        ser_bytes = ser.readline()
        try:
            decoded_bytes = ser_bytes[0:len(ser_bytes)-2].decode("utf-8").split(':')

            payload = dict(zip(payload_key_list, decoded_bytes))

            now = datetime.now()
            # print(now.strftime('YYYY-MM-DDThh:mm'))
            payload['measurement_timestamp'] = now#
            payload['plant_id'] = 'https://pauls-garden.herokuapp.com/api/plant/1/'

            print(payload)
            response = requests.request("POST", url, headers=headers, data = payload, files = files)

            print(response.text.encode('utf8'))


        except:
            print('something went wrong')
            continue

    except:
        print("Keyboard Interrupt")
        break

