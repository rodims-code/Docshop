from django.shortcuts import render

# Create your views here.
def singup(request) :
    return render(request, 'accounts/singup.html')