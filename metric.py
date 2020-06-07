import requests
import dbconn
import datetime as dt

url = "http://aio-2521:8041/v1/metric/6ca53dea-a827-4205-9fcb-59b6da7c470e/measures"
headers = {
    'X-Auth-Token': 'gAAAAABe3N1tLSiJVCo4IuKyBjF_ZmBUxfb72Pe-zdo2rtYgxoel0VBD9imeecfKicw15mYnkW-ctFBSzt73UPEsRrpr9DfCE3v9r-0awu1SNO-aRyn0TAaka5nU9sQxwa6KVZuRg3BFqsJbfTIyNx0RXaji66A_1Dj5Wm_P5tdYpYALI9x53Hc',
    'Content-Type': 'application/json;charset=utf-8'
}
response = requests.get(url, headers=headers)
data = response.json()

if response.status_code != 200:
    print('Error occurred to get the data from API call:', response.status_code)
else:
    print('API call success. Metrics data sent to influxDB for storage, please check influxDB now.')

val = 0
for dataval in data:

    # Formatting and conversion not required.
    # ts = dt.datetime.strptime(dataval[0][0:19], '%Y-%m-%dT%H:%M:%S')
    # ts_str = str(ts)
    # print(ts_str)

    # Converting into Dictionary
    val = {
        'timestamp': dataval[0],
        'granularity': dataval[1],
        'value': dataval[2]
    }

# Calling influxDB client and writing into it for storage.
# Measurement and Fields are mandatory {tags are optional}
# https://docs.influxdata.com/influxdb/v1.8/concepts/key_concepts/#field-key
dbconn.client.write_points([{"measurement": "cpu", "fields": val}])





