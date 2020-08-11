# SDRConsole-to-SDR-compatible-IQ-converter
An RF64 wav audio converter to smaller endian and manual normalizer, for replaying IQ files in SDR#
Hi! Welcome to the app! This app is intended to process SDRConsole IQ recordings into SDR Sharp playable IQ recordings.

The requirements are:

- Modules: tkinter.

It's intended for python3.8.2.

It utilizes ffmpeg binaries from https://ffbinaries.com/downloads and the libav codec.



________________________
# Goals:

Wrote the app. ✔️

Confirmed Working on Windows. ✔️

Port for Linux. 📝 TODO

Write a better GUI. 📝 TODO

Write an automatic audio normalizer to -3dBFS. 📝 TODO

Add multiprocessing support for libav and asynchronous processing of files. 📝 TODO
