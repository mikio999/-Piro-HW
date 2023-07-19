from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.idea_list, name="idea_list"),
    path('posts/idea_register/', views.idea_register, name="idea_register"),
    path('posts/idea_modify/<int:pk>', views.idea_modify, name='idea_modify'),
    path('posts/idea_delete/<int:pk>', views.idea_delete, name='idea_delete'),
    path('posts/change_interest_rate/<int:pk>/<int:rate>/', views.change_interest_rate, name="change_interest_rate"),
    path('posts/idea_detail/<int:pk>', views.idea_detail, name="idea_detail"),
    path('posts/idea_detail/<int:pk>/like/', views.idea_like, name='idea_like'),
    path('devtool_list/', views.devtool_list, name="devtool_list"),
    path('posts/devtool_register/', views.devtool_register, name="devtool_register"),
    path('posts/devtool_detail/<int:pk>', views.devtool_detail, name='devtool_detail'),
    path('posts/devtool_modify/<int:pk>', views.devtool_modify, name='devtool_modify'),
    path('posts/devtool_delete/<int:pk>', views.devtool_delete, name="devtool_delete")
]