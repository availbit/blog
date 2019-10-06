from django.shortcuts import render, redirect
from .models import MyUser
from .forms import SignUpForm
from .forms import SignInForm


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        user = form.save(commit=False)
        user.username = request.POST["username"]
        user.password = request.POST["password"]
        user.save()
        return render(request, 'myuser/sign_in.html', {'form':form})
    else:
        return render(request, 'myuser/sign_up.html')

def sign_in(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]

        user = MyUser.objects.filter(username=username)

        if user and user.password == password:
            return HttpResponseRedirect('post_list')
        else:
            return render(request, 'myuser/sign_in.html', {'form':form})
    else:
        form = SignInForm()
        return render(request, 'myuser/sign_in.html', {'form':form})

