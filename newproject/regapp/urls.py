from . import views
from django.urls import path


urlpatterns = [
    path('regapp/register',views.register ,name='register'),
    path('regapp/regapp/login',views.req ,name='req'),
    path('register',views.register ,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('regapp/regapp/Welcome.html', views.req, name='req'),
    path('regapp/regapp/index.html', views.home, name='home'),



    # , regapp/regapp/register,
]