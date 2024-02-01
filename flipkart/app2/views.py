from _decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from .models import Bookstoredb, Cart, Cartitems


# Create your views here.




class productlist(ListView):
    model = Bookstoredb
    template_name = 'productlist.html'


class detailsss(DetailView):
    model = Bookstoredb
    context_object_name = 'list'
    template_name = "detailview.html"


class SearchResultsView(ListView):
    model = Bookstoredb
    template_name = 'searchview.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Bookstoredb.objects.filter(
            Q(Book_name=query) | Q(Author=query)
        )


class BookCheckOut(DetailView):
    model = Bookstoredb
    template_name = 'checkout.html'


@login_required
def cart(request):
    cart_qs = Cart.objects.filter(user=request.user)
    if cart_qs.exists():
        cart_obj = cart_qs.first()
        cart_items = Cartitems.objects.filter(cart=cart_obj)
    else:
        cart_obj = None
        cart_items = []
    context = {

        'cart': cart_obj,
        'cart_items': cart_items
    }
    return render(request, 'cart/mycart.html', context)


@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Bookstoredb, id=book_id)
    cart_qs = Cart.objects.filter(user=request.user)
    if cart_qs.exists():
        cart_obj = cart_qs.first()
    else:
        cart_obj = Cart.objects.create(user=request.user, total_price=Decimal('0.00'))
    cart_item, created = Cartitems.objects.get_or_create(book=book, cart=cart_obj)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    cart_obj.total_price += Decimal(str(book.Price))
    cart_obj.save()
    return redirect('mycart')

def remove_from_cart(request,book_id):
    book = get_object_or_404(Bookstoredb, id=book_id)
    cart_qs = Cart.objects.filter(user=request.user)
    if cart_qs.exists():
        cart_obj = cart_qs.first()
        cart_item_qs = Cartitems.objects.filter(book=book,cart=cart_obj)
        if cart_item_qs.exists():
            cart_item = cart_item_qs.first()
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete()
            cart_obj.total_price -= Decimal(str(book.Price))
            cart_obj.save()
        return redirect('mycart')

def Comics(request):
    comics = Bookstoredb.objects.filter(Type="Comics")
    return render(request,'comics.html',{"comics":comics})

def Malayalam(request):
    malayalam = Bookstoredb.objects.filter(Language="Malayalam")
    return render(request,'malayalam.html',{'malluwood':malayalam})


