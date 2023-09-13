from django.urls import path
from . import views

urlpatterns = [
    path('',views.store, name='store'),
    path('cart/',views.cart, name='cart'),
    path('checkout/',views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('about_us/',views.aboutUs, name='about_us'),
    path('faq/',views.FAQ, name='faq'),
    path('contact_us/',views.contactUs, name='contact_us'),
]

