from django.urls import path, include
from . import views

app_name = 'pirostagram'

urlpatterns = [
    path("", views.index, name='index'),
    path('pirostagram/change_like_rate/<int:pk>/<int:rate>/', views.change_like_rate, name="change_like_rate"),
    path('pirostagram/submit_comment/<int:reddit_id>/', views.submit_comment, name='submit_comment'),
    path('pirostagram/register/', views.register, name="register")
    ]
