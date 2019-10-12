from django.shortcuts import render, redirect
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
            user.password = form.cleaned_data["password"]
            #user.registered_date = timezone.now()
            user.save()
            return render(request, 'myuser/sign_in.html', {'form':form})
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

        print(f'OBJECTS: {user}')
        print(f'OBJECTS: {user.username}, {user.password}')

        if user and user.password == password:
            return render(request, 'myblog/post_list.html')
        else:
            return render(request, 'myuser/sign_in.html')
    else:
        form = SignInForm()
        return render(request, 'myuser/sign_in.html', {'form':form})

