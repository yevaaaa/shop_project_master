from django.urls import path
from shop import views as shop_views


urlpatterns = [
    path('homepage/',shop_views.home,name='shop-homepage')
]
