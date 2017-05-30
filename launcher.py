# -*- coding: cp949 -*-
loopFlag = 1
from internetmojip import *


#### Menu  implementation
def printMenu():
    print("\nWelcome! GunSa Manager Program (xml version)")
    print("========Menu==========")
    print("Load xml:  l")
    print("Print dom to xml: p")
    print("Quit program:   q")
    print("print Book list: b")
    print("Add new book: a")
    print("sEarch Book Title: e")
    print("Make html: m")
    print("----------------------------------------")
    print("Get book data from isbn: g")
    print("send maIl : i")
    print("sTart Web Service: t")
    print("========Menu==========")


def launcherFunction(menu):
    if menu == 'l':
        LoadXMLFromFile()
    elif menu == 'q':
        QuitBookMgr()
    elif menu == 'p':
        PrintDOMtoXML()
    elif menu == 'b':
        PrintBookList(["gtcdNm1", ])
    elif menu == 'a':
        gsteukgiNm = str(input('특기명을 입력하세요 :'))
        gtcdNm1 = str(input('insert gtcdNm1(군종) :'))
        AddBook({'gsteukgiNm': gsteukgiNm, 'gtcdNm1': gtcdNm1})
    elif menu == 'e':
        keyword = str(input('input keyword to search :'))
        printBookList(SearchBookTitle(keyword))
    elif menu == 'g':
        gtcdNm2 = str(input('input gtcdNm2 to get :'))
        # isbn = '0596513984'  ,  gtcdNm2 전자상거래무역학전공
        ret = getBookDataFromISBN(gtcdNm2)
        #AddBook(ret)
    elif menu == 'm':
        keyword = str(input('input keyword code to the html  :'))
        html = MakeHtmlDoc(SearchBookTitle(keyword))
        print("-----------------------")
        print(html)
        print("-----------------------")
    elif menu == 'i':
        sendMain()
    elif menu == "t":
        startWebService()
    else:
        print("error : unknow menu key")


def QuitBookMgr():
    global loopFlag
    loopFlag = 0
    BooksFree()


##### run #####
while (loopFlag > 0):
    printMenu()
    menuKey = str(input('select menu :'))
    launcherFunction(menuKey)
else:
    print("Thank you! Good Bye")
