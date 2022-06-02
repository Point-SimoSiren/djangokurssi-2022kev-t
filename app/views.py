from django.shortcuts import render
from .models import Supplier, Product


def landingview(request):
    return render(request, 'landingpage.html')

# Product views
def productlistview(request):
    return render(request, 'productlist.html')


# Supplier views
def supplierlistview(request):
    supplierlist = Supplier.objects.all()
    context = {'suppliers': supplierlist}
    return render (request,"supplierlist.html",context)
