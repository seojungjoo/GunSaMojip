# -*- coding:utf-8 -*-
from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree
from internetmojip import *
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import tkinter.messagebox
import webbrowser
from PIL import Image, ImageTk
from io import BytesIO
import urllib
import urllib.request
import random

newImg = None
newImg2 = None
label2 = None
# smtp 정보
host = "smtp.gmail.com" # Gmail SMTP 서버 주소.'
port = "587"

g_Tk = Tk()
g_Tk.geometry("400x640+700+100")
DataList = []
menu = 4
KSKK = ""
def InitTopText():
    TempFont = font.Font(g_Tk, size=20, weight='bold', family = 'Consolas')
    MainText = Label(g_Tk, font = TempFont, text="[군입대 도우미 프로그램]")
    MainText.pack()
    MainText.place(x=21)

def InitTopText2():
    TempFont = font.Font(g_Tk, size=10, family = 'Consolas')
    MainText = Label(g_Tk, font = TempFont, text="메일 주소 :")
    MainText.pack()
    MainText.place(x=15,y=560)

def InitSearchListBox():
    global SearchListBox
    ListBoxScrollbar = Scrollbar(g_Tk)
    ListBoxScrollbar.pack()
    ListBoxScrollbar.place(x=150, y=50)
    TempFont = font.Font(g_Tk, size=15, weight='bold', family='Consolas')
    SearchListBox = Listbox(g_Tk, font=TempFont, activestyle='none',
                            width=10, height=1, borderwidth=12, relief='ridge',
                            yscrollcommand=ListBoxScrollbar.set)

    SearchListBox.insert(1, "전공,자격증")
    SearchListBox.insert(2, "맞춤특기병")
    SearchListBox.insert(3, "공익 공석")
    SearchListBox.pack()
    SearchListBox.place(x=10, y=50)

def InitSearchListBox2():
    global SearchListBox2
    global menu
    ListBoxScrollbar = Scrollbar(g_Tk)
    ListBoxScrollbar.pack()
    ListBoxScrollbar.place(x=330, y=100)
    TempFont = font.Font(g_Tk, size=15, weight='bold', family='Consolas')
    SearchListBox2 = Listbox(g_Tk, font=TempFont, activestyle='none',
                            width=26, height=1, borderwidth=12, relief='ridge',
                            yscrollcommand=ListBoxScrollbar.set)
    if menu == 0:
        SearchListBox2.insert(1, "군별로 검색")
        SearchListBox2.insert(2, "전공,자격증으로 검색")
    elif menu == 1:
        SearchListBox2.insert(1, "군별로 검색")
        SearchListBox2.insert(2, "특기명으로 검색")
    elif menu == 2:
        SearchListBox2.insert(1, "기관명으로 검색")
        SearchListBox2.insert(2, "지방청명으로 검색")
    elif menu == 4:
        SearchListBox2.insert(1, "상단 메뉴를 적용 시켜주세요")
    SearchListBox2.pack()
    SearchListBox2.place(x=10, y=100)


def InitInputLabel():
    global InputLabel
    TempFont = font.Font(g_Tk, size=15, weight='bold', family = 'Consolas')
    InputLabel = Entry(g_Tk, font = TempFont, width = 26, borderwidth = 12, relief = 'ridge')
    InputLabel.pack()
    InputLabel.place(x=10, y=155)


def InitInputLabel2():
    global InputLabel2
    TempFont = font.Font(g_Tk, size=10, family = 'Consolas')
    InputLabel2 = Entry(g_Tk, font = TempFont, width = 19, borderwidth = 12, relief = 'ridge')
    InputLabel2.pack()
    InputLabel2.place(x=90, y=550)

def InitSearchButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    SearchButton = Button(g_Tk, font = TempFont, text="검색",  command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=330, y=160)

def SearchButtonAction():
    global SearchListBox2
    global InputLabel
    global KSKK
    global RenderText
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    iSearchIndex = SearchListBox2.curselection()[0]
    if menu == 0:
        if iSearchIndex == 0:
            SearchBookTitle(InputLabel.get())
            print(InputLabel.get())
        elif iSearchIndex == 1:
            SearchBookTitle1(InputLabel.get())
    elif menu == 1:
        if iSearchIndex == 0:
            SearchBookTitleB(InputLabel.get())
        elif iSearchIndex == 1:
            SearchBookTitle1B(InputLabel.get())
    elif menu == 2:
        if iSearchIndex == 0:
            SearchBookTitleC(InputLabel.get())
        elif iSearchIndex == 1:
            SearchBookTitle1C(InputLabel.get())
    elif menu == 4:
        pass
    KSKK = RenderText.get("1.0",END)


    RenderText.configure(state='disabled')


