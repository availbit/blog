from django.shortcuts import render, redirect
from .models import MyUser
from .forms import SignUpForm
from .forms import SignInForm


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = request.POST["username"]
            user.password = request.POST["password"]
            user.save()
            return render(request, 'myuser/sign_up.html', {'form':form})

def signin(request):
    if request.method == "GET":
        form = SignInForm(request.GET)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]

            user = MyUser.objects.filter(username=username)

            if user.password == password:
                return redirect(request, 'myuser/sign_in.html', {'form':form})
            else:
                return render('post_list')
