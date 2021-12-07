from django.urls import path
from .views import (
    SnacksViews, AboutUs,
    SnackListViews, SnackDetail,
    DeleteSnack, UpdateSnack,
    CreateSnack
)

urlpatterns = [
    path('home/', SnacksViews.as_view(), name="home"),
    path("about_us/", AboutUs.as_view(), name="about-us"),
    path("", SnackListViews.as_view(), name="snack_list"),
    path("<int:pk>", SnackDetail.as_view(), name="snack_detail"),
    path("update/<int:pk>", UpdateSnack.as_view(), name="update"),
    path("create/", CreateSnack.as_view(), name="create"),
    path("delete/<int:pk>", DeleteSnack.as_view(), name="delete"),

]
