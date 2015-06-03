#!/usr/bin/python3

from subprocess import call


def synth(duration, startFreq, endFreq=False):
    cmd = 'play -n synth sin' + startFreq + ' ' + duration
    call(cmd, shell=True)