def InitSearchButton2(): # 적용
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    SearchButton = Button(g_Tk, font = TempFont, text="적용",  command=SearchButtonAction2)
    SearchButton.pack()
    SearchButton.place(x=170, y=60)

def SearchButtonAction2():
    global SearchListBox
    global menu
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    iSearchIndex = SearchListBox.curselection()[0]
    if iSearchIndex == 0:
        menu = 0
    elif iSearchIndex == 1:
        menu = 1
    elif iSearchIndex == 2:
        menu = 2
    RenderText.configure(state='disabled')
    InitSearchListBox2()


def InitSearchButton3(): # 적용
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    SearchButton = Button(g_Tk, font = TempFont, text="메일로 보내기",  command=SearchButtonAction3)
    SearchButton.pack()
    SearchButton.place(x=250, y=550)


def InitSearchButton6(): # 짤
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    SearchButton = Button(g_Tk, font = TempFont, text="입대 자극 사진",  command=SearchButtonAction6)
    SearchButton.pack()
    SearchButton.place(x=95, y=600)

def SearchButtonAction6():
    top = Toplevel()

    label2 = Label(top, text="url file load")
    label2.pack()

    i = random.randint(1, 6)
    if i == 1:
        url = "http://upload2.inven.co.kr/upload/2016/01/25/bbs/i11656379508.jpg"
    elif i == 2:
       url = "https://image.fmkorea.com/files/attach/new/20150706/3674493/175066967/188311252/1d5ec6a8ed8929fdd9ede867db2e55cd.jpg"
    elif i == 3:
      url = "http://i2.ruliweb.com/img/5/3/6/8/5368E71A4F53840006"
    elif i == 4:
     url = "http://file2.instiz.net/data/file/20140905/6/f/d/6fde109713655380bb586a814ce0ad49.jpg"
    elif i == 5:
      url = "http://cfile1.uf.tistory.com/image/2154424F5899A18D0A0726"
    elif i == 6:
     url = "http://data.ygosu.com/editor/attach/20160621/20160621225402_yvzwksdv.jpg"
    with urllib.request.urlopen(url) as u:
        raw_data = u.read()
        im = Image.open(BytesIO(raw_data))
        newImg2 = ImageTk.PhotoImage(im)
        label2.configure(image=newImg2)
    top.mainloop()

def SearchButtonAction3():
    global InputLabel2
    global host, port
    global KSKK
    html = ""
    title = "군대 입대 프로그램 메일입니다."
    senderAddr = "tjwjdwn12@gmail.com"
    recipientAddr = InputLabel2.get()
    msgtext = ""
    passwd = "5796242aa!"

    global RenderText

    msgtext = KSKK
    print(msgtext)
    import mysmtplib
    # MIMEMultipart의 MIME을 생성합니다.
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    # Message container를 생성합니다.
    msg = MIMEMultipart('alternative')

    msg = MIMEText(KSKK)
    # set message
    msg['Subject'] = title
    msg['From'] = senderAddr
    msg['To'] = recipientAddr
    msgPart = MIMEText(msgtext, 'plain')
    bookPart = MIMEText(html, 'html', _charset='UTF-8')

    # 메세지에 생성한 MIME 문서를 첨부합니다.

    print("connect smtp server ... ")
    s = mysmtplib.MySMTP(host, port)
    # s.set_debuglevel(1)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderAddr, passwd)  # 로긴을 합니다.
    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
    s.close()

    print("Mail sending complete!!!")


def InitSearchButton4(): # 적용
    TempFont = font.Font(g_Tk, size=10, weight='bold', family = 'Consolas')
    SearchButton = Button(g_Tk, font = TempFont, text="보직 설명(웹 브라우져)",  command=SearchButtonAction4)
    SearchButton.pack()
    SearchButton.place(x=220, y=65)

