from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),
    path('start/<int:quiz_id>/', views.start_quiz, name='start_quiz'),
    path('result/<int:quiz_id>/<str:score>/', views.quiz_result, name='quiz_result'),
]
