from django.urls import path

from . import views


app_name = 'posts'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('posts/<int:pk>', views.DetailView.as_view(), name='detail'),
    path('posts/<int:post_id>/add_comment', views.add_comment, name='add_comment'),
]
