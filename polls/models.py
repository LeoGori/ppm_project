from django.db import models


# Create your models here.

class Table(models.Model):
    speech_text = models.CharField(max_length=200)
    emotion = models.CharField(max_length=20)
    image = models.TextField()

    def processImage(self):
        print('ciao')

    def __str__(self):
        return self.speech_text

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#     def __str__(self):
#         return self.question_text
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.choice_text

