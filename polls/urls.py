from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    #metodo 2
    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    path('', views.TableView.as_view(), name='tables'),
]