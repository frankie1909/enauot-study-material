import requests

url = "https://rpc.mywebapi.com/getEmployeeNameById"

data = {"id":"1943-A"}

response = requests.get(url=url, data=data)

