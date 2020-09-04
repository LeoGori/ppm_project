from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.TableView.as_view(), name='tables'),
    path('anger', views.AngerView.as_view(), name='angers'),
    path('disgust', views.DisgustView.as_view(), name='disgusts'),
    path('fear', views.FearView.as_view(), name='fears'),
    path('happiness', views.HappinessView.as_view(), name='happinesses'),
    path('sadness', views.SadnessView.as_view(), name='sadnesses'),
    path('surprise', views.SurpriseView.as_view(), name='surprises'),
    path('search', views.search(), name='searches')
]