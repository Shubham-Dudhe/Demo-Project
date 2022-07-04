from django.contrib import admin
from django.urls import path
from .views.signup import Signup
from .views.login import Login,logout
from .views.index import Index
from .views.cart import Cart
from .views.checkout import Checkout
from .views.orders import Order_history
from .middlewares.auth import auth_middleware
from .views.payment import Payment,success

urlpatterns = [
    path('',Index.as_view(), name='index'),
    path('signup',Signup.as_view(),name='signup'),
    path('login',Login.as_view(),name='login'),
    path('logout',logout,name='logout'),
    path('cart',Cart.as_view(),name='cart'),
    path('checkout',auth_middleware(Checkout.as_view()),name='checkout'),
    path('orders',auth_middleware(Order_history.as_view()),name='orders'),
    path('payment',Payment.as_view(),name='payment'),
    path('payment/success/',success,name='success'),
]