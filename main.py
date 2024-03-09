import math, time, threading
import requests, subprocess
from pynput import keyboard
# from LCD.Adafruit_CharLCD import Adafruit_CharLCD as Display
# import RPi.GPIO as GPIO

class Emulator:
	HIGH=0
	LOW=1
	inputstring = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
	def input(self, name):
		out=0
		value = open("file.txt", "r").readlines()

		# value = value[0]

		# value.split(sep=None, maxsplit=-1)

		value = self.inputstring


		if name==17:	# 0

			if (value[0]=="1"):
				out = 1
			elif (value[0]=="0"):
				out = 0
			return(out)
		

		elif name==0:	# 1

			if (value[1]=="1"):
				out = 1
			elif (value[1]=="0"):
				out = 0
			return(out)
		
		elif name==22:	# 2

			if (value[2]=="1"):
				out = 1
			elif (value[2]=="0"):
				out = 0
			return(out)

		elif name==27:	# 3

			if (value[3]=="1"):
				out = 1
			elif (value[3]=="0"):
				out = 0
			return(out)
		
		elif name==4:	# 4

			if (value[4]=="1"):
				out = 1
			elif (value[4]=="0"):
				out = 0
			return(out)
		
		elif name==16:	# 5

			if (value[5]=="1"):
				out = 1
			elif (value[5]=="0"):
				out = 0
			return(out)
		
		elif name==24:	# 6

			if (value[6]=="1"):
				out = 1
			elif (value[6]=="0"):
				out = 0
			return(out)
		
		elif name==23:	# 7

			if (value[7]=="1"):
				out = 1
			elif (value[7]=="0"):
				out = 0
			return(out)
		
		elif name==25:	# 8

			if (value[8]=="1"):
				out = 1
			elif (value[8]=="0"):
				out = 0
			return(out)
		
		elif name==1:	# 9

			if (value[9]=="1"):
				out = 1
			elif (value[9]=="0"):
				out = 0
			return(out)
		
		elif name==18:	# =

			if (value[10]=="1"):
				out = 1
			elif (value[10]=="0"):
				out = 0
			return(out)
		
		elif name==12:	# C

			if (value[11]=="1"):
				out = 1
			elif (value[11]=="0"):
				out = 0
			return(out)
		
		elif name==20:	# CE

			if (value[12]=="1"):
				out = 1
			elif (value[12]=="0"):
				out = 0
			return(out)
		
	def on_press(self,key):
		pressed = ""
		key_is_normal = False
		passed = False
		try:
			pressed=key.char
			key_is_normal = True
		except AttributeError:
			pressed = key
			key_is_normal = False

		if(key_is_normal==True):
			if (pressed=="a"):
				passed = False
			elif(pressed==None):    # 5
				self.inputstring[5] = "1"
				passed = True
		else:
			if(pressed==key.insert):    # 0
				self.inputstring[0] = "1"
				passed = True
			elif(pressed==key.end):    # 1
				self.inputstring[1] = "1"
				passed = True
			elif(pressed==key.down):    # 2
				self.inputstring[2] = "1"
				passed = True
			elif(pressed==key.page_down):    # 3
				self.inputstring[3] = "1"
				passed = True
			elif(pressed==key.left):    # 4
				self.inputstring[4] = "1"
				passed = True
			
			elif(pressed==key.right):    # 6
				self.inputstring[6] = "1"
				passed = True
			elif(pressed==key.home):    # 7
				self.inputstring[7] = "1"
				passed = True
			elif(pressed==key.up):    # 8
				self.inputstring[8] = "1"
				passed = True
			elif(pressed==key.page_up):    # 9
				self.inputstring[9] = "1"
				passed = True
			elif(pressed==key.enter):    # ENTER
				self.inputstring[10] = "1"
				passed = True
			elif(pressed==key.backspace):    # CLEAR
				self.inputstring[11] = "1"
				passed = True
			elif(pressed==key.delete):    # CLEAR EVERYTHING
				self.inputstring[12] = "1"
				passed = True


			elif(pressed==key.esc):
				exit()

			

		print("Pressed " + str(pressed))
		if passed:

			buffer = ""

			for e in self.inputstring:
				buffer+=e

			print(buffer)

			f = open("file.txt", "w")
			f.write(buffer)
			f.close()

	def on_release(self, key):
		pressed = ""
		passed = False
		key_is_normal = False
		try:
			# print(f"Key {key.char} pressed")
			pressed=key.char
			key_is_normal = True
		except AttributeError:
			# print(f"Special key {key} pressed")
			
			pressed = key
			key_is_normal = False
		
		if(key_is_normal==True):
			if (pressed=="a"):
				passed = False
			elif(pressed==None):    # 5
				self.inputstring[5] = "0"
				passed = True
		else:
			if(pressed==key.insert):    # 0
				self.inputstring[0] = "0"
				passed = True
			elif(pressed==key.end):    # 1
				self.inputstring[1] = "0"
				passed = True
			elif(pressed==key.down):    # 2
				self.inputstring[2] = "0"
				passed = True
			elif(pressed==key.page_down):    # 3
				self.inputstring[3] = "0"
				passed = True
			elif(pressed==key.left):    # 4
				self.inputstring[4] = "0"
				passed = True
			
			elif(pressed==key.right):    # 6
				self.inputstring[6] = "0"
				passed = True
			elif(pressed==key.home):    # 7
				self.inputstring[7] = "0"
				passed = True
			elif(pressed==key.up):    # 8
				self.inputstring[8] = "0"
				passed = True
			elif(pressed==key.page_up):    # 9
				self.inputstring[9] = "0"
				passed = True
			elif(pressed==key.enter):    # ENTER
				self.inputstring[10] = "0"
				passed = True
			elif(pressed==key.backspace):    # CLEAR
				self.inputstring[11] = "0"
				passed = True
			elif(pressed==key.delete):    # CLEAR EVERYTHING
				self.inputstring[12] = "0"
				passed = True


			elif(pressed==key.esc):
				exit()



		print("Pressed " + str(pressed))
		if passed:

			buffer = ""

			for e in self.inputstring:
				buffer+=e

			print(buffer)

			f = open("file.txt", "w")
			f.write(buffer)
			f.close()


		print("Released " + str(pressed))
	
	def read(self):
		listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
		listener.start()
		listener.join()


				

	
