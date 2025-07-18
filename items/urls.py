from django.urls import path
from . import views


urlpatterns = [
    path('', views.home , name='home' ),
    path('sell/' , views.sellItem, name='sell'),
    path('view/<int:item_id>' ,views.viewItem , name='view'),
    path('cart/' , views.cart_view, name='cart'),
     path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),

]
