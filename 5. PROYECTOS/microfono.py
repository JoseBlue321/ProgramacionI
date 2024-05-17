#pip install SpeechRecognition
import tkinter
import speech_recognition as sr

class App:
    def __init__(self):
        self.ventana = tkinter.Tk()
        self.ventana.title("PROYECTO TRADUCTOR DE AUDIO A TEXTO")
        self.ventana.geometry('500x300')

        self.boton1 = tkinter.Button( self.ventana, text="traducir", command=self.traducir )
        self.boton1.grid( column=0, row=0 )

        self.label1 = tkinter.Label( self.ventana, text="" )
        self.label1.grid( column=0,row=1 )

        self.ventana.mainloop()
    
    def traducir(self):
        self.recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.label1.config(text="Di algo...")
            self.audio_data = self.recognizer.listen(source)

        try:
            self.text = self.recognizer.recognize_google(self.audio_data, language='es-ES')
            self.label1.config(text=self.text)
        except sr.UnknownValueError:
            self.label1.config(text="No se pudo conectar el audio...")
        except sr.RequestError:
            self.label1.config(text="Error al conectarse con el servicio de reconocimiento de voz")

#**********************
app = App()