from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("productview/<int:id>", views.productView, name="ProductView"),
    path("productviewLaptop/<int:id>", views.productViewLaptop, name="ProductViewLaptop"),
    path("productviewAccessories/<int:id>", views.productViewAccessories, name="ProductViewAccessories"),
    path("checkout/", views.checkout, name="Checkout"),
]