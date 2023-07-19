from django.urls import path
from . import views

urlpatterns = [
    path('', views.idea_list, name="idea_list"),
    path('change_interest_rate/<int:pk>/<int:rate>/', views.change_interest_rate, name="change_interest_rate"),
    path('idea_detail/<int:pk>', views.idea_detail, name="idea_detail"),
    path('idea_detail/<int:pk>/like/', views.idea_like, name='idea_like'),
    path('devtool_list/', views.devtool_list, name="devtool_list"),
]