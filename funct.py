import urllib
import sys
import os
import shutil
import main

confirm = True
baseURL = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/"

#Lists with the greetings and endings for each gender
maleGreetings = [
    '1: Building an orphanage for children with their bare hands while playing a sweet, sweet lullaby for those children with two mallets against their abs xylophone.',
    '2: Cracking walnuts with their man mind.',
    '3: Polishing their monocle smile.',
    '4: Ripping out mass loads of weights.'
    ]
femaleGreetings = [
    '1: Ingesting my delicious Old Spice man smell.',
    '2: Listening to me read romantic poetry while I make a bouquet of paper flowers from each read page.',
    '3: Enjoying a lobster dinner I prepared just for her while carrying her on my back safely through piranha infested aters.',
    '4: Being serenaded on the moon with the view of the earth while surviving off the oxygen in my lungs via a passionate kiss.',
    '5: Riding a horse backwards with me.'
    ]
maleEndings = [
    '1: I\'m on a horse.',
    '2: I\'m on a phone.',
    '3: SWAN DIVE.',
    '4: This voicemail is now diamonds.'
    ]
femaleEndings= [
    '1: But she\'ll get back to you as soon as she can.',
    '2: Thanks for calling.'
    ]
gender = ""


#Prompts user for gender and checks for proper input. Returns gender as a string
def getName():
    while True:
        gender = str(raw_input("Would you like a Male(M) or Female(F) greeting? ")).upper()
        if gender == "M":
            gender = "M"
            return gender
        elif gender == "F":
            gender = "F"
            return gender
        else:
            print "Invalid input"
            continue
#Prompts user for phone number and checks for proper input. Returns phone number as a string
def getPhone():
    realphone = ""
    while True:
        phonenumber = str(raw_input("Please type in your 10 digit phone number: "))
        for number in phonenumber:
            if number.isdigit():
                realphone += number
        if len(realphone) == 10:
            return realphone
        else:
            print "Invalid input!"
            continue
#Displays list of reasons to use based off of the gender. Prompts user to choose inputs. Checks for proper input, appends input to an array and returns an array of reasons
def getReasons(gender):
    reason = ""
    validInput = True
    print "Please choose a single reason for your message (1, 2, 3)"
    if gender == 'M':
        #Will re-reun if user uses an invalid input
        while True:
            for greetings in maleGreetings:
                print greetings
            greetingChoice = str(raw_input("Choice: "))
            if len(greetingChoice) > 1:
                print "Too many choices"
                continue
            elif greetingChoice.isdigit() and int(greetingChoice) > 0 and int(greetingChoice) <= 4:
                reason = greetingChoice
                validInput = True
            else:
                print "Error, invalid input"
                validInput = False
                continue
            if len(reason) == 1 and validInput == True:
                return reason
            else:
                continue
            break

#Runs if user chooses female gender
    if gender == 'F':
        while True:
            for greetings in femaleGreetings:
                print greetings

            greetingChoice = str(raw_input("Choice: "))
            if len(greetingChoices) > 1:
                print "Too many choices"
                continue
            elif greetingChoice.isdigit() and int(greetingChoice) >0 and int(greetingChoice) <= 5 :
                reason = greetingChoice
                validInput = True
            else:
                print "Error, invalid input"
                validInput = False
                continue
            if len(reason) == 1 and validInput == True:
                return reason
            else:
                continue
            break

#Prints list of endings based off of gender. Prompts user to choose inputs. Checks for proper input, appends input to an array and returns an array of reasons
def getEndings(gender):
    print "Please choose a single ending for your message (1, 2, 3)"
    ending = ""
    validInput = True
    if gender == 'M':
        while True:
            for endings in maleEndings:
                print endings
            endingChoice = str(raw_input("Choice: "))
            if len(endingChoice) > 1:
                print "Too many choices"
                continue
            elif endingChoice.isdigit() and int(endingChoice) > 0 and int(endingChoice) <= 4:
                ending = endingChoice
                validInput = True
            else:
                print "Error, invalid input"
                validInput = False
                continue
            if len(ending) == 1 and validInput == True:
                return ending
            else:
                continue
            break

#Runs if gender is female
    if gender == 'F':
        while True:
            for endings in femaleEndings:
                print endings
            endingChoice = str(raw_input("Choice: "))
            if len(endingChoice) > 1:
                print "Too many choices"
                continue

            elif endingChoice.isdigits() and int(endingChoice) > 0 and int(endingChoice) <= 2:
                ending = endingChoice
                validInput = True
            else:
                print "Error, invalid input"
                validInput = False
                continue
            if len(ending) == 1 and validInput == True:
                return ending
            else:
                continue
            break

#Prompts user if they want a jingle or not. Checks for proper input and returns a string of their response
def getJingle():
    while True:
        jingle = str(raw_input("Would you like to add a jingle at the end (Y/N)?")).upper()
        if jingle == "Y":
            jingle = "Y"
            return jingle
        elif jingle == "N":
            jingle = "N"
            return jingle
        else:
            print "Invalid input!"
        continue

