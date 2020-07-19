import requests
import json
import pandas as pd
from pandas import json_normalize
import numpy as np
import random
import datetime
from pyfirmata import Arduino, util
import time
# board = Arduino('COM3')

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
    print(config_df.columns)
    return(config_df)

config_df= build_iterator()


def iterate_config_list(config_df):
    for index, row in config_df.iterrows():
        board = Arduino(row['device'])
        iterator = util.Iterator(board)
        iterator.start()
        voltage = board.get_pin('a:0:1')
        time.sleep(.3)








iterate_config_list(config_df)


    #

# board = Arduino('COM3')
#
#
#
#
#
#
# iterator = util.Iterator(board)
# iterator.start()
#
# Tv1 = board.get_pin('a:0:1')
# time.sleep(1.0)
# print(Tv1.read())













# while True:
#     api_url = 'https://pauls-garden.herokuapp.com/api/plant_measurement/'
#     response = requests.get(api_url)
#     if response.status_code == 200:
#         json_string = ( json.loads(response.content.decode('utf-8')))
#         df = json_normalize(json_string,'results')
#         for index, row in df.iterrows():
#             column_names = ['plant_id', 'measurement_timestamp', 'environmental_dimension', 'environmental_value']
#             df_row = pd.DataFrame(columns=column_names)
#
#             dict = {'plant_id': row['plant_id'],
#                     'measurement_timestamp': datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'),
#                     'environmental_dimension': row['environmental_dimension'],
#                     'environmental_value': random.randint(50,60)
#                    }
#
#             measure_json = (json.dumps(dict))
#             # r = requests.post('http://127.0.0.1:8000/api/plant_measurement/', json=dict)
#             print(r.json())
#             time.sleep(1)
#
#
#     else:
#         pass
#
#     time.sleep(10)
#     print(' ')
#
#
#
#
#
#
#


