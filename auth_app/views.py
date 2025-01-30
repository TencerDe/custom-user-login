import requests
from django.shortcuts import render, redirect
from .models import CustomUser
from django.conf import settings

# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password  = request.POST.get("password")

        if CustomUser.objects.filter(username=username).exists():
            return render(request, 'sign_up.html', {'error': 'Username already exists.'})
        
        user = CustomUser(username=username, email=email)
        user.set_password(password)
        user.save()

        return redirect("log_in")
    return render(request, 'sign_up.html')

def log_in(request):
           if request.method == "POST":
                username = request.POST.get("username")
                password = request.POST.get("password")

                try:
                      user = CustomUser.objects.get(username=username)
                      if user.check_password(password):
                            request.session["user_id"] = user.id
                            return redirect("dashboard")
                      else:
                            return render(request, "log_in.html", {"error": "Invalid credentials"})
                except CustomUser.DoesNotExist:
                      return render(request, "log_in.html", {"error": "user not found"})
                
                return render(request,"log_in.html")
           
def log_out(request):
      request.session.flush()
      return redirect("log_in")

def google_login(request):
      gogle_auth_url = (
            "https://accounts.google.com/o/oauth2/auth?"
        "response_type=code"
        f"&client_id={settings.GOOGLE_CLIENT_ID}"
        "&scope=email profile"
        f"&redirect_uri={settings.GOOGLE_REDIRECT_URL}"
      )