#Takes in the user's gender, phone, reasons array, endings array and jingle. Cycles through all the stored inputs from the user and creates an array of MP3 files to download and stich. fileName = none is used if the interactive mode is chosen. Returns an array of MP3 files to stich
def stitchMP3(gender, phone, reason, ending, jingle, fileName=None):
    outputList = []
    printOut =""

    if gender == "M":
        outputList.append("m-b1-hello.mp3 ")
        outputList.append("m-b2-have_dialed.mp3")
        printOut += "Hello, you have dialed "

    else:
        outputList.append("f-b1-hello_caller.mp3")
        outputList.append("f-b2-lady_at.mp3")
        printOut += "Hello callers, the lovely/talented/intelligent and beautiful/sophisticated lady at "

    for numbers in phone:
        outputList.append(numbers + ".mp3")
        printOut += numbers

    if gender == "M":
        outputList.append("m-r0-cannot_come_to_phone.mp3")
        printOut += ". The tall, accomplished man you're calling can't come to the phone right now because they're "

        if reason == "1":
            outputList.append("m-r1-building.mp3")
            printOut += "Building an orphanage for children with their barehands while playing a sweet, sweet lullaby for those children with two mallets against their ab xylophone. "
        elif reason == "2":
            outputList.append("m-r2-cracking_walnuts.mp3")
            printOut += "Cracking walnuts with their man mind. "
        elif reason == "3":
            outputList.append("m-r3-polishing_monocole.mp3")
            printOut += "Polishing their monocle smile. "
        elif reason == "4":
            outputList.append("m-r4-ripping_weights.mp3")
            printout += "Ripping out mass loads of weights. "

        outputList.append("m-leave_a_message.mp3")
        printOut += "But leave a message and they'll return your call as soon as possible. "

        if ending == "1":
            outputList.append("m-e1-horse.mp3")
            printOut += "I'm on a horse. "
        elif ending == "2":
            outputList.append("m-e3-on_phone.mp3")
            printOut += "I'm on a phone. "
        elif ending == "3":
            outputList.append("m-e4-swan_dive.mp3")
            printOut += "Swan dive. "
        elif ending == "4":
            outputList.append("m-e5-voicemail.mp3 ")
            printOut += "This voicemail is now diamonds. "

    else:
        outputList.append("f-r0.1-unable_to_take_call.mp3")
        outputList.append("f-r0.2-she_is_busy.mp3")
        printOut += " Is unable to take your call. She's busy "

        if reason == "1":
            outputList.append("f-r1-ingesting_old_spice.mp3")
            printOut += "Ingesting my delicious Old Spice man smell. "
        elif reason == "2":
            outputList.append("f-r2-listening_to_reading.mp3")
            printOut += "Listening to me read romantic poetry while I make a bouquet of paper flowers from each read page. "
        elif reason == "3":
            outputList.append("f-r3-lobster_dinner.mp3")
            printOut += "Enjoying a lobster dinner I prepared just for her while carrying her on my back safely through piranha infested waters. "
        elif reason == "4":
            outputList.append("f-r4-moon_kiss.mp3")
            printOut += "Being serenaded on the Moon with the view of the Earth while surviving off the oxygen of lungs via a passionate kiss. "
        elif reason == "5":
            outputList.append("f-r5-riding_a_horse.mp3")
            printOut += "Riding a horse backwards with me. "

        if ending == "1":
            outputList.append("f-e1-she_will_get_back_to_you.mp3")
            printOut += "But she'll get back to you as soon as she can. "
        elif ending == "2":
            outputList.append("f-e2-thanks_for_calling.mp3")
            printOut += "Thanks for calling. "

    if jingle == "Y":
        outputList.append("m-e2-jingle.mp3")
        printOut += "Do do do doot doo do do dooot. "

    print "Your voice mail will be as follows: "
    print printOut

    while True:
        confirm = str(raw_input("Is this correct(Y/N)? ")).upper()
        if confirm == "Y":
            if fileName == None:
                fileName = str(raw_input("Please enter a filename to save the ringtone to (myFileName): "))
            createMp3(outputList, fileName)
        elif confirm == "N":
            print "Starting over"
            main.interactive()
        else:
            print "Invalid input"
            continue

#Downloads files to download into an array of MP3 files. Stiches MP3 files based off of array of MP3 files. Saves to the filename that the user inputted. Deletes downloaded MP3s and exits prpogram
def createMp3(outputList, fileName):

    for files in outputList:
        mp3 = urllib.urlretrieve(baseURL + files, files )

    mp3Destination = open(fileName + ".mp3", 'w')
    textDestination = open(fileName + ".txt", "w")

    for files in outputList:
        shutil.copyfileobj(open(files, 'r'), mp3Destination)
        textDestination.write(files + "\n")
    mp3Destination.close
    textDestination.close

    for files in set(outputList):
        os.remove(files)
    sys.exit()
