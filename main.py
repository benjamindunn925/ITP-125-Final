import funct
import sys
import os

#Interactive pat of program that promps user and takes in user input
def interactive():
    print "Welcome to the Old Spice Voicemail generator"
    gender = funct.getName()
    phone = funct.getPhone()
    reasons = funct.getReasons(gender)
    endings = funct.getEndings(gender)
    jingle = funct.getJingle()
    outputList = funct.stitchMP3(gender, phone, reasons, endings, jingle)

#Handles command line input. If input is invalid, automatically switches to interactive mode
if __name__ == '__main__':
    try:
        name, _g, gender, _p, phone, _r, reasons, _e, endings, _j, jingle, _o, output = sys.argv
        if _g != "-g" or _p != "-p" or _r != "-r" or _e != "-e" or _j != "-j" or _o != "-o":
            print "Wrong output"
            interactive()
    except:
        interactive()
    gender = gender.upper()
    jingle = jingle.upper()
    outputList = funct.stitchMP3(gender, phone, reasons, endings, jingle, fileName = output)
