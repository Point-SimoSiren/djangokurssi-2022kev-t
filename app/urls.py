from django.urls import path

from .views import productlistview, supplierlistview, addsupplier, confirmdeletesupplier, deletesupplier, \
addproduct, productsfiltered, searchsuppliers, editproductget, editproductpost, loginview, login_action, \
logout_action

urlpatterns = [
    # Login & logout
    path('', loginview),
    path('login/', login_action),
    path('logout/', logout_action),

    # Products url´s
    path('products/', productlistview),
    path('add-product/', addproduct),
    path('products-by-supplier/<int:id>/', productsfiltered),
    path('edit-product-get/<int:id>/', editproductget),
    path('edit-product-post/<int:id>/', editproductpost),


    # Supplier url´s
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
    path('delete-supplier/<int:id>/', deletesupplier),
    path('confirm-delete-supplier/<int:id>/', confirmdeletesupplier),
    path('search-suppliers/', searchsuppliers),
]
