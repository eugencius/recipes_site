from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.Register.as_view(), name="register"),
    path('login/', views.Login.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='accounts:login'), name="logout"),
    path('dashboard/', views.Dashboard.as_view(), name="dashboard"),

]
