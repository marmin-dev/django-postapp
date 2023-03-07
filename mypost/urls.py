from django.urls import path, include
from mypost import views

app_name = 'mypost'
urlpatterns = [
    # /post/
    path('', views.IndexView.as_view(), name='index'),

    # /post/id/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    # /post/all/
    path('post/all/',views.PostListView.as_view(), name='all'),

    # /post/id/delete/
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

    # /post/id/update
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),

    # /post/id/post
    path('<int:pk>/post/', views.PostCreateView.as_view(), name='post_create')

]
