import requests
import json
import pandas as pd
from pandas import json_normalize
import numpy as np
import random
import datetime
from pyfirmata import Arduino, util
import time


import serial.tools.list_ports



def list_ports():
    arduino_ports = serial.tools.list_ports.comports()
    df = pd.DataFrame( columns=['device','serial_number'])
    for port in arduino_ports:
        df = df.append(pd.DataFrame(port.__dict__, index=[0])[['device','serial_number']])
    return(df.reset_index(drop=True))


def get_config():
    api_url = 'https://pauls-garden.herokuapp.com/api/arduinopin/'
    response = requests.get(api_url)
    if response.status_code == 200:
        json_string = ( json.loads(response.content.decode('utf-8')))
        df = json_normalize(json_string,'results')
        return(df)

def build_iterator():
    config_df = get_config()
    port_df = list_ports()
    config_df = config_df.merge(port_df,how='left',left_on='arduino_id', right_on='serial_number')
    config_df['environmental_value'] = np.nan
    return(config_df)

config_df= build_iterator()


def translate(value, LeftMin, LeftMax,RightMin, RightMax):
    # Figure out how 'wide' each range is
    LeftSpan = LeftMax - LeftMin
    RightSpan =  RightMax- RightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - LeftMin) / float(LeftSpan)

    # Convert the 0-1 range into a value in the right range.
    return int(RightMin + (valueScaled * RightSpan))



def iterate_config_list(config_df,port_id):
    board = Arduino(port_id)
    iterator = util.Iterator(board)
    iterator.start()
    for index, row in config_df.iterrows():

        voltage = board.get_pin(row['pin_number'])
        time.sleep(.3)
        voltage=voltage.read()
        config_df.at[index,'environmental_value'] = translate(voltage,0,100,row['sensor_low'],row['sensor_high'])

        column_names = ['plant_id', 'measurement_timestamp', 'environmental_dimension', 'environmental_value']
        df_row = pd.DataFrame(columns=column_names)

        dict = {'plant_id': row['plant_id'],
                'measurement_timestamp': datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'),
                'environmental_dimension': row['environmental_dimension'],
                'environmental_value': row['environmental_value']
               }

        r = requests.post('https://pauls-garden.herokuapp.com/api/plant_measurement/', json=dict)
        print(r.json())
    board.exit()



























while True:
    iterate_config_list(config_df, 'COM3')
    time.sleep(3)
    print(' ')



