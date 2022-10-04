#!/usr/bin/python3
import platform
import argparse 
import sys 

sistema = format(platform.system())

if (sistema == "Linux"):
	# Text colors
	normal_color = "\33[00m"
	info_color = "\033[1;33m"
	red_color = "\033[1;31m"
	green_color = "\033[1;32m"
	whiteB_color = "\033[1;37m"
	detect_color = "\033[1;34m"
	banner_color="\033[1;33;40m"
	end_banner_color="\33[00m"
elif (sistema == "Windows"):
	banner_color=""
	end_banner_color=""


def banner():
    print (banner_color + " __  __             _        ____            _   _   _     _     " + end_banner_color)
    print (banner_color + "|  \/  | __ _  __ _(_) ___  | __ )  __ _  __| | | | | |___| |__  " + end_banner_color)
    print (banner_color + "| |\/| |/ _` |/ _` | |/ __| |  _ \ / _` |/ _` | | | | / __| '_ \ " + end_banner_color)
    print (banner_color + "| |  | | (_| | (_| | | (__  | |_) | (_| | (_| | | |_| \__ \ |_) |" + end_banner_color)
    print (banner_color + "|_|  |_|\__,_|\__, |_|\___| |____/ \__,_|\__,_|  \___/|___/_.__/ " + end_banner_color)
    print (banner_color + "              |___/                                              " + end_banner_color)

def checkArgs():
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description=red_color + 'Magic Bad Usb 1.0\n' + info_color)
    parser.add_argument('-c', "--command", action="store",dest='command',help="Command to store in badusb")
    parser.add_argument('-s', "--save", action="store",dest='save',help="Save into a file")
    parser.add_argument('-m', "--mode", action="store",dest='mode',help="Available modes: badusb (by default), flipperzero")

    args = parser.parse_args()
    if (len(sys.argv)==1) or args.command==False:
        parser.print_help(sys.stderr)
        sys.exit(1)

    return args


def converttochar(cadena):
    chars = " "

    for i in cadena:
        chars = chars + str(ord(i))
        chars = chars + " "

    chars = chars[0:len(chars)-1]
    return chars 

def keyboardsetup():
	if (args.save):
		file.write('#include "Keyboard.h"\n')
		file.write("#define KP_1          0xE1\n")
		file.write("#define KP_2          0xE2\n")
		file.write("#define KP_3          0xE3\n")
		file.write("#define KP_4          0xE4\n")
		file.write("#define KP_5          0xE5\n")
		file.write("#define KP_6          0xE6\n")
		file.write("#define KP_7          0xE7\n")
		file.write("#define KP_8          0xE8\n")
		file.write("#define KP_9          0xE9\n")
		file.write("#define KP_0          0xEA\n")
	else:
		print('#include "Keyboard.h"')
		print("#define KP_1          0xE1")
		print("#define KP_2          0xE2")
		print("#define KP_3          0xE3")
		print("#define KP_4          0xE4")
		print("#define KP_5          0xE5")
		print("#define KP_6          0xE6")
		print("#define KP_7          0xE7")
		print("#define KP_8          0xE8")
		print("#define KP_9          0xE9")
		print("#define KP_0          0xEA")

def executewindow():
	if (args.save):
		file.write("/* Init function */\n")
		file.write("void setup()\n")
		file.write("{\n")
		file.write("  // Begining the Keyboard stream\n")
		file.write("  Keyboard.begin();\n")

		file.write("  // Wait 500ms\n")
		file.write("  delay(500);\n")

		file.write("  Keyboard.press(KEY_LEFT_GUI);\n")
		file.write("  Keyboard.press('r');\n")
		file.write("  Keyboard.releaseAll();\n")

		file.write("  delay(300);\n")
	else:
		print("/* Init function */")
		print("void setup()")
		print("{")
		print("  // Begining the Keyboard stream")
		print("  Keyboard.begin();")

		print("  // Wait 500ms")
		print("  delay(500);")

		print("  Keyboard.press(KEY_LEFT_GUI);")
		print("  Keyboard.press('r');")
		print("  Keyboard.releaseAll();")

		print("  delay(300);")

