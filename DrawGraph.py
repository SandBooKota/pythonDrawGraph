import pandas as pd
import matplotlib.pyplot as plt
import os,sys
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

def button1_clicked():
    fTyp = [("","*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    filepath = filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
    file1.set(filepath)

def button2_clicked():
    #先頭3行目, 末尾1行はスキップして読み込む
    df = pd.read_csv(file1.get(), header=None, skiprows=4, skipfooter=3, engine='python')
    t = df[0]
    y1 = df[1]
    y2 = df[2]
    y3 = df[3]
    y4 = df[4]
    plt.plot(t, y1)
    plt.plot(t, y2)
    plt.plot(t, y3)
    plt.plot(t, y4)
    plt.show()

if __name__ == '__main__':
    # rootの作成
    root = Tk()
    root.geometry("500x350")
    root.title('Draw')
    root.resizable(False, False)

    # Frame1の作成
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    # ボタンの作成
    button1 = ttk.Button(root, text=u'File open', command=button1_clicked)
    button1.grid(row=0, column=3)

    file1 = StringVar()
    file1_entry = ttk.Entry(frame1, textvariable=file1, width=45)
    file1_entry.grid(row=0, column=2)

    button2 = ttk.Button(root, text=u'Draw', command=button2_clicked)
    button2.grid(row=2, column=3)

    root.mainloop()
