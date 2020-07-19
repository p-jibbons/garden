import requests
import json
import pandas as pd
from pandas import json_normalize
import random
import datetime
import time

while True:
    api_url = 'http://127.0.0.1:8000/api/arduinopin/?format=json&arduino_id=00000001&is_collecting=True'
    response = requests.get(api_url)
    if response.status_code == 200:
        json_string = ( json.loads(response.content.decode('utf-8')))
        df = json_normalize(json_string,'results')
        for index, row in df.iterrows():
            column_names = ['plant_id', 'measurement_timestamp', 'environmental_dimension', 'environmental_value']
            df_row = pd.DataFrame(columns=column_names)

            dict = {'plant_id': row['plant_id'],
                    'measurement_timestamp': datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'),
                    'environmental_dimension': row['environmental_dimension'],
                    'environmental_value': random.randint(50,60)
                   }

            measure_json = (json.dumps(dict))
            r = requests.post('http://127.0.0.1:8000/api/plant_measurement/', json=dict)
            print(r.json())
            time.sleep(1)


    else:
        pass

    time.sleep(10)
    print(' ')









