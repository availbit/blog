from django.urls import path
from . import views

urlpatterns = [
        path('myuser/signup', views.signup, name='signup'),
        path('myuser/signin', views.signin, name='signin'),

]
