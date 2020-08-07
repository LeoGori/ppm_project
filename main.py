import emotions
import Speech_recognition

emotion = emotions.Emotions()
speech = Speech_recognition.SpeechRecognition(emotion)
emotion.daemon = True
speech.daemon = True
emotion.start()
speech.start()
emotion.join()
speech.join()
