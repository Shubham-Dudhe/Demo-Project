from django.shortcuts import render,redirect
from django.views import View
from store.models import Product,Customer,Order,Coupon
from store.templatetags.cardsfilter import order_total


class Order_history(View):

    
    def get(self,request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer_id(customer).filter(status=False)
        return render(request,'orderHistory.html',{'orders':orders})
    
    def post(self,request,id=None):
        if id is not None:
            coupon = Coupon.objects.get(id=id)
            coupon.is_applied = False
            error_message = 'Coupon Removed sucessfully'
            return render(request,'orderHistory.html',{'orders':orders,'error_message':error_message})
        else:
            customer = request.session.get('customer')
            orders = Order.get_orders_by_customer_id(customer).filter(status=False)
            coupon = request.POST.get('coupon')
            cart = request.session.get('cart')
            try:
                coupon_obj = Coupon.objects.get(coupon_code__icontains = coupon)
                coupon = Coupon.objects.get(coupon_code=coupon)
            except:
                error_message = 'Coupon does not exist'
                return render(request,'orderHistory.html',{'orders':orders,'error_message':error_message})
        
            if coupon_obj.is_expired:
                error_message = 'Coupon is expired'
                return render(request,'orderHistory.html',{'orders':orders,'error_message':error_message})
            elif order_total(orders)<coupon_obj.minimum_amount:
                error_message = 'Please make cart total of '+ str(coupon_obj.minimum_amount)
                return render(request,'orderHistory.html',{'orders':orders,'error_message':error_message})

            coupon = Coupon.objects.get(coupon_code=coupon)
            discounted_price = Coupon.modify_order_total(coupon.discount_price,orders)
            message = 'Coupon Applied Sucessfully'
            coupon.is_applied = True
            return render(request,'orderHistory.html',{'orders':orders,'discounted_price':discounted_price,'message':message,'coupon_obj':coupon_obj})