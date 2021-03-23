from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q

from products.models import Product, Category
from carts.models import Cart, Order

# Create your views here.

def prod_by_category_view(request):
    template_name = 'products/home.html'
    
    key_word = request.GET.get('key_word')
    if key_word:
        result = Product.objects.filter(Q(name__icontains = key_word) | Q(detail_text__icontains = key_word))
        
        if result.exists():
            context = {'search_find': result}            
        else:
            info = "Aucun produit ne corespond a ce mot"
                
            allProd = Product.objects.all()
            allCat = Category.objects.all()
            tabProdCat = []

            for cat in allCat:
                tabProd = []
                i = 0
                for prod in allProd:
                    if cat.id == prod.category.id:
                        tabProd.append(prod)
                        i += 1
                
                if i != 0:
                    tabProdCat.append([tabProd, cat])
                    
            context = {'tab_prod_cat': tabProdCat, 'allCat': allCat, 'info': info}
    else:
            allProd = Product.objects.all()
            allCat = Category.objects.all()
            tabProdCat = []

            for cat in allCat:
                tabProd = []
                i = 0
                for prod in allProd:
                    if cat.id == prod.category.id:
                        tabProd.append(prod)
                        i += 1
                
                if i != 0:
                    tabProdCat.append([tabProd, cat])
                    
            context = {'tab_prod_cat': tabProdCat, 'allCat': allCat}
        
    return render(request, template_name, context)



def all_prod_of_category_view(request, id):
    template_name = 'products/allCatProd.html'
    prods = Product.objects.filter(category=id)
    paginator = Paginator(prods, 6) # 12 produits par page et paginator contient les pages
    page_number = request.GET.get('page') # on recupere le numero de la page
    page_obj = paginator.get_page(page_number) # on recupere les objets de la page
    
    cat = Category.objects.get(id=id)
    
    context = {'cat': cat, 'page_obj': page_obj}
    return render(request, template_name, context)
    
        
            
    
    
@login_required(login_url= 'account_login')
def product_detail(request, slug):
    prod = Product.objects.get(slug=slug)
     
    if request.method == 'POST': # ajoute si user is_authenticated
        qte = request.POST['qte']
        
        
        item = get_object_or_404(Product, slug=slug)
        order_item, created = Cart.objects.get_or_create(item=item, user=request.user)
        order_qs = Order.objects.filter(user=request.user, ordered=False)
        if order_qs.exists():
            order = order_qs[0]
            # check if the order item is in the order
            if order.orderitems.filter(item__slug=item.slug).exists():
                order_item.quantity += int(qte)
                order_item.save()
                messages.info(request, "This item quantity was updated.")
                return redirect("mainapp:cart-home")
            else:
                order_item.quantity += int(qte) - 1
                order_item.save()
                order.orderitems.add(order_item)
                messages.info(request, "This item was added to your cart.")
                return redirect("mainapp:cart-home")
        else:
            order_item.quantity += int(qte) - 1
            order_item.save()
            order = Order.objects.create(user=request.user)
            order.orderitems.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("mainapp:cart-home")

        
        
        
        return render(request, 'products/detail.html', context={'product': prod, 'item_qte': qte})
    else: # ajoute si user not authenticated
        return render(request, 'products/detail.html', context={'product': prod})
    
    
    
