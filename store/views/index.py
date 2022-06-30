from django.shortcuts import render,redirect
from store.models import Product
from store.models import Category
from store.models import Customer
from django.views import View

# Create your views here.

#print(make_password('12345678'))
#print(check_password('12345678','pbkdf2_sha256$320000$qF5LM26S0cepZRdkmdHvdg$OQuJfZn5TJHcNdBVromW9GFCUpo0+JJTo1cOaVYtXnQ='))
class Index(View):

    def get(self,request):

        cart = request.session.get('cart')
        
        if not cart:
            request.session.cart = {}

        products = Product.get_all_product()
        categories = Category.get_categories()
        category = request.GET.get('category')
        if category:
            products = Category.get_categories_by_Id(category)
        else:
            products = Product.get_all_product()
        data = {'products':products,'categories':categories}
        print('you are:',request.session.get('customer_email'))
        return render(request,'order.html',data)

    def post(self,request):

        #print(request.session)   
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        print(type(remove))
        cart = request.session.get('cart')
        #print('product',product,'cart',cart)

        if cart:
            #print('inside if')
            quantity = cart.get(product)
            #print('quantity',quantity) 
            if quantity:
                if remove:
                    if quantity==1:
                        cart.pop(product)
                    else:    
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1

        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect('index')

    
    
