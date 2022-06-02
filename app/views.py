from django.shortcuts import render, redirect
from .models import Supplier, Product


def landingview(request):
    return render(request, 'landingpage.html')


################## Product views #######################

def productlistview(request):
    productlist = Product.objects.all()
    supplierlist = Supplier.objects.all()
    context = {'products': productlist, 'suppliers': supplierlist}
    return render (request,"productlist.html",context)


def addproduct(request):
    a = request.POST['productname']
    b = request.POST['packagesize']
    c = request.POST['unitprice']
    d = request.POST['unitsinstock']
    e = request.POST['supplier']
    
    Product(productname = a, packagesize = b, unitprice = c, unitsinstock = d, supplier = Supplier.objects.get(id = e)).save()
    return redirect(request.META['HTTP_REFERER'])


# Hakee tuotteet toimittajan mukaan
def productsfiltered(request, id):
    productlist = Product.objects.all()
    supplierlist = Supplier.objects.all()
    supplier = Supplier.objects.get(id = id)
    filteredproducts = productlist.filter(supplier = id)
    context = {'products': filteredproducts, 'suppliers': supplierlist, 'supplier': supplier}
    return render (request,"filteredproductlist.html",context)


# Muokkaus get
def editproductget(request, id):
        product = Product.objects.get(id = id)
        context = {'product': product}
        return render (request,"editproduct.html",context)

# Muokkaus post
def editproductpost(request, id):
        item = Product.objects.get(id = id)
        item.unitprice = request.POST['unitprice']
        item.unitsinstock = request.POST['unitsinstock']
        item.save()
        return redirect(productlistview)


############### Supplier views ########################

def supplierlistview(request):
    supplierlist = Supplier.objects.all()
    context = {'suppliers': supplierlist}
    return render (request,"supplierlist.html",context)


def addsupplier(request):
    a = request.POST['companyname']
    b = request.POST['contactname']
    c = request.POST['address']
    d = request.POST['phone']
    e = request.POST['email']
    f = request.POST['country']
    Supplier(companyname = a, contactname = b, address = c, phone = d, email = e, country = f).save()
    return redirect(request.META['HTTP_REFERER'])


# Poisto get (lataa vahvistussivun)
def confirmdeletesupplier(request, id):
    supplier = Supplier.objects.get(id = id)
    context = {'supplier': supplier}
    return render (request,"confirmdelsupp.html",context)


# Poisto post (toteuttaa poiston tietokantaan ja palauttaa supplierlistauksen)
def deletesupplier(request, id):
    Supplier.objects.get(id = id).delete()
    return redirect(supplierlistview)


# Hakee toimittajan nimellä tai nimen osalla
def searchsuppliers(request):
    search = request.POST['search']
    filtered = Supplier.objects.filter(companyname__icontains=search)
    context = {'suppliers': filtered}
    return render (request,"searchsuppliers.html",context)