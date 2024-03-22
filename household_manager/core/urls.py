from django.urls import path
from . import views

urlpatterns =[
    path('', views.homepage,name='home'),
    path('login', views.loginPage, name='login' ),
    path('logout', views.logoutPage, name='logout'),
    path('register/', views.registerPage,name='register'),
    path('family_leader/<username>/', views.familyLeader, name='family_leader')
    
]