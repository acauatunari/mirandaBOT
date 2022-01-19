import os 
import pyttsx3
import speech_recognition as sr

#engine = pyttsx3.init()

#engine.setProperty("voice", "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0")
#engine.setProperty("rate", 120)
#engine.setProperty("volume", 1)
#engine.runAndWait()

def WriteFile(msg):
	try:
		with open("audio_transcript.txt", "a") as file:
			file.write(str(msg) + "\n")
			file.close()

	except:
		print("MENSAGE WRITE ERROR > " + msg)


def ListenAndReponse():
	msg = ""
	while(msg != "bye-bye"):

		with sr.Microphone() as source:
			sr.Recognizer().adjust_for_ambient_noise(source)
			print("Say anything")
			audio = sr.Recognizer().listen(source)
			print("processing...\n")

		try:
			msg = sr.Recognizer().recognize_google(audio, language='en-US')
			print("you say: " + msg, "\n")
		except sr.UnknownValueError:
			print("Google Speech Recognition didn't understand what you said! \n")
		except sr.RequestError as e:
			print("No results were obtained from the Google Speech Recognition service; {0}".format(e), "\n")
  
		WriteFile(msg)

		if msg == "action":
			while (msg != "exit"):
				print("### START COMMAND MODE ###")

				with sr.Microphone() as source:
					sr.Recognizer().adjust_for_ambient_noise(source)
					print("What I can do for you?")
					audio = sr.Recognizer().listen(source)
					print("processing...\n")

				try:
					msg = sr.Recognizer().recognize_google(audio, language='en-US')
					os.system(msg)
					print("doing: " + msg)
				except sr.UnknownValueError:
					print("Google Speech Recognition didn't understand what you said! \n")
				except sr.RequestError as e:
					print("No results were obtained from the Google Speech Recognition service; {0}".format(e), "\n")

ListenAndReponse() 
 	


