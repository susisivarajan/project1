from .import views
from django.urls import path

urlpatterns=[
    path("",views.index,name='index'),
    path("home", views.register, name='home'),
    path("login",views.login,name="login"),
]