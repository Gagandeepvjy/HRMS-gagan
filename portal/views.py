from functools import wraps

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import redirect, render

from .forms import CustomAuthenticationForm, LeaveRequestForm, UserForm
from .models import LeaveRequest, Profile


def role_required(role):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect("login_view")

            profile = Profile.objects.get(user=request.user)
            if profile.role != role:
                return redirect("home")

            return view_func(request, *args, **kwargs)

        return wrapper

    return decorator


def home(request):
    return render(request, "portal/home.html")


@transaction.atomic
def signup(request):
    if request.method == "POST":
        user_form = UserForm(request.POST, request.FILES)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            user_form.save()
            user = authenticate(
                request,
                username=new_user.username,
                password=user_form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
            return redirect("home")
    else:
        user_form = UserForm()
    return render(request, "registration/signup.html", {"user_form": user_form})


def login_view(request):
    if request.method == "POST":
        user_form = CustomAuthenticationForm(request, data=request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data["username"]
            password = user_form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("base")
    else:
        user_form = CustomAuthenticationForm(request)
    return render(request, "Registration/login.html", {"user_form": user_form})


def logout_view(request):
    logout(request)
    return redirect("home")


@role_required("manager")
def manager_leave_approval(request):
    leave_requests = LeaveRequest.objects.all()
    return render(
        request,
        "portal/manager_leave_approval.html",
        {"leave_requests": leave_requests},
    )


@role_required("employee")
def employee_leave_request(request):
    if request.method == "POST":
        leave_form = LeaveRequestForm(request.POST)
        if leave_form.is_valid():
            leave_form.save()
    leave_form = LeaveRequestForm()
    return render(
        request, "portal/employee_leave_request.html", {"leave_form": leave_form}
    )


@role_required("manager")
def manager_page(request):
    return render(request, "portal/manager_page.html")


@role_required("employee")
def employee_page(request):
    return render(request, "portal/employee_page.html")


@login_required
def base(request):
    if request.user.is_authenticated:
        if request.user.profile.role == "manager":
            return redirect("manager_page")
        return redirect("employee_page")
    return render(request, "login.html")
