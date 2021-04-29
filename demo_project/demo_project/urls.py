from django.urls import path
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="home.html")),
]

handler404 = 'perfect404.views.page_not_found'
