
# from django.views.static import serve
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_products, name='get_products'),
    path('products/', include('products.urls')),
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
