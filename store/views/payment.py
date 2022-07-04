from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from store.models import Product,Customer,Order,Coupon
from Eshop.settings import RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY
import razorpay







     
class Payment(View):

    def get(self,request):
        #print(request)
        #final_price = request.GET.get('price')
        #print(final_price)
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer_id(customer)
        client = razorpay.Client(auth=(RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY))
        final_price = request.GET.get('price')
        convert_into_paisa = int(final_price)*100
        data = { "amount": convert_into_paisa, "currency": "INR", "receipt": "order_rcptid_11" ,"payment_capture":1}
        payment = client.order.create(data)
        payment_order_id = payment['id']
        #print(payment_order_id)
        context = {'data':data,'orders':orders,'final_price':final_price,'order_id':payment_order_id,'api_key_id':RAZORPAY_API_KEY,}
        #print(context)
        return render(request,'paymentpage.html',context)

def success(request):
    customer = request.session.get('customer')
    razorpay_payment_id = request.GET.get('razorpay_payment_id')
    razorpay_order_id = request.GET.get('razorpay_order_id')
    razorpay_payment_signature = request.GET.get('razorpay_signature')
    orders = Order.get_orders_by_customer_id(customer)
    print(razorpay_payment_id,razorpay_order_id,razorpay_payment_signature)
    for order in orders:    
        order.status = True
        order.razorpay_order_id = razorpay_order_id
        order.razorpay_payment_id = razorpay_payment_id
        order.razorpay_payment_signature = razorpay_payment_signature
        order.save()
    return HttpResponse('Payment Success')
    

    
        

'''
var myVar = document.getElementById("order_total").value;
<input hiddden id="order_total" name="variable" value="{{final_price}}">
'''