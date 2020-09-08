import speech_recognition as sr
from threading import Thread
import django
from django.conf import settings
import ppm_project.settings as app_settings
from PIL import Image
import base64

settings.configure(INSTALLED_APPS=app_settings.INSTALLED_APPS, DATABASES=app_settings.DATABASES)

django.setup()

from polls.models import Table


class SpeechRecognition(Thread):
    def __init__(self, emotion):
        super().__init__()
        self.emotion = emotion

    def run(self):
        # obtain audio from the microphone

        while True:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Say something!")
                self.emotion.setReady()
                audio = r.listen(source)

            try:
                # for testing purposes, we're just using the default API key
                # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                # instead of `r.recognize_google(audio)`
                text = r.recognize_google(audio, language="it-IT")
                IMIR = self.emotion.getCropeImage().reshape(48, 48)
                img = Image.fromarray(IMIR)
                img.save('prova.png')
                with open("prova.png", "rb") as file:
                    img = base64.b64encode(file.read())
                # img = Image.open(io.BytesIO(base64.b64decode(img)))
                print("Google Speech Recognition thinks you said: " + text
                      + " while your mood was " + self.emotion.getEmotion())
                str_img = str(img)
                str_img = str_img[2:len(str_img) - 1]
                print(str_img)
                t = Table(speech_text=text, emotion=self.emotion.getEmotion(), image=str_img)
                print(str_img)
                t.save()

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
