import webbrowser 
import cv2 
import pytesseract
import pyautogui
import time
import sqlite3
import win32api, win32con
import numpy

IMG_PATH = 'tmp/last.png'
PX = 990
PY = 450
sqliteConnection = sqlite3.connect('database.sqlite')
cursor = sqliteConnection.cursor()
print("Database created and Successfully Connected to SQLite")

def checkConnection(path):
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV) 
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
    dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    im2 = img.copy()
    for cnt in contours: 
        x, y, w, h = cv2.boundingRect(cnt)
        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cropped = im2[y:y + h, x:x + w]
        text = pytesseract.image_to_string(cropped)
        if "Prét a participer" in text:
            return True
    return False
def screen():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(IMG_PATH)
    print("done screen")
def getUrl():
    sqlite_select_Query = "select * from histories where done = 0 order by id DESC"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchone()
    if record != None :
        return record[2]
    return None
def setDone():
    sql = ' UPDATE histories SET done = 1 '
    cursor.execute(sql)
    sqliteConnection.commit()
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
def go():
    while True:
        time.sleep(5)
        url = getUrl()
        if url != None:
            setDone()
            print("done")
            webbrowser.open_new(url)
            time.sleep(2)
            screen()
            i=0
            while i<10:
                if checkConnection(IMG_PATH) :
                    click(PX,PY)
                    break    
                screen()
                i+=1
                time.sleep(1)
                print(f'connecting...{i}')
    
go()