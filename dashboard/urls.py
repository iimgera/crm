from django.urls import path
from dashboard import views


urlpatterns = [
    path('', views.index, name='index'),
    path('customer/list', views.CustomerListView.as_view(), name='customer-list'),
    path('customer/create/', views.CustomerCreateView.as_view(), name='customer-create'),
    path('customer/<int:pk>/', views.CustomerDetailView.as_view(), name='customer-detail'),
    path('<int:pk>/update/', views.CustomerUpdateView.as_view(), name='customer-update'),
    path('<int:pk>/delete/', views.CustomerDeleteView.as_view(), name='customer-delete'),
    path('employee/list/', views.EmployeeListView.as_view(), name='employee-list'),
    path('employee/create/', views.EmployeeCreateView.as_view(), name='employee-create'),
    path('employee/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee-detail'),
    path('employee/<int:pk>/update/', views.EmployeeUpdateView.as_view(), name='employee-update'),
    path('employee/<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='employee-delete'),
    path('order/list/', views.OrderListView.as_view(), name='order-list'),
    path('order/create/', views.OrderCreateView.as_view(), name='order-create'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
    path('order/<int:pk>/update/', views.OrderUpdateView.as_view(), name='order-update'),
    path('order/<int:pk>/delete/', views.OrderDeleteView.as_view(), name='order-delete'),


]