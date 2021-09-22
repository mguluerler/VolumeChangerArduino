import serial
import time
import math


class VolumeChangerArduino():
    def __init__(self, port="COM6", baudrate=115200, sleeptime=0.001):
        self.arduino = serial.Serial(port=port, baudrate=baudrate, timeout=1)
        self.sleeptime = sleeptime
        self.serialData = ""
        self.volume_level = 0
        self.older_volume = 0
        self.popt = []
        self.funcCreator()
        self.volumeSetup()

    @staticmethod
    def volumeFormatter(x, a, b, c):
        return a * x ** 2 + b * x + c
#Converts volume percentage for pycaw
    def funcCreator(self):
        import numpy as np
        from scipy.optimize import curve_fit
        self.xdata = [0, 2, 3, 7, 13, 23, 27, 35, 45, 59, 77, 82, 88, 94, 100]
        ydata = [76, 60, 52, 40, 31, 22, 20, 16, 12, 8, 4, 3, 2, 1, 0]
        x = np.array(self.xdata, dtype=float)  # transform your data in a numpy array of floats
        y = np.array(ydata, dtype=float)  # so the curve_fit can work
        for i in range(0, len(self.xdata) - 2, 2):
            self.popt.append("")
            self.popt[int(i / 2)], _ = curve_fit(VolumeChangerArduino.volumeFormatter, [x[i], x[i + 1], x[i + 2]],
                                                             [y[i], y[i + 1], y[i + 2]])
#Setups volume tools
    def volumeSetup(self):
        from ctypes import cast, POINTER
        from comtypes import CLSCTX_ALL
        from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        self.volume = cast(interface, POINTER(IAudioEndpointVolume))
        self.volume.GetMute()
        self.volume.GetMasterVolumeLevel()
        self.volume.GetVolumeRange()

    def serialGetData(self):
        self.serialData = ""
        while self.arduino.in_waiting > 0:
            self.serialData += self.arduino.read().decode("ascii")
        return self.serialData

    def volumeChanger(self):
        while True:
            self.serialGetData()
            if self.serialData != "":
                if "\n" in self.serialData:
                    self.volume_level = int(self.serialData.rstrip().split("\r\n")[-1])
                elif type(self.serialData) == str:
                    self.volume_level = int(self.serialData)
                time.sleep(self.sleeptime * 10)
                if self.older_volume != self.volume_level:
                    if self.volume_level == 100:
                        self.volume.SetMasterVolumeLevel(0, None)
                    else:
                        for i in range(0, len(self.xdata)-2, 2):
                            if self.volume_level <= self.xdata[i+2] and self.volume_level >= self.xdata[i]:
                                self.volume.SetMasterVolumeLevel(-1*(VolumeChangerArduino.volumeFormatter(self.volume_level, *self.popt[int(i/2)])), None)
                    self.older_volume = self.volume_level
            self.serialData = ""
            time.sleep(self.sleeptime)

    def widgetOperations(self, widget_latency, position, taskbar_thick, size, transparency, margin):
        import tkinter

        def volumeWatcher():
            label.config(text=self.volume_level)
            label.after(widget_latency, volumeWatcher)

        widget = tkinter.Tk()
        self.widget = widget
        ws, hs = widget.winfo_screenwidth(), widget.winfo_screenheight()
        if size <= 1:
            fontsize = math.floor(hs*size)
        else:
            fontsize = math.floor(size)
        label = tkinter.Label(widget, font=("digital numbers", fontsize), background="#1B1E26", foreground="#FFE222")
        label.pack(anchor="center")
        label.master.overrideredirect(True)
        positions_dict = {"b": "-", "t": "+", "l": "+", "r": "-"}
        if position[2] == position[1]:
            label.master.geometry('{0}{1}{2}{3}'.format(positions_dict[position[1]], int(math.floor(ws * taskbar_thick + margin)), positions_dict[position[0]], int(math.floor(margin))))
        elif position[2] == position[0]:
            label.master.geometry('{0}{1}{2}{3}'.format(positions_dict[position[1]], int(math.floor(margin)), positions_dict[position[0]], int(math.floor(hs * taskbar_thick + margin))))
        else:
            label.master.geometry('{0}{1}{2}{3}'.format(positions_dict[position[1]], int(math.floor(margin)), positions_dict[position[0]], int(math.floor(margin))))

        # label.master.wm_attributes("-transparentcolor","#FFE221")
        label.master.wm_attributes("-alpha",transparency)
        label.master.wm_attributes("-topmost", True)
        label.master.lift()
        volumeWatcher()
        widget.mainloop()

    def useWidget(self, widget_latency=10, position="brb", taskbar_thick=0.03, size=0.08, transparency=1, margin=0):
        import threading
        self.widgetThread = threading.Thread(target=self.widgetOperations, args=(widget_latency,position,taskbar_thick,size,transparency,margin,))
        self.widgetThread.start()

    def closeWidget(self):
        self.widget.quit()

    def run(self):
        self.volumeChanger()

if __name__ == "__main__":
    x = VolumeChangerArduino()
    x.useWidget()
    x.run()