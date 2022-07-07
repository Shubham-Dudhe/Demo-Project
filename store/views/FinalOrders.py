from django.shortcuts import render
from django.views import View
from store.models import Product,Customer,Order,Coupon
from store.templatetags.cardsfilter import order_total


class ProcessOrders(View):

    
    def get(self,request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer_id(customer).filter(status=True).order_by('-date')
        return render(request,'proccess_orders.html',{'orders':orders})