from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('board/<slug:slug>/<str:password>/', views.board_detail, name='board_detail'),
    path('create/', views.create_board, name='create_board'),
    #path('accounts/login/', auth_views.LoginView.as_view(), name='login'),

]
