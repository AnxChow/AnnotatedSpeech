import matplotlib as mpl
mpl.use('TkAgg')
from matplotlib import pylab
from pylab import *
from scipy.io import wavfile

# reference: http://samcarcagno.altervista.org/blog/basic-sound-processing-python/?doing_wp_cron=1523395684.8911240100860595703125

sampFreq, snd = wavfile.read('test.wav')
s1 = snd[:,0]  #working with one channel only

# plot amplitude
timeArray = arange(0, snd.shape[0], 1)
timeArray = timeArray / sampFreq
timeArray = timeArray * 1000  #scale to milliseconds
plot(timeArray, s1, color='k')
plt.savefig( 'amp' )
ylabel('Amplitude')
xlabel('Time (ms)')
