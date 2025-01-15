from django.contrib import admin
from django.urls import path, include
from . import views
from therapist_profiles import views as index_views
from django.conf import settings
from django.conf.urls.static import static
from therapist_profiles import views as therapist_views

urlpatterns = [
    path('', therapist_views.index, name='index'),
    path('profile/', therapist_views.create_or_update_profile, name='create_or_update_profile'),
    path('profile/<str:username>/', therapist_views.view_profile_by_username, name='view_profile_by_username'),
    path('profile/<int:user_id>/', therapist_views.view_profile_by_id, name='view_profile_by_id'),
    path('therapist_profile/', therapist_views.view_profile, name='therapist_profile'),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
