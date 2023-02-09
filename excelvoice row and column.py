import speech_recognition as sr
import openpyxl

# Initialize the recognizer class
r = sr.Recognizer()

# Load the workbook and select the active sheet
workbook = openpyxl.load_workbook("data.xlsx")
sheet = workbook.active

# Get the audio from the microphone and recognize the speech
with sr.Microphone() as source:
    print("Speak the row and column: ")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("You said: {}".format(text))
except sr.UnknownValueError:
    print("Sorry, I didn't catch that.")

# Split the recognized text into row and column
text = text.split()
row = int(text[0])
col = int(text[1])

# Get the data from the microphone
with sr.Microphone() as source:
    print("Speak the data: ")
    audio = r.listen(source)

# Convert the audio to text
try:
    data = r.recognize_google(audio)
    print("You said: {}".format(data))
except sr.UnknownValueError:
    print("Sorry, I didn't catch that.")

# Write the data to the specified cell
sheet.cell(row=row, column=col).value = data

# Save the changes to the workbook
workbook.save("data.xlsx")
