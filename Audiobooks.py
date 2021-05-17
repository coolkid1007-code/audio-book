import pyttsx3
import PyPDF2 #for reading and manipulating pdf files
my_book = open('The-Time-Machine.pdf','rb')   #you can give your own pdf file
#optional
pdf = PyPDF2.PdfFileReader(my_book)
number_of_pages = pdf.numPages
print(number_of_pages)
#optional
speaker = pyttsx3.init()
page = pdf.getPage(5) #get the starting point where you want the audio to start
text = page.extractText()

speaker.say(text)
speaker.runAndWait()


