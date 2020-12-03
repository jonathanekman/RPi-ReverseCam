import RPi.GPIO as GPIO
import time
import subprocess
import os, signal
import pyautogui

GPIO.setmode(GPIO.BOARD)

GPIO.setup(5, GPIO.IN)
GPIO.setup(3, GPIO.OUT)


ok = True

try:
	while True:
		button_state = GPIO.input(5)

		if button_state == False and ok == True:
			GPIO.output(3, True) #LED ON
			print('ON')
			#Do Stuff HERE
			#subprocess.call(["./cam.sh"])
			proc1 = subprocess.Popen("./cam.sh")
			#Not here
			ok = False
			time.sleep(0.5)
			button_state = GPIO.input(5)

		if button_state == False and ok == False:
			GPIO.output(3, False) #LED OFF
			#
			#proc1.kill()
			#proc1.close()
			pyautogui.press('esc')
			#
			print('OFF')
			ok = True
			time.sleep(0.5)
			button_state = GPIO.input(5)
except:
	GPIO.cleanup()
