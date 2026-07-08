import requests, re
url='https://www.dhlottery.co.kr/'
headers={'User-Agent':'Mozilla/5.0','Accept':'text/html'}
r=requests.get(url,headers=headers,timeout=20)
text=r.text
print('status', r.status_code)
# look for draw summary patterns like 1227회 2026.06.06 ...
pattern=re.compile(r'(\d{3,4})회\s*(\d{4}\.\d{2}\.\d{2})\s*([0-9]{12,14})')
matches=pattern.findall(text)
print('matches', len(matches))
for m in matches[:20]:
    print(m)
