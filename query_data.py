import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = '-6azjF3SGpfpOiNYYZPjm_mGVBiez4eHfht9X8TrbAhb7gfYJQqNMvwgOJGu0Yu7lodtalYdjt4q4utV4P1wqw=='

org = "putteneersjoris@gmail.com"
url = "https://us-east-1-1.aws.cloud2.influxdata.com"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

bucket="sample-bucket"


query_api = client.query_api()

query = """from(bucket: "sample-bucket")
 |> range(start: -1h)
 |> filter(fn: (r) => r._measurement == "measurement1")"""
tables = query_api.query(query, org="putteneersjoris@gmail.com")

for table in tables:
  for record in table.records:
    print(record)

query_api = client.query_api()

# query = """from(bucket: "sample-bucket")
#   |> range(start: -10m)
#   |> filter(fn: (r) => r._measurement == "measurement1")
#   |> mean()"""
# tables = query_api.query(query, org="putteneersjoris@gmail.com")

# for table in tables:
#     for record in table.records:
#         print(record)

print('done')