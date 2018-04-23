import wave
import struct
import sys
import matplotlib as mpl
mpl.use('TkAgg')
from matplotlib import pylab
from pylab import *
from scipy.io import wavfile
import math

def wav_to_floats(wave_file):
    w = wave.open(wave_file)
    astr = w.readframes(w.getnframes())
    # convert binary chunks to short
    a = struct.unpack("%ih" % (w.getnframes()* w.getnchannels()), astr)
    a = [float(val) / pow(2, 15) for val in a]
    return a


signal1 = wav_to_floats('Cats/cats_un_anx.wav')
signal2 = wav_to_floats('Cats/cats_cert_anx.wav')
timeArray1 = arange(0, len(signal1))
timeArray2 = arange(0, len(signal2))

pylab.figure(num=None, figsize=(19, 12))
pylab.subplot(111)
pylab.title('Pitch')
pylab.plot(timeArray1,signal1)
pylab.plot(timeArray2,signal2)
pylab.legend(('uncert','cert'))
pylab.savefig('cats_amp_anx.png')
