from django.urls import path

from . import views

# Register your models here.

urlpatterns = [
    path('create/', views.CreateUserView.as_view())
]
