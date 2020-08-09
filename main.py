#Required modules: tkinter, ffmpeg-python
#Can be installed with pip (pip3 on linux)
#Confirmed Working on Linux

import ffmpeg
import tkinter
from tkinter import filedialog
import os
from time import sleep

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

for path in lst:
    outpath = str(os.path.join(folder_selected + os.sep + "Converted_SDRSharp_Compatible_" + str(os.path.splitext(os.path.basename(path))[0]) + str(os.path.splitext(path)[1]))).replace("\\", "/")
    print(outpath)
    try:
        (
            ffmpeg
            .input(path)
            .filter("volume", "-66dB")
            .output(outpath, acodec='pcm_s32le', loglevel="quiet")
            .run(capture_stdout=True, capture_stderr=True)
        )

    except ffmpeg.Error as e:
        print('stdout:', e.stdout.decode('utf8'))
        print('stderr:', e.stderr.decode('utf8'))
        raise e

print("Thank you for using the app! Repo: https://github.com/TheMrRandomDude/SDRConsole-to-SDR-compatible-IQ-converter")
sleep(3.5)
#ffmpeg equivalent command:
#ffmpeg -i "07-Aug-2020 224207.870 101.830MHz.wav" -filter:a "volume=-66dB" -c:a pcm_s32le output.wav
