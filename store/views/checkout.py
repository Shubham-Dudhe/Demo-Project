from django.shortcuts import render,redirect
from django.views import View
from store.models import Product,Customer,Order,Address



class Checkout(View):

    return_url = None

    def post(self,request):
        house_no = request.POST.get('house_no')
        street_name = request.POST.get('street_name')
        area = request.POST.get('area')
        town = request.POST.get('town')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        mobile_number = request.POST.get('mobile_number')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_product_by_id(list(cart.keys()))
        #print(address,phone,customer,cart,products)
        address = Address( customer=Customer(id=customer),
                           house_no=house_no,
                           street_name=street_name,
                           area=area,
                           town=town,
                           city=city,
                           state=state,
                           pincode=pincode)
        address.save()

        for product in products:
            
            order = Order(product=product,
                          customer=Customer(id=customer),
                          quantity=cart.get(str(product.id)),
                          price=product.price,
                          mobile_number=mobile_number,
                          address=Address(id=address.id))
               
            order.place_order()
        request.session['cart'] = {}
        return redirect('orders')

'''
def get(self,request):
        Checkout.return_url = request.GET.get('return_url')
        product_list = list(request.session.get('cart').keys())
        products = Product.get_product_by_id(product_list)
        #print(products)
        return render(request,'cart.html',{'products':products})
'''