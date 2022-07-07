from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from store.models import Product,Customer,Order,Coupon
from Eshop.settings import RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY
import razorpay
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

class Payment(View):

    def get(self,request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer_id(customer)
        client = razorpay.Client(auth=(RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY))
        final_price = request.GET.get('price')
        convert_into_paisa = int(final_price)*100
        if convert_into_paisa>1:
            data = { "amount": convert_into_paisa, "currency": "INR", "receipt": "order_rcptid_11" ,"payment_capture":1}
            payment = client.order.create(data)
            payment_order_id = payment['id']
            context = {'data':data,'orders':orders,'final_price':final_price,'order_id':payment_order_id,'api_key_id':RAZORPAY_API_KEY,}
            return render(request,'paymentpage.html',context)
        else:
            return redirect('index')

        
    def post(self,request):
        customer = request.session.get('customer')
        cash_on_delivery = request.GET.get('COD')
        orders = Order.get_orders_by_customer_id(customer).filter(status=False)
        for order in orders:    
            order.status = True
            order.cash_on_delivery = True
            order.save()
        request.session['cart'] = {}
        subject = 'Subject'
        html_message = render_to_string('emailtemplate.html', {'orders': orders})
        plain_message = strip_tags(html_message)
        from_email = 'djangopython1947@gmail.com'
        to = 'shubhamdudhe95@gmail.com'
        send_mail(
            'Testing Mail',
            plain_message,
            from_email,
            [to],
            fail_silently=False,)
        return redirect('proccess_orders')


def success(request):
    customer = request.session.get('customer')
    razorpay_order_id = request.GET.get('razorpay_order_id')
    orders = Order.get_orders_by_customer_id(customer).filter(status=False)
    for order in orders:    
        order.status = True
        order.razorpay_order_id = razorpay_order_id
        order.save()
    request.session['cart'] = {}
    subject = 'Subject'
    html_message = render_to_string('emailtemplate.html', {'orders': orders})
    plain_message = strip_tags(html_message)
    from_email = 'djangopython1947@gmail.com'
    to = 'iamshubh007@gmail.com'
    send_mail(
        'Testing Mail',
        plain_message,
        from_email,
        [to],
        fail_silently=False,)
    return redirect('proccess_orders')

'''
def check(request):
    customer = request.session.get('customer')
    razorpay_order_id = request.GET.get('razorpay_order_id')
    orders = Order.get_orders_by_customer_id(customer).filter(status=True)
    template_name = 'emailtemplate.html'
    context = {}
    return render(request,template_name,{'orders': orders})
'''