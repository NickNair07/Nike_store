from django.shortcuts import render, redirect
from admin_app.models import CategoryDB, ProductDB
from Nike_app.models import User_DB, Cart_DB, Checkout_DB
from django.contrib import messages


# Create your views here.
def index(request):
    data = CategoryDB.objects.all()
    return render(request, 'index.html', {'data': data})


def product_page(request, cat_name):
    cat_data = ProductDB.objects.filter(c_name=cat_name)
    return render(request, 'products.html', {'cat_data': cat_data})


def all_product_list(request):
    product = ProductDB.objects.all()
    new_product = set(product)
    context = {"product": new_product}
    return render(request, 'all_products.html', context)


def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')


def product_details(request, data_id):
    data = ProductDB.objects.get(id=data_id)
    return render(request, 'single_product.html', {'data': data})


def login_page(request):
    return render(request, 'user_login.html')


def reg_page(request):
    return render(request, 'user_registration.html')


def user_data(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm')
        obj = User_DB(first_name=first_name, last_name=last_name, username=username, password=password,
                      confirm_password=confirm_password)
        obj.save()
        return redirect(login_page)


def user_login(request):
    if request.method == 'POST':
        u_name = request.POST.get('username')
        p_word = request.POST.get('password')
        if User_DB.objects.filter(username=u_name, password=p_word).exists():
            request.session['username'] = u_name
            request.session['password'] = p_word
            return redirect(index)
        else:
            return redirect(login_page)
    return redirect(login_page)


def user_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(login_page)


def cart(request):
    cart_data = Cart_DB.objects.filter(username=request.session['username'])
    return render(request, 'cart.html', {"cart_data": cart_data})


def cart_data(request):
    if request.method == "POST":
        username = request.POST.get("username")
        product_name = request.POST.get("product_name")
        product_price = request.POST.get("product_price")
        product_qty = request.POST.get("product_qty")
        total_price = request.POST.get("total_price")

        obj = Cart_DB(username=username, product_name=product_name, product_price=product_price, 
                      product_qty=product_qty, total_price=total_price)
        obj.save()
        messages.success(request, "Product added to cart")
        return redirect(cart)
    

def delete_cart(request, data_id):
    data = Cart_DB.objects.filter(id=data_id)
    data.delete()
    return redirect(cart)


def checkout(request):
    return render(request, 'check_out.html')
        
        
def checkout_data(request):
    if request.method == "POST":
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        country = request.POST.get("country")
        address = request.POST.get("address")
        city = request.POST.get("city")
        district = request.POST.get("district")

        obj = Checkout_DB(first_name=first_name, last_name=last_name, mobile=mobile, email=email,
                         country=country, address=address, city=city, district=district)
        obj.save()
        return redirect(checkout)
    

def order_confirm(request):
    return render(request, 'order_confirm.html')