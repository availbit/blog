from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password
from .models import MyUser
from .forms import SignUpForm
from .forms import SignInForm


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            print(f'CLEANED:{form.cleaned_data}')
            user = form.save(commit=False)
            user.username = form.cleaned_data["username"]
            user.password = make_password(form.cleaned_data["password"])
            user.save()
            return redirect('sign_in')
        else:
            return render(request, 'myuser/sign_up.html')
    else:
        return render(request, 'myuser/sign_up.html')

def sign_in(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = MyUser.objects.get(username=username)

        if user and check_password(password, user.password):
            
            request.session['id'] = username
            request.user.is_authenticated= True
            return redirect(request, 'myblog/post_list')
        else:
            return render(request, 'myuser/sign_in.html')
    else:
        return render(request, 'myuser/sign_in.html')

def sign_out(request):
    if request.method == "POST":
        form = SignOutForm(request.POST)

        username = request.POST["username"]

        return redirect(request, 'myuser/sign_in.html')
    else:
        return render(request, 'myuser/sign_out.html')

