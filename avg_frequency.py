import os
import wave
import matplotlib as mpl
mpl.use('TkAgg')
from matplotlib import pylab
from pylab import *

def f(wav_file):
    sound_info, frame_rate = get_wav_info(wav_file)
    pylab.figure(num=None, figsize=(19, 12))
    pylab.subplot(111)
    pylab.title('spectrogram of %r' % wav_file)
    spectrum=pylab.specgram(sound_info, Fs=frame_rate, NFFT=8192)
    pylab.savefig('spectrogram.png')
    freqs=spectrum[1]
    t=spectrum[2]
    im=spectrum[3]
    spectrum=spectrum[0].T
    avg_freqs=[]
    for x in range(0,len(t)):
        sum=(np.dot(spectrum[x],freqs.T))
        avg_freqs.append(sum/np.sum(spectrum[x]))
    pylab.figure(num=None, figsize=(19, 12))
    pylab.subplot(111)
    pylab.title('avg freqs of %r' % wav_file)
    pylab.plot(t,avg_freqs)
    pylab.savefig(wav_file+'_avg_freq.png')

def get_wav_info(wav_file):
    wav = wave.open(wav_file, 'r')
    frames = wav.readframes(-1)
    sound_info = pylab.fromstring(frames, 'int16')
    frame_rate = wav.getframerate()
    wav.close()
    return sound_info, frame_rate

f('test.wav')
f('Pitches/hello1.wav')
f('Pitches/hello2.wav')

#A sound file does not have just a single "frequency" at any given time, unless it is just a recording of a pure sinusoidal tone. What you probably need to do is capture the power spectrum at regular intervals and store that, or possibly do some kind of processing on the power spectrum, such as identifying the largest N peaks and store those.
