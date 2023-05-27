from django.contrib import admin
from django.urls import path, include


from dashboard.views import index

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('customers/', include('dashboard.urls')),
]
