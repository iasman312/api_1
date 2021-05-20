from django.urls import path
from api_v1.views import get_token_view, add_view, subtract_view, multiply_view, divide_view

urlpatterns = [
    path('add/', add_view, name='add'),
    path('subtract/', subtract_view, name='subtract'),
    path('multiply/', multiply_view, name='multiply'),
    path('divide/', divide_view, name='divide'),
    path('get_token/', get_token_view, name='get-token')
]