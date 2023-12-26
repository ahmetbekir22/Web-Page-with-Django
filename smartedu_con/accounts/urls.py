from django.urls import path, include
from . import views

from allauth.account.views import LogoutView

urlpatterns = [
    path('login/', views.user_login, name="login"),
    path('register/', views.user_register, name="register"),
    path('dashboard/', views.user_dashboard, name="dashboard"),
    path('logout/', views.user_logout, name="logout"),
    path('enroll_the_course/', views.enroll_the_course, name="enroll_the_course"),
    path('release_the_course/', views.release_the_course, name="release_the_course"),
    path('social-auth/', include('social_django.urls',namespace='social')),
    path('accounts/logout/', LogoutView.as_view(), name='account_logout'),
]