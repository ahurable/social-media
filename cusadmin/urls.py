from django.urls import path
from .views import CustomAdmin
urlpatterns = [
    path('', CustomAdmin.as_view(), name='custom_admin_url')
]