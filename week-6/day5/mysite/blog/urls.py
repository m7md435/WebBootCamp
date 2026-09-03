from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='list'),
    path('post/<int:post_id>/', views.post_detail, name='detail'),
    path('category/<slug:category>/', views.category_posts, name='category'),
]