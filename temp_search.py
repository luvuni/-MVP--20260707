import requests
url='https://www.dhlottery.co.kr/'
headers={'User-Agent':'Mozilla/5.0','Accept':'text/html'}
r=requests.get(url,headers=headers,timeout=20)
text=r.text
print('status', r.status_code)
idx = text.find('회')
print('first index', idx)
for pos in range(idx-200, idx+200, 40):
    if pos < 0: continue
    print('===', pos)
    print(text[pos:pos+160].replace('\n',' '))
# search for '회 ' occurrences
for i in range(0, len(text), 1000):
    seg=text[i:i+1000]
    if '회' in seg:
        print('segment contains 회 at', i, seg.count('회'))
        break
