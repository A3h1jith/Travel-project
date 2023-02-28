from django.urls import path

from credentials import views

urlpatterns=[
    path('register',views.registration,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')
]