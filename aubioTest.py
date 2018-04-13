#! /usr/bin/env python

from aubio import source, pitch

pitches=pitch('test.wav')
plot(pitch[0],pitch[1])
