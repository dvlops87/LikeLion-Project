from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import User, Product, OrderList
from django.contrib import auth
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    product = Product.objects.all()
    paginator = Paginator(product, 3)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'home.html', {'products':page})

def user_signup(request):
    if request.method == "POST" :
        user = User.objects.create_user(
            username = request.POST["username"],
            password = request.POST["password"],
            university = request.POST["university"],
            userImage = request.FILES["userImage"]
        )
        user.save()
        auth.login(request, user)
        return redirect('home')
    else : 
        return render(request,'signup.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username = username, password = password)
        
        if user is not  None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': '아이디와 비밀번호가 일치하지 않습니다.'})
    else:
        return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

def user_list(request):
    userList = User.objects.all()
    return render(request, 'userList.html', {'userList':userList})

def detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'detail.html', {'product':product})

def order(request, id, user_id):
    product = get_object_or_404(Product, pk=id)
    new_order = OrderList()
    user = User.objects.get(id = user_id)
    new_order.orderUser = user
    new_order.productOrder = product
    new_order.save() 
    return render(request, 'orderFinish.html', {'new_order':new_order})

def order_list(request, user_id) : 
    o_list = OrderList.objects.all()
    p_list = Product.objects.all()

    o_list = o_list.filter(orderUser = user_id)

    result = []
    total = 0
    for i in o_list : 
        for j in p_list : 
            if str(i) == str(j) : 
                total += int(j.productPrice)
                result.append(j)
                
    return render(request, 'orderList.html', {'result':result, 'total':total})

def new(request):
    if request.method == 'POST' :
        new_Product = Product()
        new_Product.productName = request.POST['productName']
        new_Product.productDetail = request.POST['productDetail']
        new_Product.productImage = request.FILES['productImage']
        new_Product.productPrice = request.POST['productPrice']
        new_Product.save()
        return redirect('home')
    else:  
        return render(request, 'new.html')


def delete(request, id):
    delete_Product = Product.objects.get(id = id)
    delete_Product.delete()
    return redirect('home')    

def update(request, id):
    if request.method == "POST" : 
        update_product = Product.objects.get(id = id)
        update_product.productName = request.POST['productName']
        update_product.productDetail = request.POST['productDetail']
        update_product.productImage = request.FILES['productImage']
        update_product.productPrice = request.POST['productPrice']
        update_product.save()
        return redirect('detail', update_product.id)
    else : 
        product = Product.objects.get(id = id )
        return render(request, 'update.html', {'product' : product})