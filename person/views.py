from django.shortcuts import render, redirect
from .models import Customer, Order, Product, Tag
from .forms import OrderForm, CreateUserForm
from .filters import OrderFilter
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def registerPage(request):
    if request.user.is_authenticated:    
        return render(request, 'person/registration.html')
    else:
        form=CreateUserForm()
        if request.method=="POST":
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request, 'Account was created for'+ user)
                return redirect('login')
        context={'form':form}
        return render(request, 'person/registration.html', context)



def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Username or Password is incorrect')
                
        return render(request, 'person/login.html')


def logoutPage(request):
    logout(request)
    return redirect('login') 


def dashboard(request):
    orders=Order.objects.all()
    customer=Customer.objects.all()
    total_customer=customer.count()
    total_orders=orders.count()
    delivered=orders.filter(status="Delivered").count()
    pending=orders.filter(status="Pending").count()
    context={'orders':orders, 'customer':customer, 'total_customer':total_customer, 'total_orders':total_orders,'delivered': delivered, 'pending': pending}

    return render(request, 'person/dashboard.html', context)

def pro(request): #pro stands for product
    product=Product.objects.all()
    context={'product':product}
    return render(request, "person/product.html", context)


def createorder(request):
    form=OrderForm()
    if request.method=="POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form': form}
    return render(request, 'person/order_form.html', context)

#Update the order
def updateorder(request, pk):
    order=Order.objects.get(id=pk)
    form=OrderForm(instance=order)

    if request.method=="POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form': form}
    return render(request, 'person/order_form.html', context) 

def deleteorder(request,pk):
    order=Order.objects.get(id=pk)
    if request.method=="POST":
        order.delete()
        return redirect('/')
    context={'item':order}
    return render(request, 'person/delete.html',context)

def cus(request, pk_test): #cus stands for customer
    customer=Customer.objects.get(id=pk_test)
    orders=customer.order_set.all()
    order_count=orders.count()
    myFilter=OrderFilter(request.GET, queryset=orders)
    orders=myFilter.qs
    context={'customer':customer, 'orders':orders, 'order_count': order_count, 'myFilter': myFilter}
    return render(request,'person/customer.html', context)


