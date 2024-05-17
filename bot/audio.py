import speech_recognition as sr

# Crear un objeto Recognizer
recognizer = sr.Recognizer()

# Cargar el archivo de audio
audio_file = sr.AudioFile('./nota.wav')

with audio_file as source:
    audio_data = recognizer.record(source)

# Usar el reconocedor para convertir audio a texto
try:
    text = recognizer.recognize_google(audio_data, language='es-ES')
    print("Texto reconocido:", text)
except sr.UnknownValueError:
    print("No se pudo entender el audio")
except sr.RequestError:
    print("Error al conectarse al servicio de reconocimiento de voz")