from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("base", views.base, name="base"),
    # Auth
    path("signup", views.signup, name="signup"),
    path("login", views.login_view, name="login_view"),
    path("logout", views.logout_view, name="logout_view"),
    # Role
    path("employee_page", views.employee_page, name="employee_page"),
    path("manager_page", views.manager_page, name="manager_page"),
    # Api
    path("api/", include("api.urls")),
]
