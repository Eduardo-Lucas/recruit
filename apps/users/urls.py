from django.urls import path

from .views import *

app_name = 'users'

urlpatterns = [
    path('edit/<int:pk>', CustomUserUpdateView.as_view(), name='users_edit'),

]
