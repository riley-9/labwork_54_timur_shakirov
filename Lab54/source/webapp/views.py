from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category


def index_view(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'index.html', context)


def product_create_view(request):
    if request.method == 'GET':
        context = {'categories': Category.objects.all()}
        return render(request, 'product_create.html', context)
    elif request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        category = request.POST.get('category')
        category_ = Category.objects.get(name=category)
        price = request.POST.get('price')

        product = Product.objects.create(name=name, description=description, category=category_,
                                         price=price)

        return redirect('product_detail', pk=product.pk)


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'product_detail.html', context)


def product_update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    category = Category.objects.get(name=product.category.name)
    if request.method == 'GET':

        return render(request, 'product_update.html', {'product': product, 'categories': Category.objects.all(),
                                                       'name':product.name, 'description':product.description,
                                                       'price':product.price, 'category':category})
    elif request.method == 'POST':
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        category = request.POST.get('category')
        category_ = Category.objects.get(name=category)
        product.category = category_
        product.price = request.POST.get('price')
        product.save()
        return redirect('product_detail', pk=product.pk)


def product_delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        return render(request, 'product_delete.html', {'product': product})
    elif request.method == 'POST':
        product.delete()
        return redirect('index')


def category_list_view(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'index.html', context)

def category_create(request):
    if request.method == 'GET':
        return render(request, 'category_new')
    category = Category.objects.create(name=request.POST.get('name'), description=request.POST.get('description'))
    category.save()
    return redirect('category_list')

def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'GET':
        return render(request, 'category_form')\


