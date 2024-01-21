from django.shortcuts import redirect, render

from .forms import SignUpForm


def home(request):
    return render(request, "portal/home.html")


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # You can redirect to a success page or perform other actions
            return redirect("home")
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})
