from django.contrib import admin
from django.urls import path
from . import views
from therapist_profiles import views as index_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_views.index, name='index'),
    path('profile/', views.create_or_update_profile, name='create_or_update_profile'),
    path('profile/<int:user_id>/', views.view_profile, name='view_profile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)