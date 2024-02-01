from django.urls import path
from . import views
from .views import SignUpPage


urlpatterns =[
    path('signup/',SignUpPage.as_view(),name='signup')
    ]


