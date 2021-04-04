# This is just a voice recorder app, and nothing really fancy.

# All the imported modules here.
import sounddevice as sound_device
import soundfile as sound_file
from tkinter import *

from scipy.io.wavfile import write          # just in case


def voice_recorder():
    __frequency = 48000

    # Only last for 15 sec
    __duration = 15

    # Setting up the frequency and duration.
    myRecord = sound_device.rec(int(__duration * __frequency), samplerate = __frequency,
                                channels=2)

    sound_device.wait()

    # save the FLAC file, audio file
    return sound_file.write("my_audio.wav", myRecord, __frequency)

# Maybe in the future.
def stop():
    pass


# GUI
master = Tk()
master.title("Voice Recorder Ver.1")
Label(master, text = "Voice Recorder :").grid(row = 0, sticky = W, rowspan = 5)

b = Button(master, text = "Start", command = voice_recorder)
b.grid(row = 0, column = 2, columnspan = 2, rowspan = 2, padx = 5, pady = 5)

mainloop()
