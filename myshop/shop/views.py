from django.shortcuts import render, get_object_or_404
from .models import Category, SubCategory, Align, Product
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    subcategory = None
    align = None
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    alignto = Align.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug :
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {'category': category, 'subcategory' : subcategory, 'align' : align,
                                                  'categories': categories, 'subcategories' : subcategories, 'alignto' : alignto,
                                                  'products': products })

def product_detail(request, id, slug):
    categories = Category.objects.all()
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'categories':categories,'product': product,'cart_product_form': cart_product_form})