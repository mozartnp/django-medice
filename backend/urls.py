from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('backend.core.urls', namespace='core')),
    path('', include('backend.custom_user.urls', namespace='custom_user')),
    path('admin/', admin.site.urls),
]
