import pyttsx3

def text_to_speech(text, rate=150, volume=1.0, voice = None):
    #initialize TTS engine
    engine = pyttsx3.init()
    
    #set speech rate
    engine.setProperty('rate',rate)
    
    #set volume level
    engine.setProperty('volume', volume)
    
    #get available voices
    voices = engine.getProperty('voices')
    
    #set voice if specified
    if voice:
        for v in voices:
            if v.name == voice:
                engine.setProperty('voice', v.id)
                break
    
    #convert text speech
    engine.say(text)
    
    #wait for the text to finish
    engine.runAndWait()
    
#example usage
text = input("enter the text:")
text_to_speech(text, rate=200, volume=0.8, voice="english-us" )