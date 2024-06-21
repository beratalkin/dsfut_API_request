from hashlib import md5
import requests
import time
import winsound

fifa = ''
console = 'ps'
partner_id = ''
secret_key = ''
timestamp = ''
signature = ''
params = {'min_buy': '','max_buy': ''}

counter = 0

temp_response = '{"error":"empty","message":"Queue is empty"}'

while True:
    timestamp = str(int(time.time()))
    signature = (md5((partner_id+secret_key+timestamp).encode())).hexdigest()
    
    url = "https://dsfut.net/api/23/ps/14421/" + timestamp + '/' + signature
    
    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload,params=params)

    print(response.text + timestamp)
    
    time.sleep(1)
    
    if response.text != temp_response:
        winsound.Beep(440,5000)
        break
        
        
        
    
    
    
