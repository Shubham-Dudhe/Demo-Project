from django.shortcuts import render,redirect
from django.views import View
from store.models import Product,Customer,Order


class Payment(View):

    def get(self,request):
        
        product_list = list(request.session.get('cart').keys())
        products = Product.get_product_by_id(product_list)
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer_id(customer)
        return render(request,'paymentpage.html',{'orders':orders,'products':products})