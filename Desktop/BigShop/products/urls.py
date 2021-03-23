from django.urls import path, include

from .views import prod_by_category_view, product_detail, all_prod_of_category_view
from carts.views import add_to_cart, remove_from_cart, CartView, decreaseCart, increaseCart

app_name = 'mainapp'

urlpatterns = [
    path('', prod_by_category_view, name='prod_by_category'),
    path('detail/<slug>/',  product_detail, name='product-detail'),
    path('category/all/<int:id>/', all_prod_of_category_view, name='all_prod_of_category'),
    path('add/<slug>/', add_to_cart, name='add-cart'),
    path('remove/<slug>/', remove_from_cart, name='remove-cart'),
    path('cart/', CartView, name='cart-home'),
    path('decrease/<slug>', decreaseCart, name='decrease-cart'),
     path('increase/<slug>', increaseCart, name='increase-cart'),
]