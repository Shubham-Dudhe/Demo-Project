from django.shortcuts import render,redirect
from django.views import View
from store.models import Product

class Cart(View):
    
    def get(self,request):
        cart = request.session.get('cart')
        if cart:
            product_list = list(request.session.get('cart').keys())
            products = Product.get_product_by_id(product_list)
            print(products)
            return render(request,'cart.html',{'products':products})
        else:
            request.session['cart'] = {}
            return render(request, 'emptycart.html')
    
