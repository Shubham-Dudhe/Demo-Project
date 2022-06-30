from django.shortcuts import render,redirect
from store.models import Customer
from django.contrib.auth.hashers import make_password,check_password
from django.views import View

class Signup(View):

    def get(self,request):
        return render(request,'signup.html')

    def post(self,request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mobile_number = request.POST.get('mobile_number')
        
        value = {
            'first_name':first_name,
            'last_name':last_name,
            'email':email,
            'mobile_number':mobile_number
        }
        cust = Customer(first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            phone=mobile_number)
        
        error_message = self.validate_customer(cust)
            

        if not error_message:
            cust.password = make_password(cust.password)
            cust.register()
            return redirect('login')        
        else:
            data = {'error_message':error_message,'value':value}
            return render(request,'signup.html',data)

    def validate_customer(self,cust):
        error_message = None
        if not cust.first_name:
            error_message = 'First Name Required'
        elif len(cust.first_name) < 4:
            error_message = 'First Name Must be more than four character'
        elif not cust.last_name:
            error_message = 'First Name Required'
        elif len(cust.last_name)<4:
            error_message = 'Last Name Must be more than four character'
        elif not cust.email:
            error_message = 'Email is Required'
        elif len(cust.email)<4:
            error_message = 'Email Must be more than four character'
        elif not cust.password:
            error_message = 'Please enter your password'
        elif len(cust.password)<8:
            error_message = 'Password Must be more than eight character'
        elif not cust.phone:
            error_message = 'Mobile number is Required'
        elif len(cust.phone)<10:
            error_message = 'Mobile number Must be more than ten character'
        elif cust.isExists():
            error_message = 'Email Address already registerd'

        return error_message
