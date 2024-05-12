from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>', views.index, name='index'),
    path('profile', views.profile, name='profile')
]