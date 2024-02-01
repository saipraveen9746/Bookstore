from django.urls import path

from . import views
from .views import productlist, detailsss, SearchResultsView, BookCheckOut,cart,remove_from_cart,Comics

urlpatterns = [
    path('', productlist.as_view(), name='list'),
    path('deta/<int:pk>', detailsss.as_view(), name='deta'),
    path('search/',SearchResultsView.as_view(),name='search'),
    path('checkout/<int:pk>', BookCheckOut.as_view(), name='checkout'),
    path('cart/',cart,name ='mycart'),
    path('add_to_cart/<int:book_id>/',views.add_to_cart,name = 'add_to_cart'),
    path('remove_from_cart/<int:book_id>/',views.remove_from_cart,name = 'remove_from_cart'),
    path('comics/',views.Comics,name='comics'),
    path('malayalam/',views.Malayalam,name='malluwood')



]