def SearchButtonAction4():
    global SearchListBox2
    global InputLabel
    global menu
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    iSearchIndex = SearchListBox2.curselection()[0]
    if menu == 0:
        if InputLabel.get() == "육군":
            webbrowser.open('http://www.mma.go.kr/conscription/recruit_service/procedure/army/S_board_text.do?mc=mma0000388&gun_gbcd=1&mojip_gbcd=1')
        elif InputLabel.get() == "공군":
            webbrowser.open("http://www.mma.go.kr/conscription/recruit_service/procedure/air_force/G_board_text.do?mc=mma0000468&gun_gbcd=3&mojip_gbcd=1")
        elif InputLabel.get() == "해군":
            webbrowser.open("http://www.mma.go.kr/conscription/recruit_service/procedure/navy/G_board_text.do?mc=mma0000455&gun_gbcd=2&mojip_gbcd=1")
        elif InputLabel.get() == "해병":
            webbrowser.open("http://www.mma.go.kr/conscription/recruit_service/procedure/marine/G_board_text.do?mc=mma0000461&gun_gbcd=4&mojip_gbcd=1")
    elif menu == 1:
        if InputLabel.get() == "육군":
            webbrowser.open("http://www.mma.go.kr/conscription/recruit_service/procedure/army/C_board_text.do?mc=mma0000434&gun_gbcd=1&mojip_gbcd=C")
        elif InputLabel.get() == "공군":
            webbrowser.open("http://www.mma.go.kr/conscription/recruit_service/procedure/air_force/G_board_text.do?mc=mma0000468&gun_gbcd=3&mojip_gbcd=1")
        elif InputLabel.get() == "해군":
            webbrowser.open("http://www.mma.go.kr/conscription/recruit_service/procedure/navy/C_board_text.do?mc=mma0001043&gun_gbcd=2&mojip_gbcd=C")

    InitSearchListBox2()



def InitRenderText():
    global RenderText
    RenderTextScrollbar = Scrollbar(g_Tk)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=375, y=200)
    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RenderText = Text(g_Tk, width=49, height=23, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set) #Entry 를 Text로 고쳐씀
    RenderText.pack()
    RenderText.place(x=10, y=215)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)
   # RenderText.configure(state='disabled') 여기야여기

##### global
xmlFD = -1
BooksDoc = None
BooksDoc2 = None
BooksDoc3 = None

#### xml 관련 함수 구현
def LoadXMLFromFile():
    fileName = "mojip.xml"
    fileName2 = "machum.xml"
    fileName3 = "kongsuk.xml"
    global xmlFD, BooksDoc , BooksDoc2,BooksDoc3
    try:
        xmlFD = open(fileName)
    except IOError:
        print ("invalid file name or path")
    else:
        try:
            dom = parse(xmlFD)
        except Exception:
            print ("loading fail!!!")
        else:
#            print ("XML Document loading complete")
            BooksDoc = dom

    try:
        xmlFD = open(fileName2)
    except IOError:
        print ("invalid file name or path")
    else:
        try:
            dom = parse(xmlFD)
        except Exception:
            print ("loading fail!!!")
        else:
#            print ("XML Document loading complete")
            BooksDoc2 = dom

    try:
        xmlFD = open(fileName3)
    except IOError:
        print ("invalid file name or path")
    else:
        try:
            dom = parse(xmlFD)
        except Exception:
            print ("loading fail!!!")
        else:
#            print ("XML Document loading complete")
            BooksDoc3 = dom
    return None

def BooksFree():
    if checkDocument():
        BooksDoc.unlink()
        
def PrintDOMtoXML():
    if checkDocument():
        print(BooksDoc.toxml())

def PrintBookList(tags):
    global BooksDoc
    if not checkDocument():
       return None

    tree = ElementTree.fromstring(str(BooksDoc.toxml()))

    bookElements = tree.getiterator("item")  # return list type

#    booklist = BooksDoc.childNodes
#    book = booklist[0].childNodes
    for item in bookElements:
            strTitle = item.find("gtcdNm1")
            print("ㅡㅡㅡㅡㅡㅡ")
            print("군명 = ",strTitle.text)
            print("특기명 = ",item.attrib["gsteukgiNm"],"병")
            strTitle = item.find("gtcdNm2")
            print("전공/자격증 = ",strTitle.text)
            strTitle = item.find("gubun")
            print("전공/자격증 구분 = ",strTitle.text)
            if strTitle.text == "자격":
                 strTitle = item.find("jgmyeonheoDg")
                 print("자격등급 = ",strTitle.text)
            strTitle = item.find("jjganjeopGbcd")
            print("직/간접 구분 = ",strTitle.text)

