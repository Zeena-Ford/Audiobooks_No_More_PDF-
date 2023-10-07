import pyttsx3
import PyPDF2


bookPDF = open('pythonPDF', 'par')
pythonReader = PyPDF2.PdfFileReader(bookPDF)
pagesPDF = pythonReader.numPages
print(pagesPDF)

audioSpeaker = pyttsx3.init()
for pagenum in range(10, pagesPDF):
    extractedPage = pythonReader.getPage(10)
    words = extractedPage.extractText()
    audioSpeaker.say(words)
    audioSpeaker.runAndWait()