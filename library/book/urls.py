from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),  
    path('<int:book_id>/', views.book_detail, name='book_detail'), 
    path('filter/', views.book_filter, name='book_filter'),  
    path('user/<int:user_id>/', views.book_by_user, name='book_by_user'), 
]
