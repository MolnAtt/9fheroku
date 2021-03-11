from django.contrib import admin
from django.urls import path

from app_toc.views import tocview
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tocview),
]
