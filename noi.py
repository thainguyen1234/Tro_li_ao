import pyttsx3

engine = pyttsx3.init()

print("Hey Duc, Welcome to Virtual Assistant")
engine.say("Hey Duc, Welcome to Virtual Assistant")
engine.runAndWait()

isRunning = True

while isRunning:
    brain = input("Enter the sentences you want to say: ")
    
    if brain == "stop":
        isRunning = False
        brain = ""
    engine.say(brain)
    engine.runAndWait()
