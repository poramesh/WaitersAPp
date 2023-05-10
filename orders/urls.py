
from django.urls import path
from .views import OrderListView, OrderDetailView, OrderCreateView, OrderUpdateView,OrderDeleteView
from . import views

urlpatterns = [
    #path('', views.home, name='orders-home'),
    path('',OrderListView.as_view(), name = 'orders-home'),
    path('Order/<int:pk>/',OrderDetailView.as_view(), name = 'orders-detail'),
    path('Order/new/',OrderCreateView.as_view(), name = 'orders-create'),
    path('Order/<int:pk>/update/',OrderUpdateView.as_view(), name = 'orders-update'),
    path('Order/<int:pk>/delete/',OrderDeleteView.as_view(), name = 'orders-delete'),


    path('about/', views.about, name='orders-about'),

]