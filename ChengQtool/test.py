import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
import tkinter.messagebox as mbx
import csv
import scipy.io as scio

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.chan_all = 1
        self.chan_sel = 1
        self.pack()
        self.Input1 = Entry(self)
        self.Input1.pack()
        self.Input2 = Entry(self)
        self.Input2.pack()
        self.alertButton = Button(self, text='确认', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name1 = self.Input1.get() or '1'
        name2 = self.Input2.get() or '1'
        mbx.showinfo('Message', '通道总数: %s ; 读取通道: %s' % (name1, name2))
        self.chan_all = int(name1) + 1
        self.chan_sel = int(name2) - 1
        chan_total = self.chan_all
        chan_sel = self.chan_sel
        fs = 1000
        channel = []
        for line in open("emp_test.csv"):
            time, data = line.split(",")
            # time = time.strip(' \t\r\n\"')
            data = data.strip(' \t\r\n\"')
            final = data.split(" ")
            # print(len(final)/104)
            for chan in range(int((len(final)) / chan_total)):
                # print(chan)
                channel.append(float(final[chan * chan_total + chan_sel]))
                # print(time + '\t' + channel[1])
        scio.savemat("channel" + name2 + ".mat", {"channel" + name2: channel})
        x = np.linspace(0, fs, len(channel))
        y = abs(np.fft.fft(channel, len(channel))) * 2 / len(channel)
        plt.subplot(2, 1, 1)
        plt.plot(channel)
        plt.subplot(2, 1, 2)
        plt.plot(x[0:int(len(x) / 2)], y[0:int(len(x) / 2)])
        plt.show()


app = Application()
app.master.title('设置通道数以及读取通道')
# app.mainloop()
app.mainloop()

#Pyinstaller

