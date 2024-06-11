from django.urls import path, include
from news.views import CategoryViewSet, UserViewSet, home, news_details, categories_form, news_form
from rest_framework import routers

router = routers.DefaultRouter()
router.register("categories", CategoryViewSet)
router.register("users", UserViewSet)




urlpatterns = [
    path("", home, name="home-page"),
    path("news/<int:id>", news_details, name="news-details-page"),
    path("categories", categories_form, name="categories-form"),
    path("news", news_form, name="news-form"),
    path("api/", include(router.urls)),
]