
# from django.views.static import serve
from django.urls import path, include
from . import views
# authtoken
from rest_framework.authtoken.views import obtain_auth_token

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('auth/', obtain_auth_token),
    path('', views.api_home, name='api_home'),
    path('products/', include('products.urls')),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # path('products', views.add_products, name='add_products'),

    # path('profiles/', include([
    #     path('<int:id>/', include([
    #         path('', views.profile_adventurer, name='profile_adventurer'),
    #         path('achievements/<int:exp_id>',
    #              views.met_achievement_details, name='met_achievement_details')
    #     ])),
    # ])),

    # path('achievements/', views.met_all_achievements, name='met_all_achievements')

]
