from django.urls import path
from . import views

app_name = "opportunities"
urlpatterns = [
    path("", views.home, name="home"),
    path("opportunities/", views.opportunity_list, name="list"),
    path("opportunities/<int:pk>/", views.opportunity_detail, name="detail"),
    path("opportunities/<int:pk>/apply/", views.apply, name="apply"),
    path("sign-up/", views.sign_up, name="sign_up"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
