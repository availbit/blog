from django.urls import path
from . import views


urlpatterns = [
        path('myuser/sign_up', views.sign_up, name='sign_up'),
        path('myuser/sign_in', views.sign_in, name='sign_in'),
]
