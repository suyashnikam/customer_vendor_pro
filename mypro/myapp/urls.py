from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
   path('', views.home,name="home"),
   path('contact', views.contact,name="contact"),
   path('aboutUs', views.aboutUs,name="aboutUs"),
   path('register', views.register,name="register"),
   path('showvendors', views.showvendors,name="showvendors"),
   path('signin', views.signin,name="signin"),
   path('signout', views.signout,name="signout"),
   path('forget-password/' , views.ForgetPassword , name="forget_password"),
   path('change-password/<token>/' , views.ChangePassword , name="change_password"),
   path('searchvendor',views.searchvendor, name='searchvendor'),
   path('add_show', views.saveCustomer,name="add_show"),
   path('savecustomer/', views.saveCustomer,name="savecustomer"),
   path('showcustomers', views.showcustomers,name="showcustomers"),
   path('searchcustomer',views.searchcustomer, name='searchcustomer'),
   path('customerdetails/<int:id>/',views.customerdetails, name='customerdetails'),
   path('update/<int:id>/', views.FinalUpdateCustomer, name="updatedata"),
   path('askdelete/<int:id>/',views.askdelete, name='askdelete'),
   path('delete/<int:id>/', views.delete_customer, name="deletedata"),
   path('changepass/',views.user_change_pass, name='changepass'),
   path('vendordetails/<int:id>/',views.vendordetails, name='vendordetails'),
   path('updateuser/<int:id>/', views.FinalUpdateVendor, name="updatevendors"),
   path('updateuser/<int:id>/FinalUpdateVendor', views.FinalUpdateVendor, name="FinalUpdateVendor"),
   path('askdeletevendor/<int:id>/',views.askdeletevendor, name='askdeletevendor'),
   path('deleteuser/<int:id>/', views.delete_vendor, name="deletevendor"),

]