from django.urls import path
from .views import *


urlpatterns = [
    path('', CarViewSet.as_view({'get': 'list',
                                 'post': 'create'}), name='car_list'),
    path('<int:pk>/', CarViewSet.as_view({'get': 'retrieve',
                                          'put': 'update', 'delete': 'destroy'}), name='car_detail'),

    path('marka/', MarkaViewSet.as_view({'get': 'list',
                                             'post': 'create'}), name='car_list'),
    path('marka/<int:pk>/', MarkaViewSet.as_view({'get': 'retrieve',
                                                      'put': 'update', 'delete': 'destroy'}), name='car_list'),

    path('model/', ModelViewSet.as_view({'get': 'list',
                                             'post': 'create'}), name='car_list'),
    path('model/<int:pk>/', ModelViewSet.as_view({'get': 'retrieve',
                                                      'put': 'update', 'delete': 'destroy'}), name='car_list'),
    path('category/', CategoryViewSet.as_view({'get': 'list',
                                         'post': 'create'}), name='car_list'),
    path('category/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve',
                                                  'put': 'update', 'delete': 'destroy'}), name='car_list'),
    path('bet/', BetViewSet.as_view({'get': 'list',
                                             'post': 'create'}), name='car_list'),
    path('bet/<int:pk>/', BetViewSet.as_view({'get': 'retrieve',
                                                      'put': 'update', 'delete': 'destroy'}), name='car_list'),
]


