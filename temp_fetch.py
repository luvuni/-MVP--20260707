import requests, re
urls=[
    'https://www.lotto.net/lotto-645/draw-history',
    'https://www.lotto.net/lotto-645',
    'https://www.lotto.net/',
]
headers={'User-Agent':'Mozilla/5.0'}
for url in urls:
    try:
        r=requests.get(url,headers=headers,timeout=15)
        print('URL',url,'status',r.status_code,'len',len(r.text))
        found = re.findall(r'\b(\d{1,2})\s*\d{1,2}\s*\d{1,2}\s*\d{1,2}\s*\d{1,2}\s*\d{1,2}\b', r.text)
        print('found numbers examples', found[:5])
    except Exception as e:
        print('ERR',url,e)
