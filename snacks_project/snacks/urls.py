from django.urls import path
from .views import SnacksViews ,AboutUs

urlpatterns = [
    path('', SnacksViews.as_view(), name = "home"),
    path("about_us/", AboutUs.as_view(), name = "about-us")
]