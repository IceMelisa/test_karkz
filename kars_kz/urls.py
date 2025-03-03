from django.conf import settings
from django.urls import path
from .views import index,reg,log, profile, logout_view, change_password, edit_profile



urlpatterns = [
    path('', index, name='index'),
    path('reg/', reg, name='reg'),
    path('log/', log, name='log'),
    path('profile/', profile, name='profile'),
    path('logout/', logout_view, name='logout'), 
    path('change_password/', change_password, name='change_password'), 
    path('edit_profile/', edit_profile, name='edit_profile')
]

