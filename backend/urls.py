from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('backend.core.urls', namespace='core')),
    path('accounts/', include('backend.accounts.urls')),  # sem namespace
    path('', include('backend.patient.urls', namespace='patient')),
    path('admin/', admin.site.urls),
]
