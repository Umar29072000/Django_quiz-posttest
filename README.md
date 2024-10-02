# Django Quiz Application

This project is a web-based quiz application built using Django. It allows users to register, log in, take quizzes, and see their results.

## Features

- **User Registration and Authentication:** Users can register, log in, and log out.
- **Quiz System:** Users can select and start quizzes, answer questions, and see their final score.
- **Admin Panel:** Admins can add, modify, and delete quiz questions through the Django admin panel.
- **SQLite Database:** Stores user data, quizzes, and questions for easy management.

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository:**
   ```bash
   git clone <REPOSITORY_URL>
   ```

2. **Navigate to the project directory:**
   ```bash
   cd Django_quiz-posttest-main
   ```

3. **Create a virtual environment:**
   ```bash
   python -m venv env
   ```

4. **Activate the virtual environment:**
   ```bash
   env\Scripts\activate
   ```

5. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

6. **Migrate the database:**
   ```bash
   python manage.py migrate
   ```

7. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

8. **Run the server:**
   ```bash
   python manage.py runserver
   ```

# Deployment
vercel : https://django-quiz-posttest.vercel.app/quiz/