GPIO = Emulator()


# def check(name):
#   out=0
#   value = open("file.txt", "r").readlines()
#   if (name==17):
#     if (value[0]=="1"):
#       out=1
#     elif(value[0]=="0"):
#       out=0
#   return(out)
	

def get_current_time():
	return math.floor(time.time() * 100)


def sendmessage(text, phone, key, deviceid):

	parameters = {
	    "secret": key,
	    "mode": "devices",
	    "device": deviceid,
	    "sim": 1,
	    "priority": 1,
	    "phone": phone,
	    "message": text
	}


	r = requests.post(url="https://sms.uncgateway.com/api/send/sms", params=parameters)
	result = r.json()

	return(result)


# lcd = Display()		#Defining library object

# lcd.begin(2, 16)	#Setting up LCD
# lcd.home()

apiSecret = "5a4c12017ae850fb916c043f64a07639cfc1698a"
myphonenumber = "+48517726398"
phonenumber = "+48509281008"
id = "00000000-0000-0000-77d9-9a18278af37a"


# lcd.message("Rd: ")

keypin = [17, 0, 22, 27, 4, 16, 24, 23, 25, 1, 18, 12, 20]	# Defining keyboard buttons: 0 GPIO17 AC


# GPIO.setmode(GPIO.BCM)

# print(sendmessage("Hello World!", phonenumber, apiSecret, id))


state = []
count = []
clicktimes = [[]]
delay = []
duration = []
lasttime = get_current_time()

timeclick = []
timeunclick = []

time_at_click = []
time_at_unclick = []