def PrintBookList2(tags):
       global BooksDoc2
       if not checkDocument():
           return None

       tree = ElementTree.fromstring(str(BooksDoc2.toxml()))
       bookElements = tree.getiterator("item")
       for item in bookElements:
           strTitle = item.find("gtcdNm1")
           RenderText.insert(END,"ㅡㅡㅡㅡㅡㅡ\n")
           RenderText.insert(END,"군명 = "+strTitle.text+"\n")
           strTitle = item.find("gtcdNm2")
           RenderText.insert(INSERT,"입대 부대 명 = ")
           RenderText.insert(INSERT, strTitle.text)
           RenderText.insert(INSERT,"\n")
           RenderText.insert(INSERT,"특기명 = ", )
           RenderText.insert(INSERT,item.attrib["gsteukgiNm"]+"병")
           RenderText.insert(INSERT,"\n")
           strTitle = item.find("mojipYy")
           RenderText.insert(INSERT,"모집 연도 = ")
           RenderText.insert(INSERT, strTitle.text)
           RenderText.insert(INSERT,"\n")
           strTitle = item.find("ipyeongDt")
           RenderText.insert(INSERT,"입영 날짜 = ")
           RenderText.insert(INSERT, strTitle.text)
           RenderText.insert(INSERT,"\n")
           strTitle = item.find("mojipPcnt")
           RenderText.insert(INSERT,"모집 인원 수 = ")
           RenderText.insert(INSERT, strTitle.text)
           RenderText.insert(INSERT,"\n")
           strTitle = item.find("jygs")
           RenderText.insert(INSERT,"잔여 공석,부족 인원 = ")
           RenderText.insert(INSERT, strTitle.text)
           RenderText.insert(INSERT,"\n")

def PrintBookList3(tags):
        global BooksDoc3
        if not checkDocument():
            return None
        tree = ElementTree.fromstring(str(BooksDoc3.toxml()))
        bookElements = tree.getiterator("item")
        for item in bookElements:
            strTitle = item.find("ghjbcNm")
            print("ㅡㅡㅡㅡㅡㅡ")
            print("관할 지방청 명 = ", strTitle.text)
            print("복무기관 명 = ", item.attrib["bmgigwanNm"])
            strTitle = item.find("bjdsggjusoNm")
            print("복무기관 주소 = ", strTitle.text)
            strTitle = item.find("gsbaejeongPcnt")
            print("공석 배정 인원 수 = ", strTitle.text)

            strTitle = item.find("jhgyehoekPcnt")
            print("집행계획 인원 수 = ", strTitle.text)
            strTitle = item.find("rnum")
            print("순번 = ", strTitle.text)
            strTitle = item.find("seonbalYn")
            print("선발 여부 = ", strTitle.text)
            strTitle = item.find("shbmsojipDt")
            print("사회복무 소집일자 = ", strTitle.text)

#            for kk in subitems:
#                if kk.nodeName in "gtcdNm1":
#                    print("gtcdNm1",kk.firstChild.nodeValue)
#                if kk.nodeName in "gtcdNm2":
#                    print("gtcdNm2",kk.firstChild.nodeValue)
#                if kk.nodeName in "gubun":
#                    print("gubun",kk.firstChild.nodeValue)
#                if kk.nodeName in "jgmyeonheoDg":
#                    if( kk.firstChild.nodeValue != " "):
#                        print("jgmyeonheoDg",kk.firstChild.nodeValue)
#                if kk.nodeName in "jjganjeopGbcd":
#                    print("jjganjeopGbcd",kk.firstChild.nodeValue)
#            subitems = item.childNodes
#            for atom in subitems:
#               if atom.nodeName in tags:
#                   print("gtcdNm1 =",atom.firstChild.nodeValue)

                
def AddBook(bookdata):
     global BooksDoc
     # book 엘리먼트 생성
     newBook = BooksDoc.createElement('item')
     newBook.setAttribute('gsteukgiNm',bookdata['gsteukgiNm'])
     # Title 엘리먼트 생성
     titleEle = BooksDoc.createElement('gtcdNm1')
     titleEle1 = BooksDoc.createElement('gtcdNm2')
     titleEle2 = BooksDoc.createElement('gubun')
     titleEle3 = BooksDoc.createElement('jgmyeonheoDg')
     titleEle4 = BooksDoc.createElement('jjganjeopGbcd')
     # 텍스트 노드 생성
     titleNode = BooksDoc.createTextNode(bookdata['gtcdNm1'])
     titleNode1 = BooksDoc.createTextNode(bookdata['gtcdNm2'])
     titleNode2 = BooksDoc.createTextNode(bookdata['gubun'])
     titleNode3 = BooksDoc.createTextNode(bookdata['jgmyeonheoDg'])
     titleNode4 = BooksDoc.createTextNode(bookdata['jjganjeopGbcd'])
     # 텍스트 노드를 Title 엘리먼트와 연결
     try:
         titleEle.appendChild(titleNode)
         titleEle1.appendChild(titleNode1)
         titleEle2.appendChild(titleNode2)
         titleEle3.appendChild(titleNode3)
         titleEle4.appendChild(titleNode4)
     except Exception:
         print ("append child fail- please,check the parent element & node!!!")
         return None
     else:
         titleEle.appendChild(titleNode)
         titleEle1.appendChild(titleNode1)
         titleEle2.appendChild(titleNode2)
         titleEle3.appendChild(titleNode3)
         titleEle4.appendChild(titleNode4)

     # Title 엘리먼트를 Book 엘리먼트와 연결.
     try:
         newBook.appendChild(titleEle)
         newBook.appendChild(titleEle1)
         newBook.appendChild(titleEle2)
         newBook.appendChild(titleEle3)
         newBook.appendChild(titleEle4)
         booklist = BooksDoc.firstChild
     except Exception:
         print ("append child fail- please,check the parent element & node!!!")
         return None
     else:
         if booklist != None:
             booklist.appendChild(newBook)


