# -*- coding:utf-8 -*-
from xmlmojip import *
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer

##global
conn = None
#regKey = '73ee2bc65b*******8b927fc6cd79a97'
regKey = 'VLBCqkxEh5fmYHkME8uHOAZpstdHOtfWLbBTasDsOudEwqF8fi2RQRQ8ywYqlADby70fOmyXKgA7u8JdQDrC8A%3D%3D'

# 네이버 OpenAPI 접속 정보 information
#server = "openapi.naver.com"
server = 'apis.data.go.kr'


def userURIBuilder(server,**user):
    #str = "http://" + server + "/search" + "?"
    str = "http://" + server + "/1300000/mjbJiWon/list" + "?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
#    print(str)
    return str


def userURIBuilderB(server,**user):
    #str = "http://" + server + "/search" + "?"
    str = "http://" + server + "/1300000/MachumTG/list" + "?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
#    print(str)
    return str


def userURIBuilderC(server,**user):
    #str = "http://" + server + "/search" + "?"
    str = "http://" + server + "/1300000/bistGongseok/list/bistGongseok/list" + "?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
#    print(str)
    return str

def connectOpenAPIServer():
    global conn, server
    conn = HTTPConnection(server)
        
def getBookDataFromISBN(Choice):
    global server, regKey, conn
    if conn == None :
        connectOpenAPIServer()
    #uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)
    uri = userURIBuilder(server, serviceKey=regKey,numOfRows='100',pageSize='1',pageNo=str(Choice),startPage='1',output="xml")  # 다음 검색 URL
    #해군 %ED%95%B4%EA%B5%B0 공군  %EA%B3%B5%EA%B5%B0
    conn.request("GET",uri)

    req = conn.getresponse()
#    print (req.status)
    if int(req.status) == 200 :
#        print("Book data downloading complete!")
        return extractBookData(req.read())
    else:
        print ("OpenAPI request has been failed!! please retry")
        return None


def getBookDataFromISBNB(Choice):
    global server, regKey, conn
    if conn == None:
        connectOpenAPIServer()
    # uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)
    uri = userURIBuilderB(server, serviceKey=regKey, numOfRows='100', pageSize='1', pageNo=str(Choice), startPage='1',output="xml")  # 다음 검색 URL
    # http://apis.data.go.kr/1300000/MachumTG/list?serviceKey=VLBCqkxEh5fmYHkME8uHOAZpstdHOtfWLbBTasDsOudEwqF8fi2RQRQ8ywYqlADby70fOmyXKgA7u8JdQDrC8A%3D%3D&numOfRows=10&pageSize=10&pageNo=1&startPage=1
    # 해군 %ED%95%B4%EA%B5%B0 공군  %EA%B3%B5%EA%B5%B0
    conn.request("GET", uri)

    req = conn.getresponse()
    #    print (req.status)
    if int(req.status) == 200:
        #        print("Book data downloading complete!")
        return extractBookDataB(req.read())
    else:
        print("OpenAPI request has been failed!! please retry")
        return None


def getBookDataFromISBNC(Choice):
    global server, regKey, conn
    if conn == None:
        connectOpenAPIServer()
    # uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)
    uri = userURIBuilderC(server, serviceKey=regKey, numOfRows='100', pageSize='1', pageNo=str(Choice), startPage='1',output="xml")  # 다음 검색 URL
    # 해군 %ED%95%B4%EA%B5%B0 공군  %EA%B3%B5%EA%B5%B0
    conn.request("GET", uri)

    req = conn.getresponse()
    #    print (req.status)
    if int(req.status) == 200:
        #        print("Book data downloading complete!")
        return extractBookDataC(req.read())
    else:
        print("OpenAPI request has been failed!! please retry")
        return None



def extractBookData(strXml):
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)
#    print (strXml)
    # Book 엘리먼트를 가져옵니다.
    itemElements = tree.getiterator("item")  # return list type
