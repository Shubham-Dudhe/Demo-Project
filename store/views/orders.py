from django.shortcuts import render,redirect
from django.views import View
from store.models import Product,Customer,Order


class Order_history(View):

    
    def get(self,request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer_id(customer)
        return render(request,'orderHistory.html',{'orders':orders})
