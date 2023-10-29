# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
mytext = 'You are looking unhappy ?  disgusted for some reason'

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("disgusted.mp3")

# Playing the converted file
os.system("disgusted.mp3")







###!/usr/bin/env python
##import numpy as np
##import sys
##import cv2
##import os
##from mutagen.mp3 import MP3
##from gtts import gTTS
##import time
##import pygame
###print ("Enter the Text :")
###str=input()
###str=input()
###print (str)
###while True:
##    
###mtext = 'welcome to india welcome to india welcome to india '
##while True:
##    lag = 'en'
##    myobj = gTTS(text='Hey It seems your very happy . its nice to see you like this , have a good day', lang=lag, slow =False)
##    myobj.save("happy.mp3")
##    song = MP3("happy.mp3")
##    pygame.mixer.init()
##    pygame.mixer.music.load('happy.mp3')
##    pygame.mixer.music.play()
##    time.sleep(song.info.length)
##    pygame.quit()