for i in range(0, len(keypin)):
	# GPIO.setup(keypin[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
	state.append(GPIO.HIGH)
	clicktimes.append([get_current_time()])
	delay.append(0)
	duration.append(0)
	count.append(0)
	
	timeclick.append(0)
	timeunclick.append(0)

	time_at_unclick.append(0)
	time_at_click.append(0)


	# print(sendmessage("Dzisiaj jest 24 lutego 2024 roku, godzina 18:03!", phonenumber, apiSecret, id))

	# lcd.message(str(i+1))


class keypad:


	string = ""
	raw = ""


	def listen(self):
		while True:
			for i in range(len(keypin)):
				if (GPIO.input(keypin[i]) == GPIO.LOW) and (state[i] == GPIO.HIGH):	# LOW on pin i (detected circuit close)

					
					state[i] = GPIO.LOW

					time_at_click[i] = get_current_time()

					delay[i] = time_at_click[i] - timeunclick[i]

					print("Delay: ", delay[i])


					print("Only " + str(i) + ": LOW")

				elif (GPIO.input(keypin[i]) == GPIO.HIGH) and (state[i] == GPIO.LOW): # HIGH on pin i (detected circuit open)
					print("Only " + str(i) + ": HIGH")

					time_at_unclick[i] = get_current_time()
					state[i] = GPIO.HIGH

					duration[i] = time_at_unclick[i] - time_at_click[i]

					if(duration[i]>20):
						
						# Handling click without false positive ========================================

						timeunclick[i] = time_at_unclick[i]
						timeclick[i] = time_at_click[i]
						

						count[i]+=1
						print("Click approved: " + str(delay[i]) + ' ' + str(count[i]))


						# Adding data to "string" and "raw" variables so main thread can read string provided by user


						# Raw data

						buffer = []
						stringbuffer = ""

						for element in self.raw:
							buffer+=element

						

						if(i==0):
							buffer+="0"
						elif(i==1):
							buffer+="1"
						elif(i==2):
							buffer+="2"
						elif(i==3):
							buffer+="3"
						elif(i==4):
							buffer+="4"
						elif(i==5):
							buffer+="5"
						elif(i==6):
							buffer+="6"
						elif(i==7):
							buffer+="7"
						elif(i==8):
							buffer+="8"
						elif(i==9):
							buffer+="9"
						elif(i==10):
							buffer+="\n"
						elif(i==11):
							if (len(self.raw)>0):
								buffer.pop()
						elif(i==12):
							buffer=""


						for e in buffer:
							stringbuffer+=e
						

						self.raw = stringbuffer

						print(self.raw)

						# String data

						buffer = []
						stringbuffer = ""

						for element in self.string:
							buffer+=element

						lastchar = ""

						if(len(buffer)>0):
							lastchar = buffer[len(self.string)-1]


						if(i==0):
							if(delay[i]<=100):
								
								if(lastchar=="0"): # nth click (Special click)
									buffer.pop()
									buffer+=" "
								elif(lastchar==" "):
									buffer.pop()
									buffer+="0"
								else:
									buffer+="0" # Normal click
									
							else:	# Normal click
								buffer+="0"
							
						elif(i==1):
							buffer+="1"
						elif(i==2):
							if(delay[i]<=100):
								
								if(lastchar=="2"): # nth click (Special click)
									buffer.pop()
									buffer+="a"
								elif(lastchar=="a"):
									buffer.pop()
									buffer+="b"
								elif(lastchar=="b"):
									buffer.pop()
									buffer+="c"
								elif(lastchar=="c"):
									buffer.pop()
									buffer+="2"
								else:
									buffer+="2" # Normal click
									
							else:	# Normal click
								buffer+="2"
						elif(i==3):
							if(delay[i]<=100):
								
								if(lastchar=="3"): # nth click (Special click)
									buffer.pop()
									buffer+="d"
								elif(lastchar=="d"):
									buffer.pop()
									buffer+="e"
								elif(lastchar=="e"):
									buffer.pop()
									buffer+="f"
								elif(lastchar=="f"):
									buffer.pop()
									buffer+="3"
								else:
									buffer+="3" # Normal click
									
							else:	# Normal click
								buffer+="3"
						elif(i==4):
							if(delay[i]<=100):
								
								if(lastchar=="4"): # nth click (Special click)
									buffer.pop()
									buffer+="g"
								elif(lastchar=="g"):
									buffer.pop()
									buffer+="h"
								elif(lastchar=="h"):
									buffer.pop()
									buffer+="i"
								elif(lastchar=="i"):
									buffer.pop()
									buffer+="4"
								else:
									buffer+="4" # Normal click
									
							else:	# Normal click
								buffer+="4"
						elif(i==5):
							if(delay[i]<=100):
								
								if(lastchar=="5"): # nth click (Special click)
									buffer.pop()
									buffer+="j"
								elif(lastchar=="j"):
									buffer.pop()
									buffer+="k"
								elif(lastchar=="k"):
									buffer.pop()
									buffer+="l"
								elif(lastchar=="l"):
									buffer.pop()
									buffer+="5"
								else:
									buffer+="5" # Normal click
									
							else:	# Normal click
								buffer+="5"
						elif(i==6):
							if(delay[i]<=100):
								
								if(lastchar=="6"): # nth click (Special click)
									buffer.pop()
									buffer+="d"
								elif(lastchar=="d"):
									buffer.pop()
									buffer+="e"
								elif(lastchar=="e"):
									buffer.pop()
									buffer+="f"
								elif(lastchar=="f"):
									buffer.pop()
									buffer+="6"
								else:
									buffer+="6" # Normal click
									
							else:	# Normal click
								buffer+="6"
						elif(i==7):
							if(delay[i]<=100):
								
								if(lastchar=="7"): # nth click (Special click)
									buffer.pop()
									buffer+="p"
								elif(lastchar=="p"):
									buffer.pop()
									buffer+="q"
								elif(lastchar=="q"):
									buffer.pop()
									buffer+="r"
								elif(lastchar=="r"):
									buffer.pop()
									buffer+="s"
								elif(lastchar=="s"):
									buffer.pop()
									buffer+="7"
								else:
									buffer+="7" # Normal click
									
							else:	# Normal click
								buffer+="7"
						elif(i==8):
							if(delay[i]<=100):
								
								if(lastchar=="8"): # nth click (Special click)
									buffer.pop()
									buffer+="t"
								elif(lastchar=="t"):
									buffer.pop()
									buffer+="u"
								elif(lastchar=="u"):
									buffer.pop()
									buffer+="v"
								elif(lastchar=="v"):
									buffer.pop()
									buffer+="8"
								else:
									buffer+="8" # Normal click
									
							else:	# Normal click
								buffer+="8"
						elif(i==9):
							if(delay[i]<=100):
								
								if(lastchar=="9"): # nth click (Special click)
									buffer.pop()
									buffer+="w"
								elif(lastchar=="w"):
									buffer.pop()
									buffer+="x"
								elif(lastchar=="x"):
									buffer.pop()
									buffer+="y"
								elif(lastchar=="y"):
									buffer.pop()
									buffer+="z"
								elif(lastchar=="z"):
									buffer.pop()
									buffer+="9"
								else:
									buffer+="9" # Normal click
									
							else:	# Normal click
								buffer+="9"
						elif(i==10):
							buffer+="\n"
						elif(i==11):
							if (len(self.string)>0):
								buffer.pop()
						elif(i==12):
							buffer=""


						for e in buffer:
							stringbuffer+=e
						

						self.string = stringbuffer

						print(self.string)

						# =======================================

					
					
					print("Delay: " + str(delay[i]))
					print("Duration: " + str(duration))



stupid_T9 = keypad()


get_string = threading.Thread(target=stupid_T9.listen, args=())
get_string.start()



read = threading.Thread(target=GPIO.read, args=())
read.start()


stupid_T9.string = ""	# Clear the string first to prevent weird things from happening

while True:
	if "\n" in stupid_T9.string:
		print("Entered " + stupid_T9.string.removesuffix("\n"))

		# print(sendmessage(stupid_T9.string.removesuffix("\n"), phonenumber, apiSecret, id))

		stupid_T9.string = ""
	time.sleep(0.1)

# GPIO.cleanup()
