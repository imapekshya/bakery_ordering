from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.views import View
from .models import Branch, Customer, Product, Payment, Cart, OrderPlaced
from.forms import CustomerRegistrationForm, CustomerProfileForm
# Create your views here.

# def home(request):
# return render(request,'app/home.html')


class ProductView(View):
    def get(self, request):
        search_query = ''
        cakes = Product.objects.filter(category='C')
        if(request.GET.get('search_query')):
            search_query = request.GET.get('search_query')
            cakes = Product.objects.filter(
                title__icontains=search_query)
        totalitem = 0

        cookies = Product.objects.filter(
            title__icontains=search_query, category='CK')
        breads = Product.objects.filter(
            title__icontains=search_query, category='B')
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request, 'app/home.html',
                      {'cakes': cakes, 'breads': breads, 'cookies': cookies, 'totalitem': totalitem})


# def cake(request, info=None):
#     if info == None:
#         cakes = Product.objects.filter(category='C')
#     elif info == 'Black Forest' or info == 'Choco Vanilla':
#         cakes = Product.objects.filter(category='C').filter(flavour=info)

    # return render(request, 'app/cake.html', {'cakes': cakes})


def cake(request):
    return render(request, 'app/cake.html')


def buy_now(request):
    return render(request, 'app/buynow.html')


def product_detail(request):
    return render(request, 'app/productdetail.html')


class ProductDetailView(View):
    def get(self, request, pk):
        totalitem = 0
        product = Product.objects.get(pk=pk)
        item_already_in_cart = False
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            item_already_in_cart = Cart.objects.filter(
                Q(product=product.id) & Q(user=request.user)).exists()

        return render(request, 'app/productdetail.html', {'product': product, 'item_already_in_cart': item_already_in_cart, 'totalitem': totalitem})


@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('/cart')


@login_required
def show_cart(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        user = request.user
        cart = Cart.objects.filter(user=user)
        print(cart)
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        # print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
                totalamount = amount + shipping_amount

            return render(request, 'app/addtocart.html', {'carts': cart, 'totalamount': totalamount, 'amount': amount})

        else:
            return render(request, 'app/emptycart.html', {'totalitem': totalitem})


def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        print(prod_id)
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user ==
                        request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': amount + shipping_amount
        }

        return JsonResponse(data)


def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        print(prod_id)
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user ==
                        request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': amount + shipping_amount
        }

        return JsonResponse(data)


def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        print(prod_id)
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user ==
                        request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        data = {
            'amount': amount,
            'totalamount': amount + shipping_amount
        }

        return JsonResponse(data)


def profile(request):
    return render(request, 'app/profile.html')


@login_required
def orders(request):
    op = OrderPlaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html', {'order_placed': op})


@login_required
def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html', {'add': add, 'active': 'btn-primary'})


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(
                request, 'Congratulations!! Registered Successfully')
            form.save()
        return render(request, 'app/customerregistration.html', {'form': form})


@login_required
def checkout(request):
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 70.0
    totalamount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
        totalamount = amount + shipping_amount

    return render(request, 'app/checkout.html', {'add': add, 'totalamount': totalamount, 'cart_items': cart_items})


@login_required
def payment_done(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user, customer=customer,
                    product=c.product, quantity=c.quantity).save()
        c.delete()
    return redirect("orders")


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', {'form': form, 'active': 'btn-primary'})

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            reg = Customer(user=usr, name=name, address=address,
                           phone=phone, email=email)
            reg.save()
            messages.success(
                request, 'Congratulations!! Profile Updated Successfully')
        return render(request, 'app/profile.html', {'form': form, 'active': 'btn-primary'})
