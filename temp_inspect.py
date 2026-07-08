import requests
import re
url='https://www.dhlottery.co.kr/gameResult.do?method=byWin&drwNo=1200'
headers={'User-Agent':'Mozilla/5.0','Accept':'text/html'}
r=requests.get(url,headers=headers,timeout=15)
print('status', r.status_code)
print('content-type', r.headers.get('content-type'))
print('script tags count', len(re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', r.text)))
print(re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', r.text)[:30])
