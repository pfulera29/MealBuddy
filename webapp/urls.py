from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('orderplaced/',views.orderplaced),
    path('canteen/',views.restuarent,name='restuarant'),
    path('register/user/',views.customerRegister,name='register'),
    path('login/user/',views.customerLogin,name='login'),
    path('login/canteen/',views.restLogin,name='rlogin'),
    path('register/canteen/',views.restRegister,name='rregister'),
    path('profile/canteen/',views.restaurantProfile,name='rprofile'),
    path('profile/user/',views.customerProfile,name='profile'),
    path('user/create/',views.createCustomer,name='ccreate'),
    path('user/update/<int:id>/',views.updateCustomer,name='cupdate'),
    path('canteen/create/',views.createRestaurant,name='rcreate'),
    path('canteen/update/<int:id>/',views.updateRestaurant,name='rupdate'),
    path('canteen/orderlist/',views.orderlist,name='orderlist'),
    path('canteen/menu/',views.menuManipulation,name='mmenu'),
    path('logout/',views.Logout,name='logout'),
    path('canteen/<int:pk>/',views.restuarantMenu,name='menu'),
    path('checkout/',views.checkout,name='checkout'),

]