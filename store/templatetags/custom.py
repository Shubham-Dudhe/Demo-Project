from django import template


register = template.Library()

@register.filter(name='currency')
def currency(price):
    return "₹ "+str(price)

@register.filter(name='multiply')
def multiply(price,quantity):
    return price*quantity