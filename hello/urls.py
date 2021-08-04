from django.urls import path

from hello import views

urlpatterns = [
    path('', views.hello),
    path('home/', views.home),
]