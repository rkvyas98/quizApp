from django.shortcuts import render, HttpResponse, redirect
from static.questions_file import questions_file as qf
from .models import Question, Test_stat
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from json import dumps

# Create your views here.
def index(request):
    # Loading Tests data from DB
    tests_data = Test_stat.objects.all()
    total_test = len(tests_data)
    total_marks = 0
    for test in tests_data:
        total_marks += test.score
    avg_marks = float(total_marks/total_test)
    avg_marks = round(avg_marks,2)
    context={
        'total_test' : total_test,
        'avg_marks' : avg_marks
    }
    return render(request, 'index.html', context)


def fetch_data(subject, language):
    # Loading Questions from DB
    data = Question.objects.filter(subject=subject)
    answers = []
    for d in data:
        answers.append(d.answer)
    
    # Loading Tests data from DB
    tests_data = Test_stat.objects.all()
    total_test = len(tests_data)
    total_marks = 0
    for test in tests_data:
        total_marks += test.score
    avg_marks = float(total_marks/total_test)
    avg_marks = round(avg_marks,2)
    context ={
        'all_data' : data,
        'o' : 1,
        'language' : language,
        'answers' : answers,
        'total_test' : total_test,
        'avg_marks' : avg_marks
    }
    return context

def quiz(request,sub):
    context= {}
    if sub == 'c':
        context = fetch_data("C Programming", "C")
    elif sub == 'cpp':
        context = fetch_data("C++ Programming", "C++")
    elif sub == 'java':
        context = fetch_data("Java Programming", "Java")
    elif sub == 'python':
        context = fetch_data("Python Programming", "Python")
    elif sub == 'js':
        context = fetch_data("Javascript Programming", "Javascript")
    else:
        context = fetch_data("","")
    if request.method == 'POST':
        username = request.POST['username']
        score = request.POST['score']
        subject = request.POST['subject']
        print("Score is", username, subject, score)
        test = Test_stat(username = username, score = score, subject= subject)
        test.save()
        messages.success(request, "Your Quiz data has been successfully uploaded!")

    return render(request, 'quiz.html', context)


def tests_stats(request):
    # Loading Tests data from DB
    tests_data = Test_stat.objects.all()
    total_test = len(tests_data)
    total_marks = 0
    for test in tests_data:
        total_marks += test.score
    avg_marks = float(total_marks/total_test)
    avg_marks = round(avg_marks,2)

    # Top Scorer
    users = []
    top_scorer = [0,]
    for user in tests_data:
        users.append(user.username)
    users = list(set(users))
    top_user = ""
    test_count = 0
    for test in tests_data:
        if test.score > top_scorer[0]:
            top_scorer[0] = test.score 
            username = test.username
        top_user = username
    for test in tests_data:
        if test.username == username:
            test_count += 1
    top_scorer.append(top_user)
    top_scorer.append(test_count)

    # Highest attempt user
    top_user = [0,]
    total_attempts = 0
    total_score = 0
    t_user = ""
    for user in users:
        attempts = 0
        score = 0
        for test in tests_data:
            if user == test.username:
                attempts += 1
                score += test.score
        if attempts> total_attempts:
            total_attempts = attempts
            total_score = score
            t_user = user
    top_user[0] = total_attempts
    top_user.append(round(float(total_score/total_attempts),2))
    top_user.append(t_user)

    context={
        'total_test' : total_test,
        'avg_marks' : avg_marks,
        'tests_data' : tests_data,
        'top_scorer' :top_scorer,
        'top_user' : top_user
    }
    return render(request, 'tests_stats.html', context)

def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for inputs
        if len(username) > 10:
            messages.error(request, "Username should contain less than 10 characters.")
            return redirect('index')
        
        if not username.isalnum():
            messages.error(request, "Username should only contain letters and numbers.")
            return redirect('index')

        if pass1 != pass2:
            messages.error(request, "Passwords donot match. ")
            return redirect('index')

        # creating users
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your QuizApp account has been successfully created!")

        return redirect('index')
    else:
        return HttpResponse("404 Not found!")

def handleLogin(request):
    if request.method == 'POST':
        # Getting post params
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username = loginusername, password = loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In!")
            return redirect('index')
        
        else:
            messages.error(request, "Invalid Credentials, Please Try Again!")
            return redirect('index')

    return HttpResponse('404 - Not Found')

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out!")
    return redirect('index')



def student(request):
    return HttpResponse("This is student's page")

def teacher(request):
    return HttpResponse("This is teacher's page")

def insert_data(request):
    '''
    Inserting Questions
    for data in qf.c_data:
        question = Question(question = data[0],option1 = data[1],option2 = data[2],option3 = data[3],option4 = data[4],option5 ="",answer=0)
        question.save()

    for data in qf.cpp_data:
        question = Question(question = data[0],option1 = data[1],option2 = data[2],option3 = data[3],option4 = data[4],option5 ="",answer=0)
        question.save()
    
    for data in qf.java_data:
        question = Question(question = data[0],option1 = data[1],option2 = data[2],option3 = data[3],option4 = data[4],option5 ="",answer=0)
        question.save()
    
    for data in qf.py_data:
        question = Question(question = data[0],option1 = data[1],option2 = data[2],option3 = data[3],option4 = data[4],option5 ="",answer=0)
        question.save()
    for data in qf.js_data:
        question = Question(question = data[0],option1 = data[1],option2 = data[2],option3 = data[3],option4 = data[4],option5 ="",answer=0)
        question.save()
    '''

    ''' 
    Inserting Answers
    i = 1
    for a in qf.c_answers:
        ans = Question.objects.get(question_id=i)
        ans.answer = a
        ans.save()
        i+=1
    for a in qf.cpp_answers:
        ans = Question.objects.get(question_id=i)
        ans.answer = a
        ans.save()
        i+=1
    for a in qf.java_answers:
        ans = Question.objects.get(question_id=i)
        ans.answer = a
        ans.save()
        i+=1
    for a in qf.py_answers:
        ans = Question.objects.get(question_id=i)
        ans.answer = a
        ans.save()
        i+=1
    for a in qf.js_answers:
        ans = Question.objects.get(question_id=i)
        ans.answer = a
        ans.save()
        i+=1
    '''
    '''
    for i in range(41,51):
        sub = Question.objects.get(question_id=i)
        sub.subject = "Javascript Programming"
        sub.save()
    '''

    return HttpResponse("Done")

