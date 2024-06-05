import requests as req

numOfRows = 10
pageNo = 1
# OS 구분 : IOS (아이폰), AND (안드로이드), WIN (윈도우폰), ETC(기타)
MobileOS = 'ETC'
MobileApp = 'GAYOU'
serviceKey = 't73LIKbFt1hCBViupj7bDfzg6wpDFI%252F3OYYHT9jnKOOiwRVcR3IGLKh%252F55wC47sDwISMZ0ssmWDBPSjeu2NNQg%253D%253D'
# 응답메세지 형식 : REST방식의 URL호출 시 json값 추가(디폴트 응답메세지 형식은XML)
_type = 'json'

"""
한국관광공사_두루누비 정보 서비스_GW API
"""
def courseList():
    # MobileOS = ''
    # MobileApp = 'asfdsdfasdfasdfasdf156asd456asd1f5asd1f56a1sd5f1a5s6df1asd1f65asd1f56as1df65a1sd5f6156'
    serviceKey = ''
    url = f'https://apis.data.go.kr/B551011/Durunubi/courseList?numOfRows={numOfRows}&pageNo={pageNo}&MobileOS={MobileOS}&MobileApp={MobileApp}&serviceKey={serviceKey}&_type={_type}'
    print(url)
    res = req.get(url)
    print(res, res.status_code)
    print(res.text)
    if res.status_code != 200:
        print(res.status_code)
        return None
    print('-'*200)
    data = res.json()
    print(data)
    if 'resultCode' in data:
        print(data['resultCode'])
        return data['resultCode']
    print(data['resultCode'])
    print(data['response']['header'])
    print('-'*200)
    data = data['response']['body']['items']['item']
    # for d in data:
    #     print(d)
    return data

courseList()