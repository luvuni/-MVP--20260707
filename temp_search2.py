import requests
url='https://www.dhlottery.co.kr/'
headers={'User-Agent':'Mozilla/5.0','Accept':'text/html'}
r=requests.get(url,headers=headers,timeout=20)
text=r.text
for key in ['1227회','1228회','1229회','1230회','1231회']:
    idx=text.find(key)
    print('KEY',key,'idx',idx)
    if idx != -1:
        snippet=text[max(0,idx-120):idx+180].replace('\n',' ')
        print(snippet)
