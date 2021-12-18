import speech_recognition as sr
import pyttsx3 as px3
import pywhatkit as pk
import wikipedia as wiki
import datetime

talker = px3.init()
voice = talker.getProperty('voices')
talker.setProperty('voice',voice[1].id)

def talk(text):
	talker.say(text)
	talker.runAndWait()

talk("hello i am your personal assistant")
talk("what can i do for you")

def get_command():
	listening = sr.Recognizer()
	with sr.Microphone() as mic:
		command_unif = listening.listen(mic)
		command = listening.recognize_google(command_unif)
		print(command)
		if 'assistant' in command.lower():
			command = command.replace('assistant','')
			print(command)
			return command
		else:
			pass
	command = 'nothing'
	return command

def run():
	while True:
		command = get_command()
		if 'break' in command:
			exit()
		elif 'time' in command:
			time = datetime.datetime.now().strftime('%I %M %p')
			talk("currently it is" + time)
			talk("anything else?")
			pass
		elif 'date' in command:
			date = datetime.datetime.now().strftime("%d %m %Y")
			talk("it is" + date + "today")
			talk("anything else?")
			pass
		elif 'about' in command:
			talk('here is what i found')
			data = wiki.summary(command[command.index('about')+6:], 1)
			talk(data)
			talk("anything else?")
			pass
		elif 'play' in command:
			command = command.replace("play", '')
			pk.playonyt(command)
			pass
		elif 'search' in command:
			command = command.replace('search', '')
			pk.search(command)
			pass
		elif 'nothing' in command:
			talk("please try and say assistant in what you say!!")
			pass
		else:
			talk("sorry did not get what you said")
			talk("anything else?")
			pass



run()
