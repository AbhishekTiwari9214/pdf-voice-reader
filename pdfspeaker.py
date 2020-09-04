import pyttsx3
import PyPDF2
book = open('example.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
rate = speaker.getProperty('rate')
speaker.setProperty('rate', rate-50)


page = pdfReader.getPage(16)
text = page.extractText()

print(text)
pyttsx3.speak(text)

speaker.runAndWait()
