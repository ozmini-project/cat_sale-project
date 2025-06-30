from django.urls import path
from . import views

urlpatterns = [
    path('preferences/', views.	ListView.as_view()),
    path('preferences/create/', views.CreateView.as_view()),
    path('preference/<int:adoption_id>/', views.DetailView.as_view()),
    path('matches/', views.MatchesList.as_view()),
    path('run-matching/', views.RunMatchingView.as_view()),

]