def AddBookB(bookdata):
    global BooksDoc2
    # book 엘리먼트 생성
    newBook = BooksDoc2.createElement('item')
    newBook.setAttribute('gsteukgiNm', bookdata['gsteukgiNm'])
    # Title 엘리먼트 생성
    titleEle = BooksDoc2.createElement('gtcdNm1')
    titleEle1 = BooksDoc2.createElement('gtcdNm2')
    titleEle2 = BooksDoc2.createElement('mojipYy')
    titleEle3 = BooksDoc2.createElement('mojipTms')
    titleEle4 = BooksDoc2.createElement('ipyeongDt')
    titleEle5 = BooksDoc2.createElement('mojipPcnt')
    titleEle6 = BooksDoc2.createElement('jygs')
    # 텍스트 노드 생성
    titleNode = BooksDoc2.createTextNode(bookdata['gtcdNm1'])
    titleNode1 = BooksDoc2.createTextNode(bookdata['gtcdNm2'])
    titleNode2 = BooksDoc2.createTextNode(bookdata['mojipYy'])
    titleNode3 = BooksDoc2.createTextNode(bookdata['mojipTms'])
    titleNode4 = BooksDoc2.createTextNode(bookdata['ipyeongDt'])
    titleNode5 = BooksDoc2.createTextNode(bookdata['mojipPcnt'])
    titleNode6 = BooksDoc2.createTextNode(bookdata['jygs'])
    # 텍스트 노드를 Title 엘리먼트와 연결
    try:
        titleEle.appendChild(titleNode)
        titleEle1.appendChild(titleNode1)
        titleEle2.appendChild(titleNode2)
        titleEle3.appendChild(titleNode3)
        titleEle4.appendChild(titleNode4)
        titleEle5.appendChild(titleNode5)
        titleEle6.appendChild(titleNode6)
    except Exception:
        print("append child fail- please,check the parent element & node!!!")
        return None
    else:
        titleEle.appendChild(titleNode)
        titleEle1.appendChild(titleNode1)
        titleEle2.appendChild(titleNode2)
        titleEle3.appendChild(titleNode3)
        titleEle4.appendChild(titleNode4)
        titleEle5.appendChild(titleNode5)
        titleEle6.appendChild(titleNode6)

    # Title 엘리먼트를 Book 엘리먼트와 연결.
    try:
        newBook.appendChild(titleEle)
        newBook.appendChild(titleEle1)
        newBook.appendChild(titleEle2)
        newBook.appendChild(titleEle3)
        newBook.appendChild(titleEle4)
        newBook.appendChild(titleEle5)
        newBook.appendChild(titleEle6)
        booklist = BooksDoc2.firstChild
    except Exception:
        print("append child fail- please,check the parent element & node!!!")
        return None
    else:
        if booklist != None:
            booklist.appendChild(newBook)



