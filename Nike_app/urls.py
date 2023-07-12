from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product_page/<cat_name>/', views.product_page, name='product_page'),
    path('single_product/<int:data_id>/', views.product_details, name='single_product'),
    path('all_product_list/', views.all_product_list, name='all_product_list'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('login_page', views.login_page, name='login_page'),
    path('reg_page', views.reg_page, name='reg_page'),
    path('user_data', views.user_data, name='user_data'),
    path('user_login', views.user_login, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('cart', views.cart, name='cart'),
    path('cart_data', views.cart_data, name='cart_data'),
    path('delete_cart<int:data_id>/', views.delete_cart, name='delete_cart'),
    path('checkout', views.checkout, name='checkout'),
    path('checkout_data', views.checkout_data, name='checkout_data'),
    path('order_confirm', views.order_confirm, name='order_confirm'),
]