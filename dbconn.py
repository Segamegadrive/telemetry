from influxdb import InfluxDBClient

client = InfluxDBClient(host='localhost', port='8086', database='metrics')
client.switch_database('metrics')
