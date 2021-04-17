from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product, Category
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    """ Widok odpowiedzialny za dodawanie produktów do koszyka """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    """ Widok pozwalający na usunięcie produktu z koszyka """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    """ Widok koszyka """
    cart = Cart(request)

    category = Category.objects.all()
    if request.POST:
        xx = request.POST
        zz = dict(xx.lists())
        my_list = []
        for key, value in zz.items():
            my_list.append(value)
        products = Product.objects.filter(name=my_list[0][0])
        return render(request, '../../shop/templates/shop/search/search.html',
                      {'products': products, 'category': category})

    return render(request, 'cart/detail.html', {'cart': cart, 'category': category})
