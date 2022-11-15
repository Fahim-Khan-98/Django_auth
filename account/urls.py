from django.urls import path
from account import views
app_name='account'
urlpatterns=[

    path('',views.home,name="home"),
    path('register/',views.registerRequest,name="register"),
    path('login/',views.loginRequest,name="login"),
    path("logout/", views.logoutRequest, name= "logout"),
    

]