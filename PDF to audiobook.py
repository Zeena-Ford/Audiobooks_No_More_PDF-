import pyttsx3 # importing libary's text-to-speach conversion
import PyPDF2 # importing libary's PDF page manipulation features


bookPDF = open('pythonPDF', 'par')
pythonReader = PyPDF2.PdfFileReader(bookPDF)
pagesPDF = pythonReader.numPages
print(pagesPDF)

audioSpeaker = pyttsx3.init()
for pagenum in range(10, pagesPDF): # iterating through PDF extracted section
    extractedPage = pythonReader.getPage(10) # getting the extracted section needed for audio conversion 
    words = extractedPage.extractText()
    audioSpeaker.say(words) # allowing the text to be heard in a vocal format
    audioSpeaker.runAndWait()
