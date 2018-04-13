import urllib
import scipy.io.wavfile
import pydub
import matplotlib.pyplot as plt
import numpy as np

rate,audData=scipy.io.wavfile.read("test.wav")

#wav number of channels mono/stereo
audData.shape[1]
#if stereo grab both channels
channel1=audData[:,0] #left
channel2=audData[:,1] #right

#create a time variable in seconds
time = np.arange(0, float(audData.shape[0]), 1) / rate

#plot amplitude (or loudness) over time
plt.figure(1)
plt.subplot(211)
plt.plot(time, channel1, linewidth=0.01, alpha=0.7, color='#ff7f00')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.subplot(212)
plt.plot(time, channel2, linewidth=0.01, alpha=0.7, color='#ff7f00')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.savefig('amp2.png')
