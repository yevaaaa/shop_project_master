from django.urls import path
from users import views as user_views


urlpatterns = [
    path('homepage/',user_views.home,name='shop-homepage'),
    path('index/',user_views.home,name='shop-index')

]