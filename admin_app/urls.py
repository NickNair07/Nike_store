from django.urls import path
from . import views

urlpatterns = [
    path('admin_page/', views.admin_page, name='admin_page'),
    path('add_category/', views.add_category, name='add_category'),
    path('category_data/', views.category_data, name='category_data'),
    path('display_category/', views.display_category, name='display_category'),
    path('edit_category/<int:data_id>/', views.edit_category, name='edit_category'),
    path('update_category/<int:data_id>/', views.update_category, name='update_category'),
    path('delete_category/<int:data_id>/', views.delete_category, name='delete_category'),

    path('add_product/', views.add_product, name='add_product'),
    path('display_product/', views.display_product, name='display_product'),
    path('product_data/', views.product_data, name='product_data'),
    path('edit_product/<int:data_id>/', views.edit_product, name='edit_product'),
    path('update_product/<int:data_id>/', views.update_product, name='update_product'),
    path('delete_product/<int:data_id>/', views.delete_product, name='delete_product'),
]
