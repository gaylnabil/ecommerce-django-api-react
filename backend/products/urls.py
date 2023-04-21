
# from django.views.static import serve
from django.urls import path
from . import views

urlpatterns = [
    # Using Generics API View
    path('', views.product_list_create_view),
    path('<int:pk>/', views.product_detail_view),
    path('<int:pk>/update/', views.product_update_view),
    path('<int:pk>/delete/', views.product_destroy_view),

    # ****************************************************

    # # Using Decorator @api_view(['GET'])
    # path('<int:pk>/', views.product_alt_view),

    # ****************************************************

    # # Using Mixin and Generics API View
    # path('', views.product_mixin_view),
    # path('<int:pk>/', views.product_mixin_view),
    # path('<int:pk>/update/', views.product_mixin_view),
    # path('<int:pk>/delete/', views.product_mixin_view),



]
