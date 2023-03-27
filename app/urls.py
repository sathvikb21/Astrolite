from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('signup', views.signuppage, name='signup'),
    path('login', views.loginpage, name='login'),
    path('logout', views.logoutpage, name='logout'),
]
