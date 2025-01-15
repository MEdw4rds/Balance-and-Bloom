from . import views
from django.urls import path
from .views import (
    LikeView, AddCategoryView, CategoryView, CategoryListView
)

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name="post_detail"),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('like/<slug:slug>', LikeView, name='like_post'),
    path('category-list/', CategoryListView, name='category-list'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]