from rest_framework.routers import DefaultRouter

# from products.viewsets import ProductViewSet
from products.viewsets import ProductViewSetListCreateAPIView

router = DefaultRouter()

# # for ProductViewSet
# router.register(
#     'products',
#     ProductViewSet,
#     basename='products'
# )

# for ProductViewSetListCreateAPIView
router.register(
    'products',
    ProductViewSetListCreateAPIView,
    basename='products'
)


print('router.urls: ', router.urls)
urlpatterns = router.urls
