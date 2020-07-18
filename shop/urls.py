from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

from . import views
# from .views import *

# router = routers.DefaultRouter()
# router.register(r'merch', views.HeroViewSet)

urlpatterns = [
    # path('signup/', views.signup, name='signup'),
    # path('account/', include('django.contrib.auth.urls')), 
    # path('', views.index, name='index'), 
    path('users/', views.ListUsersView.as_view({'post': 'list', 'get': 'list'}), name='users'),
    path('products/', views.ListProductsView.as_view({'post': 'list', 'get': 'list'}), name='products')

]