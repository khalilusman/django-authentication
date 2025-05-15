from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    
    # path('',view.home,  name='home' ),
    path('', views.post_list , name='post'),
    path('new_post/', views.new_post, name="new-post"),
    path('<slug:slug>', views.post_page, name="page"),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='delete_post'),
]