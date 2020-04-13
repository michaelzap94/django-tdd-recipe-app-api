from django.contrib import admin
from django.urls import path
from . import views

app_name = 'user'
# we need .as_view() because 'CreateUserView' is a class with no return render/redirect
urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
]
