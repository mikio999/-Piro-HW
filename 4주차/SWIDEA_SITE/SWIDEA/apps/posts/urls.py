from django.urls import path
from . import views

urlpatterns = [
    path('', views.idea_list, name="idea_list"),
    path('idea_detail/<int:pk>', views.idea_detail, name="idea_detail"),
    path('devtool_list/', views.devtool_list, name="devtool_list")
]