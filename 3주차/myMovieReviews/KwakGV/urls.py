from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name="movie_list"),
    path('review_list/', views.review_list, name="review_list"),
    path('review_list/<int:pk>', views.review_list_info, name="review_list_info")
]