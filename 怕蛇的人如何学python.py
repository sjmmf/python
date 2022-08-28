'''
通过tkinter实现了图形界面

实现的功能：切换文本，添加文本，删除文本（删一行或者删所有），重置，显示正确率、每秒字符数以及所用时间
'''
from tkinter import *           #导入tkinter库
import time
import os
from random import choice

'''
记得在开始测试之前点击“重置”按钮，并且在.py同目录下手动创建一个text.txt
'''
#对图形窗口进行封装
class GUI:
    def __init__(self) :
        self.start_time = 0
        self.sentence_words_num = 0
        self.sentence = ''
        self.root = Tk()
        self.root.title('Python打字速度测试   作者——lmsyyds')
        self.root.geometry('900x500+300+100')
        self.root.config(bg='lightgreen')
        self.interface()

    #此方法用于主界面
    def interface(self):
        #此部分对应大标题
        Label(self.root,text='Python打字速度测试',anchor=CENTER,font=('宋体',30,'bold'),bg='yellow',fg='red').place(x=260,y=30)
        
        #此部分对应文本显示框
        self.text_show_label = Label(self.root,text='当前无文本',wraplength=400,anchor=CENTER,font=('宋体',15,'bold'),bg='yellow',fg='red',width=40,justify=LEFT)
        self.text_show_label.place(x=250,y=150)
    
        #此部分对应输入框
        self.text = StringVar()
        self.text.trace("w",lambda name,index,mode,text=self.text:self.check(text))
        self.input_entry = Entry(self.root,font=('宋体',15,'bold'),width=40,textvariable=self.text)
        self.input_entry.place(x=250,y=250)

        #此部分对应“重置”按钮
        button1 = Button(self.root,text='重置',font=('宋体',18,'bold'),width=12,bg='yellow',fg='red',command=self.Reset,relief='groove',cursor='heart')
        button1.place(x=120,y=320)

        #此部分对应“切换文本”按钮
        button2 = Button(self.root,text='切换文本',font=('宋体',18,'bold'),width=12,bg='yellow',fg='red',command=self.getSentence,relief='groove',cursor='heart')
        button2.place(x=360,y=320)

        #此部分对应“时间”按钮
        button3 = Button(self.root,text='时间',font=('宋体',18,'bold'),width=12,bg='yellow',fg='red',command=self.time_result,relief='groove',cursor='heart')
        button3.place(x=600,y=320)

        #此部分对应“添加文本”按钮
        button4 = Button(self.root,text='添加文本',font=('宋体',18,'bold'),width=12,bg='yellow',fg='red',command=self.init_child_root,relief='groove',cursor='heart')
        button4.place(x=240,y=420)

        #此部分对应“删除文本”按钮
        button5 = Button(self.root,text='删除文本',font=('宋体',18,'bold'),width=12,bg='yellow',fg='red',command=self.init_delete_root,relief='groove',cursor='heart')
        button5.place(x=500,y=420)

        #此部分用于速度显示
        self.speed_label = Label(self.root,text='速度：00 字每秒',font=('宋体',15,'bold'),bg='yellow',fg='red')
        self.speed_label.place(x=120,y=380)

        #此部分用于显示准确率
        self.accuracy_label = Label(self.root,text='准确率：00%',font=('宋体',15,'bold'),bg='yellow',fg='red')
        self.accuracy_label.place(x=380,y=380)

        #此部分用于显示所用时间
        self.time_label = Label(self.root,text='时间：0 秒',font=("宋体",15,'bold'),bg='yellow',fg='red')
        self.time_label.place(x=620,y=380)

    #“重置”方法实现
    def Reset(self):
        self.input_entry.config(state=NORMAL)
        self.input_entry.delete(0,END)
        self.start_time = 0
        self.speed_label.config(text='速度：00 字每秒')
        self.accuracy_label.config(text='准确率：00%')
        self.time_label.config(text='时间：0 秒')

    #“切换文本”方法实现
    def getSentence(self):
        self.Reset()
        with open('/home/lmsubuntu/桌面/python_code/怕蛇的人如何学 Python/text.txt', 'r', encoding='utf-8') as f:
            sentence = f.readlines()
            self.sentence = choice(sentence).rstrip()
            self.text_show_label.config(text=self.sentence)
            self.sentence_words_num = len(self.sentence)

    #"时间"方法实现
    def time_result(self):
        segment = round(time.time()-self.start_time)
        input_text = self.text.get()
        ch_per_second = round(len(input_text)/segment)            #每秒字符数计算
        count = 0
        for index, char in enumerate(input_text):
            if self.sentence[index] == char:
                count = count + 1
        accuracy = round((count/self.sentence_words_num)*100)     #正确率计算
        self.speed_label.config(text='速度：{} 字每秒'.format(ch_per_second))
        self.accuracy_label.config(text='准确率：{}%'.format(accuracy))
        self.time_label.config(text='时间：{} 秒'.format(segment))

    #“检查”方法的实现
    def check(self,text):
        if self.start_time == 0 and len(text.get()) == 1:
            self.start_time = time.time()
        elif len(text.get()) == self.sentence_words_num:
            self.input_entry.config(state=DISABLED)
            self.time_result()

    #“添加文本”子窗口
    def init_child_root(self):
        #此处用于规划子界面
        self.child_root = Toplevel(self.root)
        self.child_root.geometry('450x450')
        self.child_root.title('添加文本')
        self.child_root.config(bg='lightblue')
        
        #此处对应子窗口输入框
        self.child_input_entry = Entry(self.child_root,width=80)
        self.child_input_entry.pack()
        
        #此处对应子窗口“重置”按钮
        child_button1 = Button(self.child_root,text='重置',font=('宋体',18,'bold'),width=12,bg='yellow',fg='red',command=self.child_reset,relief='groove',cursor='heart')
        child_button1.place(x=50,y=300)

        #此处对应子窗口“保存”
        child_button2 = Button(self.child_root,text='保存',font=('宋体',18,'bold'),width=12,bg='yellow',fg='red',command=self.child_text_save,relief='groove',cursor='heart')
        child_button2.place(x=250,y=300)

    #添加文本子窗口“重置”方法实现
    def child_reset(self):
        self.child_input_entry.config(state=NORMAL)
        self.child_input_entry.delete(0,END)
    
    #添加文本子窗口“保存”方法实现
    def child_text_save(self):
        child_text = self.child_input_entry.get()
        with open('/home/lmsubuntu/桌面/python_code/怕蛇的人如何学 Python/text.txt', 'a+', encoding='utf-8') as f:
            f.write('\n'+child_text)
            f.close()
    
    #“删除文本”子窗口
    def init_delete_root(self):
        #此处用于规划子界面
        self.delete_root = Toplevel(self.root)
        self.delete_root.geometry('300x300+100+100')
        self.delete_root.title('删除文本')
        self.delete_root.config(bg='orange')

        #此处对应子窗口“删除第一行”按钮
        delete_per_row_button = Button(self.delete_root,text='删除第一行',font=('宋体',18,'bold'),width=12,bg='yellow',fg='red',command=self.per_row_delete,relief='groove',cursor='heart')
        delete_per_row_button.place(x=70,y=100)

        #此处对应子窗口“删除全部”按钮
        delete_all_button = Button(self.delete_root,text='删除全部',font=('宋体',18,'bold'),width=12,bg='yellow',fg='red',command=self.all_delete,relief='groove',cursor='heart')
        delete_all_button.place(x=70,y=200)
 
    #删除文本子窗口“删除第一行”方法实现
    def per_row_delete(self):
        with open('/home/lmsubuntu/桌面/python_code/怕蛇的人如何学 Python/text.txt', 'r', encoding='utf-8') as f:
            line = f.readlines()
            try:
                line = line[1:]
                f = open('/home/lmsubuntu/桌面/python_code/怕蛇的人如何学 Python/text.txt', 'w', encoding='utf-8')
                f.writelines(line)
                f.close()
            except:
                pass

    #删除文本子窗口“删除全部”方法实现
    def all_delete(self):
        with open('/home/lmsubuntu/桌面/python_code/怕蛇的人如何学 Python/text.txt', 'r', encoding='utf-8') as f:
            line = f.readlines()
            length = len(line)
            for index in range(0,length):
                try:
                    line = line[1:]
                    f = open('/home/lmsubuntu/桌面/python_code/怕蛇的人如何学 Python/text.txt', 'w', encoding='utf-8')
                    f.writelines(line)
                    f.close()
                except:
                    pass

if __name__ == '__main__':
    window = GUI()
    window.root.mainloop()