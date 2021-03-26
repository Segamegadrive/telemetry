import requests
import dbconn
#import datetime as dt

url = "http://aio-2521:8041/v1/metric/6ca53dea-a827-4205-9fcb-59b6da7c470e/measures"
headers = {
    'X-Auth-Token': 'gAAAAABe_562XC-eSH69KHsmLADY3n-3saWOCi0O-iVpazku1PL1wkjGXZl4bDP3GVOyPuTFqN2kynNV6vrmIsyy_uyN7sK-TlNc_0F-WZ7ugUaIyDnomUrQe7vikrBzXXzVx6_SZeda3VT1Wn4uKSxGa4Kjnn8V2CsscXdIFpm_aUC2qAOQJS4',
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





