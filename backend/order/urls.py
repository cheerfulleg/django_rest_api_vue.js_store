from rest_framework import routers

from .views import OrderViewSet, OrderItemViewSet

app_name = 'orders'

router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)

urlpatterns = router.urls
