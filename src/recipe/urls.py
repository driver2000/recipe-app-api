from django.urls import include, path
from rest_framework.routers import DefaultRouter

from recipe.views import TagViewSet

router = DefaultRouter()

router.register("tags", TagViewSet)

app_name = "recipe"

urlpatterns = [path("", include(router.urls))]
