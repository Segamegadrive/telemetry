import requests
import dbconn
import datetime as dt

url = "http://aio-2521:8041/v1/metric/6ca53dea-a827-4205-9fcb-59b6da7c470e/measures"
headers = {
    'X-Auth-Token': 'gAAAAABe3CcmC6Eo6UcC4Dh-IyA-1NAcwrzf1TDK-dv0Q4x4ovNsabL_isAi40Yaj3xk6zjMjOqe7Bwwja3T_WhJDx4BNJnKT1V2mQCQGwdaf4a_aqsJb2BW22R9H38tlUG77hJkTQ1SbdH2miahoGGlzqITbp1UlXZZc8bJsZCzuCB_T3PzmBo',
    'Content-Type': 'application/json;charset=utf-8'
}
response = requests.get(url, headers=headers)
data = response.json()

if response.status_code != 200:
    print('Error occurred to get the data:', response.status_code)
else:
    print('Data retrieved below successfully:')

for dataval in data:

    ts = dt.datetime.strptime(dataval[0][0:19], '%Y-%m-%dT%H:%M:%S')
    ts_str = str(ts)
    ts_int = int(ts_str)

    val = {
        'timestamp': ts_int,
        'granularity': dataval[1],
        'value': dataval[2]
    }

dbconn.client.write_points({"measurements": "cpu", "tags": val})





