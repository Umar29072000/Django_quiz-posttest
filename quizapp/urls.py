from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from quiz import views as quiz_views
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quiz/', include('quiz.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/register/', quiz_views.register, name='register'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', lambda request: redirect('quiz_list')),
]