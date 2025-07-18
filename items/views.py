from django.shortcuts import render ,redirect,get_object_or_404
from .models import Item ,ItemImage ,CartItem
from .form import ItemForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

def home(request):
    item_list = Item.objects.all().order_by('-id')  # Latest first
    paginator = Paginator(item_list, 6)  # 6 items per page
    page_number = request.GET.get('page')
    items = paginator.get_page(page_number)
    
    return render(request, 'home.html', {'items': items})

@login_required
def sellItem(request):
    if request.method =='POST':
        form = ItemForm(request.POST)
        images = request.FILES.getlist('images') 

        if form.is_valid():
            item = form.save(commit=False)
            item.seller = request.user
            item.save()

            for image in images:
                ItemImage.objects.create(item=item, image=image)
            
            return redirect('home')

    else:
        form = ItemForm(request.POST)

    return render(request , 'sellItem.html' , {'form':form})

def viewItem(request ,item_id):
    item = Item.objects.get(pk=item_id)
    return render(request , 'viewItem.html' , {'item':item})


def cart_view(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Optional check

    cart_items = CartItem.objects.filter(user=request.user)

    total_price = sum(item.item.price * item.quantity for item in cart_items)

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })


@login_required
def add_to_cart(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        item=item
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()
        messages.info(request, f"{item.name} quantity increased in your cart.")
    else:
        messages.success(request, f"{item.name} added to your cart!")

    return render(request , 'viewItem.html' ,{'item':item})
