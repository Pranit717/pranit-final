from django.urls import path, include
from .import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import re_path
from django.views.static import serve


urlpatterns = [
    path('',views.search, name='search'),
    path('create/',views.create, name='create'),
] + static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
