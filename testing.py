
#Importing Dependancies
import pytesseract
import PIL
import pyautogui
import time
import os
import datetime


##Variables##
#imageFile =
num_seconds = 5

#debug that it initiated
print("Initiating...")

#clickLocation = locateAllOnScreen('findIcon.PNG')
#print("Location", str(clickLocation))
#click()

def shotRead():
    #Opening image and assigning to variable
    im = PIL.Image.open("testImg.PNG") #unquote for set image testing

    #Find Area
    #topLeft = locateOnScreen('messengerIcon.PNG')
    #im = pyautogui.screenshot(region = (0, 0, 200, 150)) #Use for screen capture rather than pre set imageFile
    print("imported Image")



    #screenCap.save('output.jpeg')

    #Running Tesseract and pulling out the text
    readText = pytesseract.image_to_string(im, lang = 'eng')


    #Outputting the text to the output file
    outLog = open("Output.txt", "a")
    outLog.write("++++++++++++++")
    outLog.write("\n")
    #outLog.write(str(date.datetime()))
    outLog.write("\n")
    outLog.write(readText)
    outLog.write("\n")
    outLog.write("\n")
    outLog.close()

shotRead()

print("All Done")
