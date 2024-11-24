from . import views
from django.urls import path

urlpatterns = [
    
    path('', views.rev_list,name='rev_list'),
    path('create/', views.rev_create,name='rev_create'),
    path('<int:rev_id>/del/', views.rev_del,name='rev_del'),
    path('<int:rev_id>/edit/', views.rev_edit,name='rev_edit'),
    path('register/', views.register,name='register'),
]

