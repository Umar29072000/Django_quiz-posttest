from django import forms
from .models import Question, Answer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super(QuizForm, self).__init__(*args, **kwargs)
        for question in questions:
            answers = Answer.objects.filter(question=question)
            choices = [(answer.pk, answer.text) for answer in answers]
            self.fields[f'question_{question.pk}'] = forms.ChoiceField(
                label=question.text, choices=choices, widget=forms.RadioSelect)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
