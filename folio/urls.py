from . import views
from .views import HomePage, AboutPage
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'folio'

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('about', AboutPage.as_view(), name= 'about')
]
