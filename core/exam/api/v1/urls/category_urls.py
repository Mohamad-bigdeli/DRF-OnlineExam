from rest_framework.routers import DefaultRouter
from ..views import CategoryViewSet, FavoriteCategoryViewSet

app_name = "api-v1"

router = DefaultRouter()

urlpatterns = []

router.register(r"categories", CategoryViewSet, basename="categories")
router.register(
    r"favorite-categories", FavoriteCategoryViewSet, basename="favorite-categories"
)

urlpatterns += router.urls
