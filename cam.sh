#!/bin/bash

mplayer tv:// -tv driver=v4l2:norm=PAL_BGHIN:width=360:height=240:outfmt=uyvy:device=/dev/video0:input=1:fps=10 -vo sdl -hardframedrop -msglevel all=6 -fs
