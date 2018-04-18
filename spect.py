import os
import wave
import matplotlib as mpl
mpl.use('TkAgg')
from matplotlib import pylab
from pylab import *

def graph_spectrogram(wav_file):
    sound_info, frame_rate = get_wav_info(wav_file)
    pylab.figure(num=None, figsize=(19, 12))
    pylab.subplot(111)
    pylab.title('spectrogram of %r' % wav_file)
    spectrum=pylab.specgram(sound_info, Fs=frame_rate, NFFT=8192)
    pylab.savefig('spectrogram.png')
    
def get_wav_info(wav_file):
    wav = wave.open(wav_file, 'r')
    frames = wav.readframes(-1)
    sound_info = pylab.fromstring(frames, 'int16')
    frame_rate = wav.getframerate()
    wav.close()
    return sound_info, frame_rate

graph_spectrogram('test.wav')
print(get_wav_info('test.wav'))
