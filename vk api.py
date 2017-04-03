import urllib.request
import json

req = urllib.request.Request('https://api.vk.com/method/wall.getComments?owner_id=38899819&domain=justmashko&count=2&post_id=5292') 
with urllib.request.urlopen(req) as response:
    result = response.read().decode('utf-8')

data = json.loads(result) 

print(data)
