from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', first,name="home"),
    path('login/', Login,name="login"),
    path('signup/', Signup),
    path('addtodo/',addtodo),
    path('deletetodo/<int:id>',deletetodo),
    path('changestatus/<int:id>/<str:status>',changetodo),
    path('logout',signout)
]
