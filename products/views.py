from django.shortcuts import render, redirect
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', index_context(products))


def index_context(products):
    for product in products:
        product.created_at = product.created_at.strftime('%Y-%m-%d %H:%M:%S')
        product.updated_at = product.updated_at.strftime('%Y-%m-%d %H:%M:%S')
    return {'products': products}


def edit(request, product_id):
    msg = ''
    if request.method == 'POST':
        edit_product(request.POST, product_id)
        msg = 'Product is successfully edited.'
        return redirect('/products', {})
    return render(request, 'products/edit.html', edit_context(product_id))


def edit_context(product_id, msg=''):
    return {'product': Product.objects.filter(id=product_id)[0], 'msg': msg}


def edit_product(params, product_id):
    Product.objects.filter(id=product_id).update(
        name=params['name'],
        comment=params['comment'])


def new(request):
    if request.method == 'GET':
        return render(request, 'products/new.html')
    elif request.method == 'POST':
        params = request.POST
        product = Product(name=params['name'], comment=params['comment'])
        product.save()
        return redirect('/products')
