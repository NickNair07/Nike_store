from django.shortcuts import render, redirect
from admin_app.models import CategoryDB, ProductDB
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib import messages


# Create your views here.
def admin_page(request):
    return render(request, 'admin_page.html')


def add_category(request):
    return render(request, 'add_category.html')


def category_data(request):
    if request.method == 'POST':
        c_name = request.POST.get('c_name')
        c_image = request.FILES['c_image']
        c_description = request.POST.get('c_description')
        obj = CategoryDB(name=c_name, image=c_image, description=c_description)
        obj.save()
        messages.success(request, 'Category added Successfully')
        return redirect(add_category)


def display_category(request):
    data = CategoryDB.objects.all()
    return render(request, 'display_category.html', {'data': data})


def edit_category(request, data_id):
    data = CategoryDB.objects.get(id=data_id)
    return render(request, 'edit_category.html', {'data': data})


def update_category(request, data_id):
    if request.method == 'POST':
        c_name = request.POST.get('c_name')
        c_description = request.POST.get('c_description')
        try:
            c_image = request.FILES['c_image']
            fs = FileSystemStorage()
            file = fs.save(c_image.name, c_image)
        except MultiValueDictKeyError:
            file = CategoryDB.objects.get(id=data_id).image
        CategoryDB.objects.filter(id=data_id).update(name=c_name, description=c_description, image=file)
        messages.success(request, 'Category updated Successfully')
        return redirect(display_category)


def delete_category(request, data_id):
    data = CategoryDB.objects.filter(id=data_id)
    data.delete()
    messages.error(request, 'Category deleted Successfully')
    return redirect(display_category)


def add_product(request):
    data = CategoryDB.objects.all()
    return render(request, 'add_product.html', {'data': data})


def product_data(request):
    if request.method == 'POST':
        c_name = request.POST.get('c_name')
        p_name = request.POST.get('p_name')
        p_qty = request.POST.get('p_qty')
        p_price = request.POST.get('p_price')
        description = request.POST.get('p_description')
        p_image = request.FILES['p_image']

        obj = ProductDB(c_name=c_name, p_name=p_name, p_qty=p_qty, p_price=p_price, description=description,
                        p_image=p_image)
        obj.save()
        messages.success(request, 'Product added Successfully')
        return redirect(add_product)


def display_product(request):
    data = ProductDB.objects.all()
    return render(request, 'display_product.html', {'data': data})


def edit_product(request, data_id):
    data = CategoryDB.objects.all()
    p_data = ProductDB.objects.get(id=data_id)
    return render(request, 'edit_product.html', {'data': data, 'p_data': p_data})


def update_product(request, data_id):
    if request.method == 'POST':
        c_name = request.POST.get('c_name')
        p_name = request.POST.get('p_name')
        p_qty = request.POST.get('p_qty')
        p_price = request.POST.get('p_price')
        description = request.POST.get('p_description')
        try:
            p_image = request.FILES['p_image']
            fs = FileSystemStorage()
            file = fs.save(p_image.name, p_image)
        except MultiValueDictKeyError:
            file = ProductDB.objects.get(id=data_id).p_image
        ProductDB.objects.filter(id=data_id).update(c_name=c_name, p_name=p_name, p_qty=p_qty, p_price=p_price,
                                                    description=description, p_image=file)
        messages.success(request, 'Product updated Successfully')
        return redirect(display_product)


def delete_product(request, data_id):
    data = ProductDB.objects.filter(id=data_id)
    data.delete()
    messages.error(request, 'Product Deleted Successfully')
    return redirect(display_product)


