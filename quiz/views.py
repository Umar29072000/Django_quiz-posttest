from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from .models import Quiz, Question, Answer, QuizAttempt
from .forms import QuizForm, UserRegisterForm

def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz_list.html', {'quizzes': quizzes})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Account created successfully for {user.username}!')
            return redirect('quiz_list')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def start_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    if request.method == 'POST':
        form = QuizForm(request.POST, questions=questions)
        if form.is_valid():
            score = 0
            for question in questions:
                selected_answer_id = form.cleaned_data[f'question_{question.pk}']
                selected_answer = Answer.objects.get(pk=selected_answer_id)
                if selected_answer.is_correct:
                    score += 1
            score_percentage = (score / len(questions)) * 100
            QuizAttempt.objects.create(user=request.user, quiz=quiz, score=score_percentage)
            return redirect('quiz_result', quiz_id=quiz.id, score=score_percentage)
    else:
        form = QuizForm(questions=questions)
    return render(request, 'start_quiz.html', {'quiz': quiz, 'form': form})

# @login_required
def quiz_result(request, quiz_id, score):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    score = float(score)
    return render(request, 'quiz_result.html', {'quiz': quiz, 'score': score})