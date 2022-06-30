from django.shortcuts import render,redirect,HttpResponseRedirect
from store.models import Customer
from django.contrib.auth.hashers import make_password,check_password
from django.views import View

class Login(View):

    return_url = None

    def get(self,request):
        Login.return_url = request.GET.get('return_url')
        return render(request,'login.html')

    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        error_message = None
        try:
            customer = Customer.objects.get(email=email)
        except:
            error_message = 'Customer is not registered'
        else:
            if customer:
                flag = check_password(password,customer.password)
                if flag:
                    request.session['customer'] = customer.id
                    #request.session['customer_email'] = customer.email
                    if Login.return_url:
                        return HttpResponseRedirect(Login.return_url)
                    else:
                        Login.return_url = None
                        return redirect('index') 
                else:
                    error_message = 'Email or password is incorrect'
            else:
                error_message = 'Email or password is incorrect'
            
        return render(request,'login.html',{'error_message':error_message})


def logout(request):
    request.session.clear()
    return redirect('login')