from django.contrib import admin
from django.urls import path, include
from AppPersonajes.views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", inicio, name="inicio"),
    path("AppPersonajes/", include("AppPersonajes.urls")),
]
