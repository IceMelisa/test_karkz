from django.contrib import admin
from django.urls import path, include
from kars_kz.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('kars_kz.urls')),  
    

]

