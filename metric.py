import requests
import dbconn
import datetime as dt

url = "http://aio-2521:8041/v1/metric/6ca53dea-a827-4205-9fcb-59b6da7c470e/measures"
headers = {
    'X-Auth-Token': 'gAAAAABe3L1fi5BzcqT753iOs_8P-RS8NjnyXmwVbDgnPIRsDTHpoFkunwmC4DRiSvOhdzhZT-UvujeOMMJpwO3gb6rvIH-aIMOYrTNmht8I3cYGR91ZL1goUHxkb3a8aqPnYaRrCCJ4GJV-gbF6wShoXJ-9mZ9rve5EvSh-sl2hVH0bFyFAiiI',
    'Content-Type': 'application/json;charset=utf-8'
}
response = requests.get(url, headers=headers)
data = response.json()

if response.status_code != 200:
    print('Error occurred to get the data:', response.status_code)
else:
    print('Data retrieved below successfully:')

val = 0

for dataval in data:

    ts = dt.datetime.strptime(dataval[0][0:19], '%Y-%m-%dT%H:%M:%S')
    ts_str = str(ts)
    # ts_int = int(ts_str)
    # print(type(ts_int))

    val = {
        'timestamp': ts,
        'granularity': dataval[1],
        'value': dataval[2]
    }

dbconn.client.write_points([{"measurement": "cpu", "tags": val}])





