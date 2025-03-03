from django.conf import settings
from django.urls import path
from .views import index,reg,log, profile, logout_view, change_password, edit_profile, create_post
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name='index'),
    path('reg/', reg, name='reg'),
    path('log/', log, name='log'),
    path('profile/', profile, name='profile'),
    path('logout/', logout_view, name='logout'), 
    path('change_password/', change_password, name='change_password'), 
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('create_post/', create_post, name='create_post'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 