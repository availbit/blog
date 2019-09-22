from django.shortcuts import render
from ./models import MyUser
form django.shortcuts import redirect

# Create your views here.

def signup(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]

            return redirect('post_list')

def signin(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]

            return redirect('post_list')

