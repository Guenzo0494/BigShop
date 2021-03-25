from django import template

from carts.models import Order

register = template.Library()

@register.filter(name="cart_total")
def cart_total(user):
    order = Order.objects.filter(user=user, ordered=False)

    if order.exists():
        nmb = 0
        for item in order[0].orderitems.all():
            nmb += item.quantity
        return nmb
    else:
    	return 0
 
