from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from .models import Table

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views import generic
from django.shortcuts import render
from .models import Table
import base64
import io
from .forms import TextForm
from django.views.generic.edit import FormView


def search(request):
    qur = request.GET.get("text_field")
    qur2 = request.GET.get("date_field")
    tables = Table.objects.all()
    if qur != "" and qur is not None:
        tables = tables.filter(speech_text__contains=qur)
    if qur2 != "" and qur2 is not None:
        tables = tables.filter(date=qur2)
    return render(request, 'polls/search.html', {'tables': tables})


class TableView(generic.ListView):
    template_name = 'polls/table.html'
    context_object_name = 'speech_text_list'
    model = Table


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'speech_text_list'
    model = Table


class EmotionsView(generic.ListView):
    template_name = 'polls/emotions.html'
    context_object_name = 'emotion_list'
    model = Table

    def get_queryset(self):
        """Return the last five published questions."""
        return Table.objects.all()


class AngerView(generic.ListView):
    template_name = 'polls/anger.html'
    context_object_name = 'anger_emotion_list'
    model = Table

    def get_queryset(self):
        """Return the last five published questions."""
        return Table.objects.filter(emotion="Arrabbiato")


class DisgustView(generic.ListView):
    template_name = 'polls/disgust.html'
    context_object_name = 'disgust_emotion_list'
    model = Table

    def get_queryset(self):
        return Table.objects.filter(emotion="Disgustato")


class FearView(generic.ListView):
    template_name = 'polls/fear.html'
    context_object_name = 'fear_emotion_list'
    model = Table

    def get_queryset(self):
        return Table.objects.filter(emotion="Impaurito")


class HappinessView(generic.ListView):
    template_name = 'polls/happiness.html'
    context_object_name = 'happiness_emotion_list'
    model = Table

    def get_queryset(self):
        """Return the last five published questions."""
        return Table.objects.filter(emotion="Felice")


class SadnessView(generic.ListView):
    template_name = 'polls/sadness.html'
    context_object_name = 'sadness_emotion_list'
    model = Table

    def get_queryset(self):
        """Return the last five published questions."""
        return Table.objects.filter(emotion="Triste")


class SurpriseView(generic.ListView):
    template_name = 'polls/surprise.html'
    context_object_name = 'surprise_emotion_list'
    model = Table

    def get_queryset(self):
        return Table.objects.filter(emotion="Sorpreso")

# class IndexView(generic.ListView):
#     template_name = 'polls/index.html'
#     context_object_name = 'latest_question_list'
#
#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.all()
#
#
# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'polls/detail.html'
#
#
# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'
#
#
# def vote(request, question_id):
#     # return HttpResponse("You're voting on question %s." % question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
