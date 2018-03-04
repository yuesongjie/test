import requests
import json
url='http://www.qihuo18.com/api/v1/market/exchangelist'
# data={'catid':'66'}
# r=requests.get(url,params=data).content
r=requests.get(url).content
print(json.dumps(json.loads(r), indent=4, sort_keys=False, ensure_ascii=False))