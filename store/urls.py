from django.conf.urls.static import static
from django.urls import path

from website import settings
from . import views

urlpatterns = [
                  path('', views.home, name='home'),
                  path('product', views.product),
                  path('contact', views.contact),
              ]
