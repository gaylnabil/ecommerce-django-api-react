from rest_framework.routers import DefaultRouter

from products.viewsets import ProductViewSet

router = DefaultRouter()

router.register(
    'products-abc',
    ProductViewSet,
    basename='products'
)

print('router.urls: ', router.urls)
urlpatterns = router.urls
