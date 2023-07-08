# SPEECH RECOGNITION FROM AUDIO:-


#python program to recognise the speech from an audio

#imporot a package known as speecch recognition and name it (shortcut) as sr
 

import speech_recognition as sr 

r = sr.Recognizer() 
with sr.Microphone() as source: 

    #take microphone as the source
    print("Speak anything: ")
    audio = r.listen(source)

    #try and except resembles the if-else statement 
    try:
        text = r.recognize_google(audio)
        print('You said : {}' . format(text))
    except:
        print('Sorry could not recognize your voice')


