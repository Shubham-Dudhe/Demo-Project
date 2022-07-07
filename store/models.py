from django.db import models
import datetime

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    @staticmethod
    def get_categories():
        return Category.objects.all()

    @staticmethod
    def get_categories_by_Id(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_product()

    def __str__(self):
        return f"{self.name}"



class Product(models.Model):

    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description = models.CharField(max_length=200,default='',null=True,blank=True)
    image = models.ImageField(upload_to='Uploads/products/')

    def __str__(self):
        return f"{self.name}"

    @staticmethod
    def get_all_product():
        return Product.objects.all()

    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in=ids)

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def register(self):
        self.save()

    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True
        return False


class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    house_no = models.IntegerField()
    street_name = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.pincode}"

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()    
    mobile_number = models.CharField(max_length=50,blank=True, null=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    razorpay_order_id = models.CharField(max_length=500,null=True,blank=True)
    cash_on_delivery = models.CharField(max_length=500,null=True,blank=True)
    

    def place_order(self):
        return self.save()

    @staticmethod
    def get_orders_by_customer_id(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')


class Coupon(models.Model):
    coupon_code = models.CharField(max_length=50)
    is_expired = models.BooleanField(default=False)
    is_applied = models.BooleanField(default=False)
    discount_price = models.IntegerField(default=100)
    minimum_amount = models.IntegerField(default=500)

    def __str__(self):
        return f"{self.coupon_code}"


    @staticmethod
    def modify_order_total(coupon,orders):
        sum = 0
        for order in orders:
            sum += order.price*order.quantity
        final_price = sum - coupon
        return final_price
