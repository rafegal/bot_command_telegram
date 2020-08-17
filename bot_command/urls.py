from django.urls import path
from django.contrib import admin
from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("event/", views.event),
]
