# -*- coding:utf-8 -*-

from internetmojip import *
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import messagebox
import tkinter.messagebox

loopFlag = 1
#### Menu  implementation
def printMenu():
    print("₩n입대 도우미 프로그램 !!)")
    print("========Menu==========")
    print("모집현황 출력 : b")
    print("군명으로 찾기 (육,해,공군) : e")
    print("전공 , 자격증으로 찾기 : g")
#    print("Make html: m")
    print("프로그램 닫기:   q")
    print("메일로 보내기 : i")
    print("========Menu==========")


def launcherFunction(menu):
    if menu == 'q':
        QuitBookMgr()
    elif menu == 'b':
        PrintBookList2(["gtcdNm1", ])
        #PrintBookList(["gsteukgiNm", ])
    elif menu == 'e':
        keyword = str(input('검색할 군명을 입력해주세요 (ex : 육군, 공군, 해군, 해병) :'))
        SearchBookTitleB(keyword)
    elif menu == 'g':
        keyword = str(input('검색할 자격증, 전공을 입력해주세요 :'))
        SearchBookTitle1B(keyword)
 #       gtcdNm2 = str(input('input gtcdNm2 to get :'))
        # isbn = '0596513984'  ,  gtcdNm2 전자상거래무역학전공
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

LoadXMLFromFile()
getBookDataFromISBN(1)
#getBookDataFromISBN(201)
#getBookDataFromISBN(301)
#getBookDataFromISBN(3701)
#getBookDataFromISBN(5701)
#getBookDataFromISBN(6701)
#getBookDataFromISBN(7701)
#getBookDataFromISBN(9801)
#getBookDataFromISBN(10001)
getBookDataFromISBNB(1)
#getBookDataFromISBNB(201)
#getBookDataFromISBNB(301)
#getBookDataFromISBNB(3701)
#getBookDataFromISBNB(5701)
#getBookDataFromISBNB(6701)
#getBookDataFromISBNB(8701)
getBookDataFromISBNC(1)
#getBookDataFromISBNC(301)
#getBookDataFromISBNC(451)
#getBookDataFromISBNC(701)
#getBookDataFromISBNC(801)



menu = 4
InitTopText()
InitTopText2()
InitSearchListBox()
InitSearchListBox2()
InitInputLabel()
InitInputLabel2()
InitSearchButton()
InitSearchButton2()
InitSearchButton3()
InitSearchButton4()
InitSearchButton6()
InitRenderText()
g_Tk.mainloop()
