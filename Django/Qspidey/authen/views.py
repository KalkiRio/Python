from django.shortcuts import render

# Create your views here.
def Signup(request):
    return render(request, 'signup.html')

def LoginUser(request):
    return render(request, 'login.html')