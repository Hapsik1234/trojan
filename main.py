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

					duration = time_at_unclick[i] - time_at_click[i]

					if(duration>20):
						
						# Handling click without false positive ========================================

						timeunclick[i] = time_at_unclick[i]
						timeclick[i] = time_at_click[i]
						

						count[i]+=1
						print("Click approved: " + str(delay[i]) + ' ' + str(count[i]))


						# Adding data to string and raw variables

						


						# =======================================

					
					
					print("Delay: " + str(delay[i]))
					print("Duration: " + str(duration))


def main_f():
	while True:
		if not (stupid_T9.string.find('\n')==-1):
			print(stupid_T9.string)
			stupid_T9.string = ""



print("gfousy9sou")

stupid_T9 = keypad()


# main = threading.Thread(target=main_f, args=())
# main.start()


get_string = threading.Thread(target=stupid_T9.listen, args=())
get_string.start()




read = threading.Thread(target=GPIO.read, args=())
read.start()





# finally:
# 	GPIO.cleanup()
