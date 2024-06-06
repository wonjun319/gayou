import requests as req

serviceKey = 't73LIKbFt1hCBViupj7bDfzg6wpDFI%252F3OYYHT9jnKOOiwRVcR3IGLKh%252F55wC47sDwISMZ0ssmWDBPSjeu2NNQg%253D%253D'


def deco(func):
    def wrapper(**kwargs):
        try:
            return func(**kwargs)
        except Exception as e:
            print('='*100)
            print(e)
            print('='*100)
        return None
    return wrapper


"""
한국관광공사_두루누비 정보 서비스_GW API
https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15101974#/

(Base URL: apis.data.go.kr/B551011/Durunubi)

GET : /courseList
코스 목록 정보를 조회하는 기능입니다.

Parameters
Name            type            Description
----------------------------------------------
numOfRows       string          한페이지결과수
pageNo          string          페이지번호
MobileOS *      string          OS 구분 : IOS (아이폰), AND (안드로이드), WIN (윈도우폰), ETC(기타)
MobileApp *     string          서비스명(어플명)
serviceKey *    string          인증키(서비스키)
_type           string          응답메세지 형식 : REST방식의 URL호출 시 json값 추가(디폴트 응답메세지 형식은XML)
crsKorNm        string          코스명
routeIdx        string          길 고유번호
crsLevel        string          난이도(하:1, 중:2, 상:3)
brdDiv          string          걷기/자전거 구분(DNBW=자전거 길, DNWW=걷기 길)
"""
@deco
def courseList(numOfRows='10', pageNo='1', MobileOS='ETC', MobileApp='GAYOU', _type='json', crsKorNm='', routeIdx='', crsLevel='', brdDiv=''):
    url = f'https://apis.data.go.kr/B551011/Durunubi/courseList?numOfRows={numOfRows}&pageNo={pageNo}&MobileOS={MobileOS}&MobileApp={MobileApp} \
        &serviceKey={serviceKey}&_type={_type}&crsKorNm={crsKorNm}&routeIdx={routeIdx}&crsLevel={crsLevel}&brdDiv={brdDiv}'
    
    res = req.get(url)
    data = res.json()
    data = data['response']['body']['items']['item']
    return data


"""
한국관광공사_두루누비 정보 서비스_GW API
https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15101974#/

(Base URL: apis.data.go.kr/B551011/Durunubi)

GET : /routeList
길 목록 정보를 조회하는 기능입니다.

Parameters
Name            type            Description
----------------------------------------------
numOfRows       string          한페이지결과수
pageNo          string          페이지번호
MobileOS *      string          OS 구분 : IOS (아이폰), AND (안드로이드), WIN (윈도우폰), ETC(기타)
MobileApp *     string          서비스명(어플명)
serviceKey *    string          인증키(서비스키)
_type           string          응답메세지 형식 : REST방식의 URL호출 시 json값 추가(디폴트 응답메세지 형식은XML)
themeNm         string          길 명
brdDiv          string          걷기/자전거 구분(DNBW=자전거 길, DNWW=걷기 길)
"""
@deco
def routeList(numOfRows='10', pageNo='1', MobileOS='ETC', MobileApp='GAYOU', _type='json', brdDiv=''):
    url = f'https://apis.data.go.kr/B551011/Durunubi/routeList?numOfRows={numOfRows}&pageNo={pageNo}&MobileOS={MobileOS}&MobileApp={MobileApp} \
        &serviceKey={serviceKey}&_type={_type}&brdDiv={brdDiv}'
    res = req.get(url)
    data = res.json()
    data = data['response']['body']['items']['item']
    return data


"""
한국관광공사_외래객 친화 관광정보 GW API
https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15111159#

(Base URL: apis.data.go.kr/B551011/ForFriTourService)

GET : /locationBasedList
내주변 좌표를 기반으로 외래객 친화 관광정보 목록을 조회하는 기능입니다. 파라미터에 따라 제목순, 수정일순(최신순), 등록일순, 거리순 정렬검색을 제공합니다.(이미지 : 공공누리1,3유형만 제공만)

Parameters
Name            type            Description
----------------------------------------------
serviceKey *    string          공공데이터포털에서 받은 인증키
numOfRows       number          한 페이지 결과 수
pageNo          number          현재 페이지 번호
MobileOS *      string          IOS (아이폰), AND (안드로이드), WIN (윈도우폰), ETC
MobileApp *     string          서비스명=어플명
arrange         string          정렬구분(A=제목순, C=수정일순, D=생성일순, E=거리순) 대표이미지가반드시있는정렬 (O=제목순, Q=수정일순, R=생성일순,S=거리순)
contentTypeId   string          관광타입(1145:음식 , 1146:기도실) ID
mapX *          string          GPS X좌표(WGS84 경도 좌표)
mapY *          string          GPS Y좌표(WGS84 위도 좌표)
radius *        string          거리 반경(단위:m) , Max값 20000m=20Km
modifiedtime    string          수정일(형식 :YYYYMMDD)
_type           string          응답메세지 형식 : REST방식의 URL호출 시 json값 추가(디폴트 응답메세지 형식은XML)
"""
@deco
def locationBasedList(mapX, mapY, radius, numOfRows=10, pageNo=1, MobileOS='ETC', MobileApp='GAYOU', arrange='', contentTypeId='', modifiedtime='', _type='json'):
    url = f'https://apis.data.go.kr/B551011/Durunubi/routeList?numOfRows={numOfRows}&pageNo={pageNo}&MobileOS={MobileOS}&MobileApp={MobileApp} \
        &serviceKey={serviceKey}&_type={_type}'
    res = req.get(url)
    data = res.json()
    data = data['response']['body']['items']['item']
    return data


