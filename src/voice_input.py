import speech_recognition as sr

def listen_for_command():
    """Listens to the microphone and returns the spoken text."""
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("\n[Microphone] Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("[Microphone] Listening! Speak your post content now:")
        
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=15)
            print("[Microphone] Processing speech...")
            
            # Use Google's free speech recognition
            text = recognizer.recognize_google(audio)
            print(f"[Recognized]: {text}")
            return text
            
        except sr.WaitTimeoutError:
            print("[Error] Listening timed out. No speech detected.")
            return None
        except sr.UnknownValueError:
            print("[Error] Could not understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"[Error] Could not request results; {e}")
            return None
