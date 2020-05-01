from tkinter import *
from tkinter import messagebox
import re
import requests
from bs4 import BeautifulSoup


class MainWindow(object):

    def __init__(self):
        self.root = Tk()
        self.source = Entry(self.root)
        self.load = Button(self.root)
        self.data = Text(self.root)
        self.target = Entry(self.root)
        self.search = Button(self.root)
        self.result = Text(self.root)
        self.scroll1 = Scrollbar(self.root)
        self.scroll2 = Scrollbar(self.root)

    def config(self):
        self.root.title('Data analyzer')
        self.root.geometry('400x300')
        self.load.config(text="load")
        self.search.config(text="search")

        self.source.config(font='Consolas 12')
        self.data.config(font='Consolas 12')
        self.target.config(font='Consolas 12')
        self.result.config(font='Consolas 12')

        self.scroll1.config(command=self.data.yview)
        self.scroll2.config(command=self.result.yview)
        self.data.config(yscrollcommand=self.scroll1.set)
        self.result.config(yscrollcommand=self.scroll2.set)

    def layout(self):
        self.source.place(relwidth=0.5, height=30, relx=0.1, rely=0.05)
        self.load.place(relwidth=0.2, height=30, relx=0.65, rely=0.05)
        self.data.place(relwidth=0.9, relheight=0.3, relx=0.05, rely=0.18)
        self.target.place(relwidth=0.5, height=30, relx=0.1, rely=0.52)
        self.search.place(relwidth=0.2, height=30, relx=0.65, rely=0.52)
        self.result.place(relwidth=0.9, relheight=0.3, relx=0.05, rely=0.65)
        self.scroll1.place(width=20, relheight=0.4, relx=0.95, rely=0.09)
        self.scroll2.place(width=20, relheight=0.4, relx=0.95, rely=0.58)

    def load_data(self, event):
        print(event)
        path = self.source.get()
        self.data.delete('0.0', END)
        try:
            res = path.find('http')
            if res == 0:
               response = requests.get(path)
               content = response.content
               parser = BeautifulSoup(content, 'html.parser')
               html = parser.prettify()
               self.data.insert('0.0', html)
            else:
                with open(path, 'r', encoding='utf-8') as f:
                    data = f.read()

                self.data.insert('0.0', data)

        except BaseException as err:
            messagebox.showerror('run error', err)

    def search_result(self, event):
        print(event)
        request = self.target.get()
        pattern = re.compile(request)
        response = pattern.findall(self.data.get('0.0', END))
        counter = 0
        self.result.delete('0.0', END)
        for item in response:
            counter += 1
            self.result.insert(END, f'{counter} - {item} \n')

    def binding(self):
        self.load.bind('<Button-1>', self.load_data)
        self.search.bind('<Button-1>', self.search_result)

    def run(self):
        self.config()
        self.layout()
        self.binding()
        self.root.mainloop()


