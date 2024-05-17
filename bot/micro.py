import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Di algo:")
    audio_data = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio_data, language='es-ES')
        print("Texto reconocido:", text)
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
    except sr.RequestError:
        print("Error al conectarse al servicio de reconocimiento de voz")