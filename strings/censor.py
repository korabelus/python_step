from tkinter import *
from tkinter import messagebox


# root:
root = Tk()
root.title('Шифровальщик')
root.geometry('700x350')
root.resizable(False, False)

# main_frame:
frame = Frame(root)
frame.pack(padx=10, pady=10)

# logo:
img = PhotoImage(file='download.png')
img = img.subsample(1, 1)
logo = Label(frame, image=img)
logo.pack(side='left')

# source_text:
source_text = Text(frame)
source_text.config(width=50, height=7,
                   font='Arial 11')
source_text.pack(padx=50)

# buttons:
panel = Frame(frame)
panel.pack(pady=10, padx=70)
b1 = Button(panel, text='Исправить', width=14,
            font='Arial 14')
b1.pack(side='left')

b2 = Button(panel, text='Сброс', width=14,
            font='Arial 14')
b2.pack(padx=15)

# target_text:
target_text = Text(frame)
target_text.config(width=50, height=7,
                   font='Arial 11')
target_text.pack(padx=50)


def correct_text(event):
    print(event)
    text1 = source_text.get('0.0', END)
    bad1 = 'bitch'
    text2 = text1.replace(bad1, 'girl')
    target_text.insert('0.0', text2)


def reset_text(event):
    print(event)
    source_text.delete('0.0', END)
    target_text.delete('0.0', END)


# run:
b1.bind('<Button-1>', correct_text)
b2.bind('<Button-1>', reset_text)
root.mainloop()
