from django.urls import path

from .views import landingview, productlistview, supplierlistview, addsupplier, confirmdeletesupplier, deletesupplier, \
addproduct, productsfiltered, searchsuppliers, editproductget, editproductpost

urlpatterns = [
    path('', landingview),

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
