from django.conf.urls import url
from django.urls import path

from .views import indexPageView, contactPageView

urlpatterns = [
    path('', indexPageView, name='home'),
    path('home/', contactPageView, name='contact_us')
]
