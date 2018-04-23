import matplotlib as mpl
mpl.use('TkAgg')
from matplotlib import pylab
from pylab import *
from scipy.io import wavfile
import math

# reference: http://samcarcagno.altervista.org/blog/basic-sound-processing-python/?doing_wp_cron=1523395684.8911240100860595703125

sampFreq, snd = wavfile.read('Cats/cats_un_ro.wav')
snd = snd / (2.**15)
s1 = snd[:,0]  #working with one channel only

# plot amplitude
timeArray = arange(0, snd.shape[0], 1)
timeArray = timeArray / sampFreq
timeArray = timeArray * 1000  #scale to milliseconds

knownTime=[1470, 1634, 2124, 2500, 4002]

start=0 #holds start ms value
ampVals=[] #to hold avg amp vals of word
sum=0.0
for x in knownTime: #go through the word end times
    for i in range(start,x): #go through the word
        sum=sum+s1[i]
    ampVals.append(20*(math.log10(abs(sum/(x-start))))) #avg
    start=x
#should we hold max value or the avg value? (amplitude)
print(ampVals)

plot(timeArray, s1, color='k')
ylabel('Amplitude')
xlabel('Time (ms)')
plt.savefig( 'amp' )
