from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name="movie_list"),
    path('review_list/', views.review_list, name="review_list"),
    path('review_list/<int:pk>', views.review_list_info, name="review_list_info"),
    path('create_review/', views.create_review, name="create_review"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('join/', views.join, name='join'),
]