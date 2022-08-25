from django_distill import distill_path
from django.urls import path
from .views import HomePageView


def get_static_template():
    return None


urlpatterns = [
    distill_path(
        "",
        HomePageView.as_view(),
        name="home_page",
        distill_func=get_static_template,
        distill_file="index.html",
    ),
]
