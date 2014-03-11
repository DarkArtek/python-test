import requests
import json
#r= requests.get('http://ialpython.apiary.io/laboratories')
#print r.text

url ='http://ialpyton.apiary.io/laboratories'
payload = {'network_status':'down'}

r = requests.get(url,data=json.dumps(payload))

print r.text

