from rest_framework import routers

from .views import ItemViewSet, CategoryViewSet

app_name = 'items'

router = routers.DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = router.urls
