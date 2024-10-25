from django.urls import path
from .views import apply, user_list_view,register, login_view

urlpatterns = [
    path('apply/', apply, name='apply'),
    path('user-list/', user_list_view, name='user_list'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
]