def AddBookC(bookdata):
    global BooksDoc3
    # book 엘리먼트 생성
    newBook = BooksDoc3.createElement('item')
    newBook.setAttribute('bmgigwanNm', bookdata['bmgigwanNm'])
    # Title 엘리먼트 생성
    titleEle = BooksDoc3.createElement('ghjbcNm')
    titleEle1 = BooksDoc3.createElement('bjdsggjusoNm')
    titleEle2 = BooksDoc3.createElement('gsbaejeongPcnt')
    titleEle3 = BooksDoc3.createElement('jhgyehoekPcnt')
    titleEle4 = BooksDoc3.createElement('rnum')
    titleEle5 = BooksDoc3.createElement('seonbalYn')
    titleEle6 = BooksDoc3.createElement('shbmsojipDt')
    # 텍스트 노드 생성
    titleNode = BooksDoc3.createTextNode(bookdata['ghjbcNm'])
    titleNode1 = BooksDoc3.createTextNode(bookdata['bjdsggjusoNm'])
    titleNode2 = BooksDoc3.createTextNode(bookdata['gsbaejeongPcnt'])
    titleNode3 = BooksDoc3.createTextNode(bookdata['jhgyehoekPcnt'])
    titleNode4 = BooksDoc3.createTextNode(bookdata['rnum'])
    titleNode5 = BooksDoc3.createTextNode(bookdata['seonbalYn'])
    titleNode6 = BooksDoc3.createTextNode(bookdata['shbmsojipDt'])
    # 텍스트 노드를 Title 엘리먼트와 연결
    try:
        titleEle.appendChild(titleNode)
        titleEle1.appendChild(titleNode1)
        titleEle2.appendChild(titleNode2)
        titleEle3.appendChild(titleNode3)
        titleEle4.appendChild(titleNode4)
        titleEle5.appendChild(titleNode5)
        titleEle6.appendChild(titleNode6)
    except Exception:
        print("append child fail- please,check the parent element & node!!!")
        return None
    else:
        titleEle.appendChild(titleNode)
        titleEle1.appendChild(titleNode1)
        titleEle2.appendChild(titleNode2)
        titleEle3.appendChild(titleNode3)
        titleEle4.appendChild(titleNode4)
        titleEle5.appendChild(titleNode5)
        titleEle6.appendChild(titleNode6)

    # Title 엘리먼트를 Book 엘리먼트와 연결.
    try:
        newBook.appendChild(titleEle)
        newBook.appendChild(titleEle1)
        newBook.appendChild(titleEle2)
        newBook.appendChild(titleEle3)
        newBook.appendChild(titleEle4)
        newBook.appendChild(titleEle5)
        newBook.appendChild(titleEle6)
        booklist = BooksDoc3.firstChild
    except Exception:
        print("append child fail- please,check the parent element & node!!!")
        return None
    else:
        if booklist != None:
            booklist.appendChild(newBook)


def SearchBookTitle(keyword):
    global BooksDoc
    retlist = []
    if not checkDocument():
        return None
    try:
        tree = ElementTree.fromstring(str(BooksDoc.toxml()))
    except Exception:
        print ("Element Tree parsing Error : maybe the xml document is not corrected.")
        return None
    
    #get Book Element
    bookElements = tree.getiterator("item")  # return list type
    for item in bookElements:
        strTitle = item.find("gtcdNm1")
        print(keyword)
        if (strTitle.text.find(keyword) >=0 ):
            RenderText.insert(INSERT,"ㅡㅡㅡㅡㅡㅡ"+"\n")
            RenderText.insert(INSERT,"군명 = "+strTitle.text+"\n")
            RenderText.insert(INSERT,"특기명 = "+item.attrib["gsteukgiNm"]+"병\n")
            strTitle = item.find("gtcdNm2")
            RenderText.insert(INSERT,"전공/자격증 = "+strTitle.text+"\n")
            strTitle = item.find("gubun")
            RenderText.insert(INSERT,"전공/자격증 구분 = "+strTitle.text+"\n")
            if strTitle.text == "자격":
                 strTitle = item.find("gubun")
                 RenderText.insert(INSERT,"자격등급 = "+strTitle.text+"\n")
            strTitle = item.find("jjganjeopGbcd")
            RenderText.insert(INSERT,"직/간접 구분 = "+strTitle.text+"\n")

#            retlist.append((item.attrib["gsteukgiNm"], strTitle.text))

#    return retlist

