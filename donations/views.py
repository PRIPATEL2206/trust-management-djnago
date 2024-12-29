from django.http.request import HttpRequest
from django.shortcuts import render
from .forms import AddDonationForm,AddDonationTypeForm
from .models import DonationType,Donation
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def donation_type_page_view(request:HttpRequest):
    context={
        'donation_types':DonationType.objects.all()
    }
    return render(request,'donations/all_donations.html',context)

def donation_page_view(request:HttpRequest,id:str):
    page_number = request.GET.get('page',1)
    search = request.GET.get('search',"")
    sort_by = request.GET.get('sort_by',"created_at")

    donation_type = DonationType.objects.get(id=int(id))
    donations = Donation.objects.filter(
        Q(donation_for=id)& (
            Q(display_name__icontains=search) | 
            Q(handover_by__icontains=search) | 
            Q(desc__icontains=search) | 
            Q(add_by__username__icontains=search) 
        )
    ).order_by("-"+sort_by)
    paginatore= Paginator(donations,10)
    try:
        page = paginatore.get_page(page_number)
    except:
        page = paginatore.get_page(1)

    context={
        'page':page,
        'donation_type':donation_type,
        "total":paginatore.count,
        "total_pages":paginatore.num_pages,
        "search":search,
        "sort_by":sort_by
    }
    
    return render(request,'donations/donations.html',context)

def add_donation_types(request:HttpRequest):
    form = AddDonationTypeForm()
    if request.POST:
        form = AddDonationTypeForm(request.POST,request.FILES)
        if form.is_valid():
            donation_type = form.save(commit=False) 
            donation_type.created_by = request.user
            donation_type.save()
            form = AddDonationTypeForm()

    context = {
        'form':form,
        'title':"Add Doantion Type"
    }
    return render(request,'donations/add_page.html',context)

def add_donation(request:HttpRequest):
    donation_type = request.GET.get('type')
    form = AddDonationForm({"donation_for":donation_type})
    form.errors.clear()
    if request.POST:
        form = AddDonationForm(request.POST)
        if form.is_valid():
            donation_type = form.save(commit=False) 
            donation_type.add_by = request.user
            donation_type.save()
            form = AddDonationForm()

    context = {
        'form':form,
        'title':"Add Donations"
        }
    return render(request,'donations/add_page.html',context)