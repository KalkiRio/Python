from . import views
from django.urls import path

urlpatterns = [
    path('signup/', views.Signup, name="signup"),
    path('login/', views.LoginUser, name="login"),
]