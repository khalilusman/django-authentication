from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    
    # path('',view.home,  name='home' ),
    path('', views.post_list , name='post'),
    path('new_post/', views.new_post, name="new-post"),
    path('<slug:slug>', views.post_page, name="page"),
]