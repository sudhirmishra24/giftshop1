from django.shortcuts import render,redirect
from django.http import Http404
from django.contrib import messages
from .models import customer,Product,Cart
# Create your views here.
def index(request):
    username=request.session.get('username')
    try:
        if username is not None:
            return render(request,'index.html',{'username': username})
        else:
            return render(request,'login.html')
    except Exception:
        messages.error("some error occured.")
        return redirect(login)
def contact(request):
    return render(request, 'contact.html')

def shop(request):
    username=request.session.get('username')
    try:
        if username is not None:
            products=Product.objects.all()
            return render(request,'shop.html',{'products':products,'username':username})
        else:
            return render(request,'login.html')
    except Exception:        
        return redirect(login)
        

def testimonial(request):
    username=request.session.get('username')
    try:
        if username is not None:
            return render(request,'testimonial.html',{'username': username})
        else:
            return render(request,'login.html')
    except Exception:
        messages.error("some error occured.")
        return redirect(login)
def login(request):
    request.session.flush()
    if request.method=="POST":
        username= request.POST.get('username')
        password= request.POST.get('password')
        try:
            user=customer.objects.get(username=username,password=password)
            request.session['username']=username
            request.session['id']= user.id
            return redirect ('index')
        except Exception:
            messages.error(request, 'Username and Password not register')
            return render(request, 'login.html', {'messages': messages.get_messages(request)})
        
    else:
        return render(request, 'login.html')

def logout(request):
    username=request.session.get('username')
    if username:
        request.session.flush()
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login') 

def registration(request):
    if request.method == 'POST':
        cname = request.POST.get('cname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        cadd = request.POST.get('cadd')
        username = request.POST.get('username')
        password = request.POST.get('password')
        images = request.FILES.get('images')    
        user = customer( cname=cname,email=email,phone=phone,cadd=cadd,username=username,password=password,images=images )
        user.save()
        return redirect('/login') 

    return render(request, 'registration.html') 
def upload_image(request):
    # username=request.session.get('username')
    
    if request.method=='POST':
        image_upload=customer()
        image_upload.images=request.FILES['images']
        
        image_upload.save()
        return redirect("/upload_image")

    images=customer.objects.all()
    return render(request,'upload.html',{'images':images})


# View to add products to cart
def add_to_cart(request,pk):
    username = request.session.get('username')
    if username is None:
        return redirect('login')
    try:
        user = customer.objects.get(username=username)
        product = Product.objects.get(id=pk)
        cart_items,created = Cart.objects.get_or_create(customer=user, product=product)
        if not created:
            cart_items.quantity += 1  
            cart_items.save()
        
        messages.success(request, f"{product.name} has been added to your cart.")
        return redirect('shop')  # Redirect to shop or cart page    
    except Product.DoesNotExist:
        messages.error(request, "Product not found.")
        return redirect('shop')
# View to show cart items
def view_cart(request):
    username = request.session.get('username')
    if username is None:
        return redirect('login')
    try:
        user = customer.objects.get(username=username)
        cart_items = Cart.objects.filter(customer=user)
        total_price = sum(item.product.price * item.quantity for item in cart_items)        
        return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price, 'username': username})
    except customer.DoesNotExist:
        messages.error(request, "User not found.")
        return redirect('login')
# View to remove product from cart
def remove_from_cart(request, cart_item_id):
    try:
        cart_item = Cart.objects.get(id=cart_item_id)
        cart_item.delete()
        messages.success(request, "Item removed from your cart.")
        return redirect('view_cart')
    except Cart.DoesNotExist:
        messages.error(request, "Item not found in your cart.")
        return redirect('view_cart')


       
