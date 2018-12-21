
#Importing Dependancies
from pytesseract import *
from PIL import *
from pyautogui import *
from time import *
from os import system
from datetime import *

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
    ##im = Image.open("testImg.jpeg") #unquote for set image testing

    #Find Area
    topLeft = locateOnScreen('messengerIcon.PNG')
    screenCap = screenshot(region = (43, 268, 428, 504))
    print("imported Image")

    
    
    screenCap.save('output.jpeg')

    #Running Tesseract and pulling out the text
    readText = pytesseract.image_to_string(screenCap, lang = 'eng')


    #Outputting the text to the output file
    outLog = open("Output.txt", "a")
    outLog.write("++++++++++++++")
    outLog.write("\n")
    outLog.write(str(datetime.now()))
    outLog.write("\n")
    outLog.write(readText)
    outLog.write("\n")
    outLog.write("\n")
    outLog.close()

shotRead()

print("All Done")
