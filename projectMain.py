from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.by import By
import pyperclip
import time
import tkinter.ttk
import newUi 
import newTime


def kAssert(f):
    while True:
        try:
            f()
            time.sleep(1)
            # login = driver.find_element(By.CLASS_NAME,'HeaderView_link_sign__jZmkX')
            break
        except:
            pass
        
#driver = {}
def step0():
    driver.get('https://weverse.io/')

def step1(): ## Sign in 버튼값 가져오기
    global login
    login = driver.find_element(By.CLASS_NAME,'HeaderView_link_sign__jZmkX')
    click()

def step2(): ## id 버튼값 가져오기 
    global login 
    login = driver.find_element(By.NAME,'userEmail')
    click()

def step3(): ## pw 버튼값 가져오기  
    global login
    login = driver.find_element(By.NAME,'password')
    click()

## ready
## -----------------------------------------

def step4(): ## notice 창 진입
    driver.get(newUi.values.url)
    
def addStep1(): ## 링크 클릭
    global login
    login =driver.find_element(By.CLASS_NAME,'gOuterLink')
    click()
    

def step5(): ## 성 입력
    driver.switch_to.window(driver.window_handles[-1])
    global login
    login = driver.find_element(By.ID,'requiredProperties-lastName')
    click()

def step6(): ## 이름 입력
    global login
    login = driver.find_element(By.ID,'requiredProperties-firstName')
    click()

def step7(): ## 생년월일 입력
    global login 
    login = driver.find_element(By.ID,'requiredProperties-birthDate')
    click()

## 원래본
"""
def step8(): ## 전화번호 입력
    global login 
    login = driver.find_element(By.ID, 'requiredProperties-phoneNumber')
    login.clear() ## 기존에 있었던 번호 삭제
    click()
    time.sleep(1)
"""
## 수정본
def step8():
    global login 
    login = driver.find_element(By.ID,'requiredProperties-phoneNumber')
    for i in range(len(login.get_attribute("value"))):
        login.send_keys(Keys.BACK_SPACE)

## 수정본 
def step9():
    checkboxes  = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
    for checkbox in checkboxes:
        driver.execute_script("arguments[0].click();", checkbox)    

## 원래본        
"""
def step9():
    global login
    login = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
    for checkbox in login:
       time.sleep(1)
       checkbox.click()
"""


def step10():
    global login
    login = driver.find_element(By.XPATH,"//input[@type='submit']")
    click()



def click(): ## form click()
    global login
    login.click()


def Paste(): ## id 값 복사해서 붙여넣기
    global login  
    pyperclip.copy(newUi.values.step7Value)
    login.send_keys(Keys.CONTROL, 'v')
    login.send_keys(Keys.ENTER)

def Paste2():   ## id 값 복사해서 붙여넣기 in application 
    global login  
    pyperclip.copy(newUi.values.step7Value)
    login.send_keys(Keys.CONTROL, 'v')
 

def project_main():
    newUi.main_pp()
    global driver
    driver = webdriver.Chrome()
    kAssert(step0)
    ## login button
    kAssert(step1)  ## Sing in 버튼값 가져오기 + click()
    ## input id newUi.values (id,pw,이동)
    kAssert(step2)   ## login id 버튼값 가져오기 + click()
    newUi.values.step7Value = newUi.values.user_id
    kAssert(Paste)   ## login id에 값 넣기
    ## input pw value
    kAssert(step3)  ## login pw 버튼값 가져오기 + click()
    newUi.values.step7Value = newUi.values.user_pw
    kAssert(Paste)  ## lgoin pw에 값 넣기
    
    ## Notice로 이동
    kAssert(step4)  
    ## application site 진입 링크 + click
    kAssert(addStep1)
    ## application site에서 값 넣기
    ## input lastName 
    kAssert(step5)     ## lastname form 값 찾아오기 
    newUi.values.step7Value = newUi.values.user_LastName
    kAssert(Paste2)     ## lastname form에 값 paste

    ## input firstName 
    kAssert(step6)     ## firstname form 값 찾아오기
    newUi.values.step7Value = newUi.values.user_FirstName
    kAssert(Paste2)     ## firstname form에 값 paste

    ## input birth
    kAssert(step7)     ## birth form 값 찾아오기
    newUi.values.step7Value = newUi.values.user_Birth
    kAssert(Paste2)     ## birth fo  rm에 값 paste

    ## input PhoneNuber
    kAssert(step8)     ## phoneNumber form 값 찾아오기
    newUi.values.step7Value = newUi.values.user_Pnumber
    kAssert(Paste2)     ## phonNumber form에 값 paste
    ## input 
    kAssert(step9)     ## check box에 v 체크 
    ## Ready 
    kAssert(step10)    ## 최종 sumit


## 메인 실행    
project_main()

