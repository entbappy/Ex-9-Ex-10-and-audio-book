import pyttsx3
import PyPDF2

book = open("Bappy's CV.pdf","rb")
pdf = PyPDF2.PdfFileReader(book)
page = pdf.numPages
print(page)

talk = pyttsx3.init()
for i in range(0,page):
    final = pdf.getPage(i)
    now = final.extractText()
    talk.say(now)
    talk.runAndWait()



