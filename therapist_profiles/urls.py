from django.contrib import admin
from django.urls import path, include
from . import views
from therapist_profiles import views as index_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('admin/', admin.site.urls),
    path('', index_views.index, name='index'),
    path('profile/', views.create_or_update_profile, name='create_or_update_profile'),
    path('profile/<str:username>/', views.view_profile_by_username, name='view_profile_by_username'),
    path('profile/<int:user_id>/', views.view_profile_by_id, name='view_profile_by_id'),
    path('accounts/', include('allauth.urls')),
    path('', views.create_or_update_profile, name='create_or_update_profile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
