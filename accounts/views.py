from django.contrib.auth import get_user_model, login, logout
from django.shortcuts import render, redirect

# Create your views here.
#Afficher l'utilisateur connecte
User = get_user_model()

def singup(request) :
    if request.method == "POST" :
        # Traiter le formulaire
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username,
                                        password=password)
        login(request, user)
        return redirect('index')
    return render(request, 'accounts/singup.html')

def logout_user(request):
    logout(request)
    return redirect('index')