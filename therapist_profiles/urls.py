from django.contrib import admin
from django.urls import path, include
from . import views
from therapist_profiles import views as index_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('username/<str:username>/', views.view_profile_by_username, name='view_profile_by_username'),
    path('', views.create_or_update_profile, name='create_or_update_profile'),
    path('profiles/', views.therapist_profiles, name='therapist_profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
