from tkinter import *
from tkinter import messagebox
import re

class MainWindow(object):

    def __init__(self):
        self.root = Tk()

        self.frame = Frame(self.root)

        self.caption = Label(self.frame)

        self.label1 = Label(self.frame)
        self.label2= Label(self.frame)
        self.label3 = Label(self.frame)
        self.label4 = Label(self.frame)

        self.entry1 = Entry(self.frame)
        self.entry2 = Entry(self.frame)
        self.entry3 = Entry(self.frame)
        self.entry4 = Entry(self.frame)

        self.button1 = Button(self.frame)
        self.button2 = Button(self.frame)


    def config(self):
        self.root.title('Registration Form')

        self.root.resizable(False, False)

        self.caption.config(text='Registration',
                            font='Arial 16')
        self.label1.config(text='Login',
                           font='Isocpeur 14')
        self.label2.config(text='Password',
                           font='Isocpeur 14')
        self.label3.config(text='Password again',
                           font='Isocpeur 14')
        self.label4.config(text='Email',
                           font='Isocpeur 14')

        self.entry1.config(width=15, fg='red',
                           font='Isocpeur 14')
        self.entry2.config(width=15, fg='red',
                           font='Isocpeur 14')
        self.entry3.config(width=15, fg='red',
                           font='Isocpeur 14')
        self.entry4.config(width=15, fg='red',
                           font='Isocpeur 14')

        self.button1.config(text='save', width=10,
                            font='Arial 12')
        self.button2.config(text='cancel', width=10,
                            font='Arial 12')

    def layout(self):
        self.frame.pack(padx=10, pady=10)

        self.caption.grid(row=0, column=0, columnspan=2, pady = 15)

        self.label1.grid(row=1, column=0)
        self.label2.grid(row=2, column=0)
        self.label3.grid(row=3, column=0)
        self.label4.grid(row=4, column=0)

        self.entry1.grid(row=1, column=1)
        self.entry2.grid(row=2, column=1)
        self.entry3.grid(row=3, column=1)
        self.entry4.grid(row=4, column=1)

        self.button1.grid(row=5, column=0, pady=30)
        self.button2.grid(row=5, column=1, pady=30, padx=5)

    def save_handler(self, event):
        reg_str1 = r''
        reg_str2 = r''
        reg_str3 = r''

        pattern1 = re.compile(reg_str1)
        pattern2 = re.compile(reg_str2)
        pattern3 = re.compile(reg_str3)

        res1 = pattern1.match(self.entry1.get())
        res2 = pattern2.match(self.entry1.get())
        res3 = pattern3.match(self.entry1.get())

        if res1 is None:
            messagebox.showwarning('Warning', 'Login is not correct')

    def reset_handler(self, event):
        print(event)
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)

    def binding(self):
        self.button1.bind('<Button-1>', self.save_handler)
        self.button2.bind('<Button-1>', self.reset_handler)

    def run(self):
        self.config()
        self.layout()
        self.binding()
        self.root.mainloop()