#    print(itemElements)
    for item in itemElements:
        gsteukgiNm = item.find("gsteukgiNm")
        gtcdNm1 = item.find("gtcdNm1")
        gtcdNm2 = item.find("gtcdNm2")
        gubun = item.find("gubun")
        jgmyeonheoDg = item.find("jgmyeonheoDg")
        jjganjeopGbcd = item.find("jjganjeopGbcd")
        if len(gtcdNm1.text) > 0 :
           AddBook({"gsteukgiNm":gsteukgiNm.text,"gtcdNm1":gtcdNm1.text,"gtcdNm2":gtcdNm2.text,"gubun":gubun.text,"jgmyeonheoDg":jgmyeonheoDg.text,"jjganjeopGbcd":jjganjeopGbcd.text})


def extractBookDataB(strXml):
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)
#    print (strXml)
    # Book 엘리먼트를 가져옵니다.
    itemElements = tree.getiterator("item")  # return list type
#    print(itemElements)
    for item in itemElements:
        gsteukgiNm = item.find("gsteukgiNm")
        gtcdNm1 = item.find("gtcdNm1")
        gtcdNm2 = item.find("gtcdNm2")
        mojipYy = item.find("mojipYy")
        mojipTms = item.find("mojipTms")
        ipyeongDt = item.find("ipyeongDt")
        mojipPcnt = item.find("mojipPcnt")
        jygs = item.find("jygs")

        if len(gtcdNm1.text) > 0 :
           AddBookB({"gsteukgiNm":gsteukgiNm.text,"gtcdNm1":gtcdNm1.text,"gtcdNm2":gtcdNm2.text,"mojipYy":mojipYy.text,"mojipTms":mojipTms.text,"ipyeongDt":ipyeongDt.text,"mojipPcnt":mojipPcnt.text,"jygs":jygs.text})


def extractBookDataC(strXml):
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)
#    print (strXml)
    # Book 엘리먼트를 가져옵니다.
    itemElements = tree.getiterator("item")  # return list type
#    print(itemElements)
    for item in itemElements:
        bmgigwanNm = item.find("bmgigwanNm")
        ghjbcNm = item.find("ghjbcNm")
        bjdsggjusoNm = item.find("bjdsggjusoNm")
        gsbaejeongPcnt = item.find("gsbaejeongPcnt")
        jhgyehoekPcnt = item.find("jhgyehoekPcnt")
        rnum = item.find("rnum")
        seonbalYn = item.find("seonbalYn")
        shbmsojipDt = item.find("shbmsojipDt")
        if len(ghjbcNm.text) > 0 :
           AddBookC({"bmgigwanNm":bmgigwanNm.text,"ghjbcNm":ghjbcNm.text,"bjdsggjusoNm":bjdsggjusoNm.text,"gsbaejeongPcnt":gsbaejeongPcnt.text,"jhgyehoekPcnt":jhgyehoekPcnt.text,"rnum":rnum.text,"seonbalYn":seonbalYn.text,"shbmsojipDt":shbmsojipDt.text})




class MyHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        from urllib.parse import urlparse
        import sys
      
        parts = urlparse(self.path)
        keyword, value = parts.query.split('=',1)

        if keyword == "gtcdNm2" :
            html = MakeHtmlDoc(SearchBookTitle(value)) # keyword에 해당하는 책을 검색해서 HTML로 전환합니다.
            ##헤더 부분을 작성.
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode('utf-8')) #  본분( body ) 부분을 출력 합니다.
        else:
            self.send_error(400,' bad requst : please check the your url') # 잘 못된 요청라는 에러를 응답한다.
        
def startWebService():
    try:
        server = HTTPServer( ('localhost',8080), MyHandler)
        print("started http server....")
        server.serve_forever()
        
    except KeyboardInterrupt:
        print ("shutdown web server")
        server.socket.close()  # server 종료합니다.

def checkConnection():
    global conn
    if conn == None:
        print("Error : connection is fail")
        return False
    return True
