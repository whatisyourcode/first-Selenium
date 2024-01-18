from tkinter import *
import tkinter.ttk 
## project import!!!
tk = Tk()               ## 윈도우 객체 생성
tk.title('Weverse')     ## 윈도우 title name
tk.geometry('360x180')  ## 윈도우 크기 ## 350 x 160
tk.resizable(False, False) ## 윈도우 크기를 고정 (x축,y축) , True = 조절 가능 False = 조절 불가능

values=[str(i)+"" for i in range(0, 25)] 
values2=[str(i)+"" for i in range(0,61)]



## ms 값 3개
def validate_text(new_text):
    if len(new_text) > 3:
        return False
    return True

def close_window():
    tk.destroy()

## 비밀번호 체크하는 함수
def check_entry():
    if text_Class.text1.get() == '1234':
        button_Class.button1.config(state='normal')
    else:
        button_Class.button1.config(state='disabled')


class user_input:
    def __init__(self,p_Password,user_id,user_pw,user_LastName,user_FirstName,user_Birth,user_Pnumber,hour,minute,second,ms,url):
        self.p_Password = p_Password
        self.user_id = user_id
        self.user_pw = user_pw
        self.user_LastName = user_LastName
        self.user_FirstName = user_FirstName
        self.user_Birth = user_Birth
        self.user_Pnumber = user_Pnumber
        self.hour = hour
        self.minute = minute
        self.second = second
        self.ms = ms
        self.url = url
    step7Value = ''

def play():
    global values
    values = user_input(text_Class.text1.get(),text_Class.text2.get(),text_Class.text3.get(),
                        text_Class.text4.get(),text_Class.text5.get(),text_Class.text6.get(),
                        text_Class.text7.get(),combobox_Class.combobox8.get(),combobox_Class.combobox9.get(),
                        combobox_Class.combobox10.get(),text_Class.text11.get(),text_Class.text12.get())



## label values
class label_Class: 
    lab1 = Label(tk,text='프로그램 비밀번호',fg='red')
    lab2 = Label(tk,text='로그인 아이디')
    lab3 = Label(tk,text='로그인 비밀번호')
    lab4 = Label(tk,text='성')
    lab5 = Label(tk,text='이름')
    lab6 = Label(tk,text='생년월일')
    lab7 = Label(tk,text='연락처')
    lab8 = Label(tk,text=' 시')
    lab9 = Label(tk,text=' 분')
    lab10 = Label(tk,text=' 초')
    lab11 = Label(tk,text=' ms')
    lab12 = Label(tk,text='URL 주소',fg='blue')

class text_Class:
    ## text values
    text1 = Entry(tk,width=20)
    text2 = Entry(tk,width=20)
    text3 = Entry(tk,width=20)  
    text4 = Entry(tk,width=20)
    text5 = Entry(tk,width=20)
    text6 = Entry(tk,width=20)
    text7 = Entry(tk,width=20)
    ## text11 = ms , text12 = URL
    text11 = Entry(tk,width=5)
    text12 = Entry(tk,width=20)

    vcmd = tk.register(validate_text)
    text11.configure(validate="key", validatecommand=(vcmd, "%P"))
    text1.bind("<KeyRelease>", lambda event: check_entry()) ## 프로그램 비밀번호 event


class combobox_Class:
    combobox8 = tkinter.ttk.Combobox(tk, width=2, values=values)
    combobox9 = tkinter.ttk.Combobox(tk, width=2, values=values2)
    combobox10 = tkinter.ttk.Combobox(tk, width=2, values=values2)
    combobox8.set('0') ## 초기값
    combobox9.set('0') ## 초기값
    combobox10.set('0') ## 초기값



     ## function

def event():
    button_Class.button1['text']='Running..'

def label_Grid():
    label_Class.lab1.grid(row=1,column=1)
    label_Class.lab2.grid(row=2,column=1)
    label_Class.lab3.grid(row=3,column=1)
    label_Class.lab4.grid(row=4,column=1)
    label_Class.lab5.grid(row=5,column=1)
    label_Class.lab6.grid(row=6,column=1)
    label_Class.lab7.grid(row=7,column=1)
    label_Class.lab8.grid(row=1,column=5)
    label_Class.lab9.grid(row=2,column=5)
    label_Class.lab10.grid(row=3,column=5)
    label_Class.lab11.grid(row=4,column=5)
    label_Class.lab12.grid(row=8,column=1)

def text_Grid():
    text_Class.text1.grid(row=1,column=3)
    text_Class.text2.grid(row=2,column=3)
    text_Class.text3.grid(row=3,column=3)
    text_Class.text4.grid(row=4,column=3)
    text_Class.text6.grid(row=6,column=3)
    text_Class.text5.grid(row=5,column=3)
    text_Class.text7.grid(row=7,column=3)
    text_Class.text12.grid(row=8,column=3)
    text_Class.text11.grid(row=4,column=6) ## ms
    text_Class.text12.grid(row=8,column=3) ## URL 

def combobox_Grid():
    combobox_Class.combobox8.grid(row=1,column=6)
    combobox_Class.combobox9.grid(row=2,column=6)
    combobox_Class.combobox10.grid(row=3,column=6)

def button_Grid():
    button_Class.button1.grid(row=8,column=6)

    

class button_Class:
    button1 = Button(tk,text="Run",width=8,command=lambda:(play(),close_window()) ,state='disabled')



def main_pp():
    label_Grid()
    text_Grid()
    combobox_Grid()
    button_Grid()
    check_entry()
    tk.mainloop()