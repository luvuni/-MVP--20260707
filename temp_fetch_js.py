import requests,re
headers={'User-Agent':'Mozilla/5.0'}
urls=[
    'https://www.dhlottery.co.kr/resources/js/common.js?v=20260127',
    'https://www.dhlottery.co.kr/common/cmmUtil.js?v=20260625',
    'https://www.dhlottery.co.kr/common/gmUtil.js?v=20260209',
    'https://www.dhlottery.co.kr/common/msgUtil.js?v=20260318',
]
for url in urls:
    r=requests.get(url,headers=headers,timeout=15)
    print('URL',url,'status',r.status_code,'len',len(r.text))
    txt=r.text
    found=False
    for pat in ['getLottoNumber','getLottoNumberWin','drwNo','common.do','gameResult.do','byWin','lotto','drawNo','ajax','JSON','xmlHttpRequest','method']:
        if pat in txt:
            found=True
            print('  found',pat)
    if found:
        print('---')