def generatecommand(chars):
	for i in chars:
		if (i != " "):
			if (i == "1"):
				if (args.save):
					file.write("Keyboard.press(KP_1);\n")
					file.write("Keyboard.release(KP_1);\n")
				else:
					print ("Keyboard.press(KP_1);")
					print ("Keyboard.release(KP_1);")
			elif (i == "2"):
				if (args.save):
					file.write("Keyboard.press(KP_2);\n")
					file.write("Keyboard.release(KP_2);\n")
				else:
					print ("Keyboard.press(KP_2);")
					print ("Keyboard.release(KP_2);")
			elif (i == "3"):
				if (args.save):
					file.write("Keyboard.press(KP_3);\n")
					file.write("Keyboard.release(KP_3);\n")
				else:
					print ("Keyboard.press(KP_3);")
					print ("Keyboard.release(KP_3);")
			elif (i == "4"):
				if (args.save):
					file.write("Keyboard.press(KP_4);\n")
					file.write("Keyboard.release(KP_4);\n")
				else:
					print ("Keyboard.press(KP_4);")
					print ("Keyboard.release(KP_4);")
			elif (i == "5"):
				if (args.save):
					file.write("Keyboard.press(KP_5);\n")
					file.write("Keyboard.release(KP_5);\n")
				else:
					print ("Keyboard.press(KP_5);")
					print ("Keyboard.release(KP_5);")
			elif (i == "6"):
				if (args.save):
					file.write("Keyboard.press(KP_6);\n")
					file.write("Keyboard.release(KP_6);\n")
				else:
					print ("Keyboard.press(KP_6);")
					print ("Keyboard.release(KP_6);")
			elif (i == "7"):
				if (args.save):
					file.write("Keyboard.press(KP_7);\n")
					file.write("Keyboard.release(KP_7);\n")
				else:
					print ("Keyboard.press(KP_7);")
					print ("Keyboard.release(KP_7);")
			elif (i == "8"):
				if (args.save):
					file.write("Keyboard.press(KP_8);\n")
					file.write("Keyboard.release(KP_8);\n")
				else:
					print ("Keyboard.press(KP_8);")
					print ("Keyboard.release(KP_8);")
			elif (i == "9"):
				if (args.save):
					file.write("Keyboard.press(KP_9);\n")
					file.write("Keyboard.release(KP_9);\n")
				else:
					print ("Keyboard.press(KP_9);")
					print ("Keyboard.release(KP_9);")
			elif (i == "0"):
				if (args.save):
					file.write("Keyboard.press(KP_0);\n")
					file.write("Keyboard.release(KP_0);\n")
				else:
					print ("Keyboard.press(KP_0);")
					print ("Keyboard.release(KP_0);")
			if (args.save):
				file.write("delay(1);\n")
			else:          
				print ("delay(1);")
		else:
			if (args.save):
				file.write("Keyboard.releaseAll();\n")
				file.write("Keyboard.press(KEY_LEFT_ALT);\n")
			else:
				print ("Keyboard.releaseAll();")
				print ("Keyboard.press(KEY_LEFT_ALT);")
	if (args.save):
		file.write("Keyboard.releaseAll();\n")
	else:
		print ("Keyboard.releaseAll();")

def pressenterfunct():
	if (args.save):
		file.write("void typeKey(uint8_t key)\n")
		file.write("{\n")
		file.write("  Keyboard.press(key);\n")
		file.write("  delay(50);\n")
		file.write("  Keyboard.release(key);\n")
		file.write("}\n")
	else:
		print("void typeKey(uint8_t key)")
		print("{")
		print("  Keyboard.press(key);")
		print("  delay(50);")
		print("  Keyboard.release(key);")
		print("}")

def returnandend():
	if (args.save):
		file.write("  typeKey(KEY_RETURN);\n")

		file.write("  delay(3000);\n")
		file.write('//Keyboard.print(F("f"));\n')

		file.write("// Ending stream\n")
		file.write("  Keyboard.end();\n")
		file.write("}\n")

		file.write("/* Unused endless loop */\n")
		file.write("void loop() {}\n")
		file.close()
		print (" ")
		print (whiteB_color + "[" + green_color + "+" + whiteB_color + "]  File saved successfull with name " + info_color + args.save)

	else:
		print("  typeKey(KEY_RETURN);")

		print("  delay(3000);")
		print('//Keyboard.print(F("f"));')

		print("// Ending stream")
		print("  Keyboard.end();")
		print("}")

		print("/* Unused endless loop */")
		print("void loop() {}")


def generatecommandflipper(cadena):
	cadena = cadena + " "
	if (args.save):
		file.write("DELAY 100\n")
		file.write("GUI m\n")
		file.write("DELAY 100\n")
		file.write("GUI r\n")
	else:
		print ("DELAY 100")
		print ("GUI m")
		print ("DELAY 100")
		print ("GUI r")

	inicio = 0
	while (inicio != -1):
		fin = cadena.find(" ", inicio+1)
		if (fin != -1):
			char = cadena[inicio:fin]
			char = char.strip()
			comando = "ALTCHAR " + str(char)
			if (args.save):
				file.write(comando+"\n")
				file.write("DELAY 10\n")
			else:
				print(comando)
				print ("DELAY 10")
		inicio = cadena.find(" ", inicio+1)
		
	if (args.save):
		file.write("DELETE\n")
		file.write("ENTER\n")
		print (whiteB_color + "[" + green_color + "+" + whiteB_color + "]  File saved successfull with name " + info_color + args.save)
	else:
		print ("DELETE\n")
		print ("ENTER")
			



########## Main function #################3
if __name__ == "__main__":
	banner()
	args = checkArgs()
	if (args.command):
		if (args.save):
			filename = args.save
			file = open(filename, "w")
	
	cadena = args.command
			
	if (args.mode == "flipperzero"):
		chars = converttochar(cadena)
		chars = chars.strip()
		generatecommandflipper(chars)
		
	else:
		#Generate Arduino Script
		keyboardsetup()
		pressenterfunct()
		executewindow()

		#Convert command to ALTCODE
		chars = converttochar(cadena)
		generatecommand(chars)

		#Finish 
		returnandend()
	