def SearchBookTitle1(keyword):
    global BooksDoc
    retlist = []
    if not checkDocument():
        return None
    try:
        tree = ElementTree.fromstring(str(BooksDoc.toxml()))
    except Exception:
        print("Element Tree parsing Error : maybe the xml document is not corrected.")
        return None

    # get Book Element
    bookElements = tree.getiterator("item")  # return list type
    for item in bookElements:
        strTitle = item.find("gtcdNm2")
        if (strTitle.text.find(keyword) >= 0):
            RenderText.insert(INSERT,"ㅡㅡㅡㅡㅡㅡ\n")
            strTitle = item.find("gtcdNm1")
            RenderText.insert(INSERT,"군명 = "+ strTitle.text+"n")
            RenderText.insert(INSERT,"특기명 = "+ item.attrib["gsteukgiNm"]+ "병\n")
            strTitle = item.find("gtcdNm2")
            RenderText.insert(INSERT,"전공/자격증 = "+ strTitle.text+"\n")
            strTitle = item.find("gubun")
            RenderText.insert(INSERT,"전공/자격 구분 = "+strTitle.text+"\n")
            if strTitle.text == "자격":
                strTitle = item.find("jgmyeonheoDg")
                RenderText.insert(INSERT,"자격등급 = "+ strTitle.text+"\n")
            strTitle = item.find("jjganjeopGbcd")
            RenderText.insert(INSERT,"직/간접 구분 = "+ strTitle.text+"\n")


def SearchBookTitleB(keyword):
    global BooksDoc2
    retlist = []
    if not checkDocument():
        return None
    try:
        tree = ElementTree.fromstring(str(BooksDoc2.toxml()))
    except Exception:
        print("Element Tree parsing Error : maybe the xml document is not corrected.")
        return None

    # get Book Element
    bookElements = tree.getiterator("item")  # return list type
    for item in bookElements:
        strTitle = item.find("gtcdNm1")
        if (strTitle.text.find(keyword) >= 0):
            RenderText.insert(INSERT,"ㅡㅡㅡㅡㅡㅡ\n")
            RenderText.insert(INSERT,"군명 = "+strTitle.text+"\n")
            strTitle = item.find("gtcdNm2")
            RenderText.insert(INSERT,"입영 부대 = "+ strTitle.text+"\n")
            RenderText.insert(INSERT,"특기명 = "+ item.attrib["gsteukgiNm"]+"병\n")
            strTitle = item.find("mojipYy")
            RenderText.insert(INSERT,"모집 년도 = "+ strTitle.text+"\n")
            strTitle = item.find("ipyeongDt")
            RenderText.insert(INSERT,"입영 날짜 = "+ strTitle.text+"\n")
            strTitle = item.find("mojipPcnt")
            RenderText.insert(INSERT,"모집 인원 = "+ strTitle.text+"\n")
            strTitle = item.find("jygs")
            RenderText.insert(INSERT,"잔여 공석 = "+ strTitle.text+"\n")


# retlist.append((item.attrib["gsteukgiNm"], strTitle.text))

#    return retlist

def SearchBookTitle1B(keyword):
    global BooksDoc2
    retlist = []
    if not checkDocument():
        return None
    try:
        tree = ElementTree.fromstring(str(BooksDoc2.toxml()))
    except Exception:
        print("Element Tree parsing Error : maybe the xml document is not corrected.")
        return None

    # get Book Element
    bookElements = tree.getiterator("item")  # return list type
    for item in bookElements:
        if (item.attrib["gsteukgiNm"].find(keyword) >= 0):
            RenderText.insert(INSERT,"ㅡㅡㅡㅡㅡㅡ\n")
            RenderText.insert(INSERT,"특기명 = "+ item.attrib["gsteukgiNm"]+"병\n")
            strTitle = item.find("gtcdNm1")
            RenderText.insert(INSERT,"군명 = "+strTitle.text+"\n")
            strTitle = item.find("gtcdNm2")
            RenderText.insert(INSERT,"입영 부대 = "+ strTitle.text+"\n")
            strTitle = item.find("mojipYy")
            RenderText.insert(INSERT,"모집 년도 = "+ strTitle.text+"\n")
            strTitle = item.find("ipyeongDt")
            RenderText.insert(INSERT,"입영 날짜 = "+ strTitle.text+"\n")
            strTitle = item.find("mojipPcnt")
            RenderText.insert(INSERT,"모집 인원 = "+ strTitle.text+"\n")
            strTitle = item.find("jygs")
            RenderText.insert(INSERT,"잔여 공석 = "+ strTitle.text+"\n")



