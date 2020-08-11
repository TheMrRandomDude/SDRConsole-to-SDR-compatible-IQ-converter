#Required modules: tkinter
#Required binaries: ffmpeg binary, download from: https://ffbinaries.com/downloads

import tkinter
from tkinter import filedialog
import os
import sys
from time import sleep

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

root = tkinter.Tk()
root.withdraw()

print("Hi! Welcome to the app! This app is intended to process SDRConsole IQ recordings into SDR Sharp playable IQ recordings")
sleep(1)
print("Please select the file or files which you want processed!")
sleep(2)

filez = filedialog.askopenfilenames(parent=root,title='Choose a file or files')
lst = list(filez)

sleep(1)

print("Choose the output directory!")

sleep(1)

folder_selected = filedialog.askdirectory()

lokacija = resource_path('ffmpeg.exe')
os.chdir(os.path.dirname(lokacija))

for path in lst:
    outpath = str(os.path.join(folder_selected + os.sep + "Converted_SDRSharp_Compatible_" + str(os.path.splitext(os.path.basename(path))[0]) + str(os.path.splitext(path)[1]))).replace("\\", "/")
    print(outpath)
    
    komanda = 'ffmpeg.exe -i "' + str(path) + '" -filter:a "volume=-66dB" -c:a pcm_s32le -rf64 auto "' + str(outpath) + '"'
    os.system(komanda)
    
print("Thank you for using the app! Repo: https://github.com/TheMrRandomDude/SDRConsole-to-SDR-compatible-IQ-converter")
print('Press Enter to exit or click "X"!')
input()
