from pynput import keyboard
import time

# string = "0000000000000"

string = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]


def on_press(key):
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
            string[5] = "1"
            passed = True
    else:
        if(pressed==key.insert):    # 0
            string[0] = "1"
            passed = True
        elif(pressed==key.end):    # 1
            string[1] = "1"
            passed = True
        elif(pressed==key.down):    # 2
            string[2] = "1"
            passed = True
        elif(pressed==key.page_down):    # 3
            string[3] = "1"
            passed = True
        elif(pressed==key.left):    # 4
            string[4] = "1"
            passed = True
        
        elif(pressed==key.right):    # 6
            string[6] = "1"
            passed = True
        elif(pressed==key.home):    # 7
            string[7] = "1"
            passed = True
        elif(pressed==key.up):    # 8
            string[8] = "1"
            passed = True
        elif(pressed==key.page_up):    # 9
            string[9] = "1"
            passed = True
        elif(pressed==key.enter):    # ENTER
            string[10] = "1"
            passed = True
        elif(pressed==key.backspace):    # CLEAR
            string[11] = "1"
            passed = True
        elif(pressed==key.delete):    # CLEAR EVERYTHING
            string[12] = "1"
            passed = True


        elif(pressed==key.esc):
            exit()

        

    print("Pressed " + str(pressed))
    if passed:

        buffer = ""

        for e in string:
            buffer+=e

        print(buffer)

        f = open("file.txt", "w")
        f.write(buffer)
        f.close()



def on_release(key):
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
            string[5] = "0"
            passed = True
    else:
        if(pressed==key.insert):    # 0
            string[0] = "0"
            passed = True
        elif(pressed==key.end):    # 1
            string[1] = "0"
            passed = True
        elif(pressed==key.down):    # 2
            string[2] = "0"
            passed = True
        elif(pressed==key.page_down):    # 3
            string[3] = "0"
            passed = True
        elif(pressed==key.left):    # 4
            string[4] = "0"
            passed = True
        
        elif(pressed==key.right):    # 6
            string[6] = "0"
            passed = True
        elif(pressed==key.home):    # 7
            string[7] = "0"
            passed = True
        elif(pressed==key.up):    # 8
            string[8] = "0"
            passed = True
        elif(pressed==key.page_up):    # 9
            string[9] = "0"
            passed = True
        elif(pressed==key.enter):    # ENTER
            string[10] = "0"
            passed = True
        elif(pressed==key.backspace):    # CLEAR
            string[11] = "0"
            passed = True
        elif(pressed==key.delete):    # CLEAR EVERYTHING
            string[12] = "0"
            passed = True


        elif(pressed==key.esc):
            exit()

        

    print("Pressed " + str(pressed))
    if passed:

        buffer = ""

        for e in string:
            buffer+=e

        print(buffer)

        f = open("file.txt", "w")
        f.write(buffer)
        f.close()


    print("Released " + str(pressed))


listener = keyboard.Listener(on_press=on_press, on_release=on_release)

listener.start()
listener.join()

# Programmed penetration test ==================

# f = open("file.txt", "w")   # Simulating a click
# f.write("0")
# f.close()

# time.sleep(5)

# f = open("file.txt", "w")   # Idle after 5 second click
# f.write("1")
# f.close()

# time.sleep(5)

# f = open("file.txt", "w")   # Simulating false positive
# f.write("0")
# f.close()

# time.sleep(1)

# f = open("file.txt", "w")   # Idle after 1 second false positive
# f.write("1")
# f.close()

# time.sleep(5)

# f = open("file.txt", "w")   # Simulating a click after 5 seconds of idle
# f.write("0")
# f.close()

# time.sleep(5)

# f = open("file.txt", "w")   # Idle after 5 second click
# f.write("1")
# f.close()

# End of test =======================