def SearchBookTitleC(keyword):
    global BooksDoc3
    retlist = []
    if not checkDocument():
        return None
    try:
        tree = ElementTree.fromstring(str(BooksDoc3.toxml()))
    except Exception:
        print("Element Tree parsing Error : maybe the xml document is not corrected.")
        return None

    # get Book Element
    bookElements = tree.getiterator("item")  # return list type
    for item in bookElements:
        if (item.attrib["bmgigwanNm"].find(keyword) >= 0):
            RenderText.insert(INSERT,"ㅡㅡㅡㅡㅡㅡ\n")
            RenderText.insert(INSERT,"복무기관 명 = "+item.attrib["bmgigwanNm"]+"\n")
            strTitle = item.find("ghjbcNm")
            RenderText.insert(INSERT,"관할 지방청 명 = "+strTitle.text+"\n")
            strTitle = item.find("bjdsggjusoNm")
            RenderText.insert(INSERT,"복무 기관 주소 = "+ strTitle.text+"\n")
            strTitle = item.find("gsbaejeongPcnt")
            RenderText.insert(INSERT,"공석 배정 인원 수 = "+ strTitle.text+"\n")
            strTitle = item.find("jhgyehoekPcnt")
            RenderText.insert(INSERT,"집행 계획 인원 수 = "+ strTitle.text+"\n")
            strTitle = item.find("seonbalYn")
            RenderText.insert(INSERT,"선발 여부 = "+ strTitle.text+"\n")


# retlist.append((item.attrib["gsteukgiNm"], strTitle.text))

#    return retlist

def SearchBookTitle1C(keyword):
    global BooksDoc3
    retlist = []
    if not checkDocument():
        return None
    try:
        tree = ElementTree.fromstring(str(BooksDoc3.toxml()))
    except Exception:
        print("Element Tree parsing Error : maybe the xml document is not corrected.")
        return None

    # get Book Element
    bookElements = tree.getiterator("item")  # return list type
    for item in bookElements:
        strTitle = item.find("ghjbcNm")
        if (strTitle.text.find(keyword) >= 0):
            RenderText.insert(INSERT,"ㅡㅡㅡㅡㅡㅡ\n")
            RenderText.insert(INSERT,"관할 지방청 명 = "+ strTitle.text+"\n")
            RenderText.insert(INSERT,"복무기관 명 = "+ item.attrib["bmgigwanNm"]+"\n")
            strTitle = item.find("bjdsggjusoNm")
            RenderText.insert(INSERT,"복무 기관 주소 = "+ strTitle.text+"\n")
            strTitle = item.find("gsbaejeongPcnt")
            RenderText.insert(INSERT,"공석 배정 인원 수 = "+ strTitle.text+"\n")
            strTitle = item.find("jhgyehoekPcnt")
            RenderText.insert(INSERT,"집행 계획 인원 수 = "+ strTitle.text+"\n")
            strTitle = item.find("seonbalYn")
            RenderText.insert(INSERT,"선발 여부 = "+ strTitle.text+"\n")



def MakeHtmlDoc(BookList):
    from xml.dom.minidom import getDOMImplementation
    #get Dom Implementation
    impl = getDOMImplementation()
    
    newdoc = impl.createDocument(None, "html", None)  #DOM 객체 생성
    top_element = newdoc.documentElement
    header = newdoc.createElement('header')
    top_element.appendChild(header)

    # Body 엘리먼트 생성.
    body = newdoc.createElement('body')

    for bookitem in BookList:
        #create bold element
        b = newdoc.createElement('b')
        #create text node
        ibsnText = newdoc.createTextNode("gsteukiCd:" + bookitem[0])
        b.appendChild(ibsnText)

        body.appendChild(b)
    
        # BR 태그 (엘리먼트) 생성.
        br = newdoc.createElement('br')

        body.appendChild(br)

        #create title Element
        p = newdoc.createElement('p')
        #create text node
        titleText= newdoc.createTextNode("gsgicimId:" + bookitem[1])
        p.appendChild(titleText)

        body.appendChild(p)
        body.appendChild(br)  #line end

    #append Body
    top_element.appendChild(body)
    
    return newdoc.toxml()


def printBookList(blist):
    for res in blist:
        print (res)
    
def checkDocument():
    global BooksDoc
    if BooksDoc == None:
        print("Error : Document is empty")
        return False
    return True


#def sendMain():
