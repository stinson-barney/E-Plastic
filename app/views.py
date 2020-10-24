from django.shortcuts import render
from .models import *
from random import *
# Create your views here.

def IndexPage(request):
    return render(request,"app/index2.html")

def LoginPage(request):
    return render(request,"app/login.html")

def registerUser(request):
    if request.POST['role'] == "employee":
        role = request.POST['role']
        email = request.POST['email']
        print("Email------------->",email)
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        gender = request.POST['gender']
        contact = request.POST['contact']

        user = User.objects.filter(email = email)
        if user:
            message = "User already"
            return render(request,"app/index2.html",{'msg':message})
        else:
            if password == cpassword:
                otp = randint(10000,99999)
                newuser = User.objects.create(email = email,password = password,otp=otp,role=role)
                newemp = Employee.objects.create(user_id=newuser,Firstname = firstname ,Lastname=lastname,gender=gender,contact=contact)
                return render(request,"app/login.html")
            else:
                message = "password dosen't match"
                return render(request,"app/index2.html",{'msg':message})
    elif request.POST['role'] == "hirer":
        role = request.POST['role']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        gender = request.POST['gender']
        contact = request.POST['contact']

        user = User.objects.filter(email = email)
        if user:
            massage = "User already Exst"
            return render(request,"app/index2.html",{'msg':message})
        else:
            if password == cpassword:
                otp = randint(10000,99999)
                newuser = User.objects.create(email = email,password = password,otp=otp,role=role)
                newemp = Employee.objects.create(user_id=newuser,FirstName = firstname ,Lastname=lastname,gender=gender,contact=contact)
                return render(request,"app/login.html")
            else:
                message = "password dosen't match"
                return render(request,"app/index2.html",{'msg':message})

        print("invalid")

def LoginUser(request):
    if request.POST['role']=="employee":
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.filter(email=email)
        if user:
            if user.password == password and user.role == "employee":
                emp = Employee.objects.filter(user_id=user)
                request.session['email'] = user.email
                request.session['firstname'] = emp.Firstname
                return render(request,"app/home.html")



        