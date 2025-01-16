from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_time_slot, name='book_time_slot'),
    path('booking_list/', views.booking_list, name='booking_list'),
    path('edit_booking/<int:booking_id>/',
         views.edit_booking, name='edit_booking'),
    path('booking/delete/', views.delete_booking, name='delete_booking'),
    path('booking_success/', views.booking_success, name='booking_success'),
]
