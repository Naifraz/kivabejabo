from django.shortcuts import render,HttpResponse,get_object_or_404, HttpResponseRedirect,redirect
from .models import author, article,content as ContentClass,Contatct,subscribe,\
    livingcost as LivingcostClass,earning  as EarningClass,\
    embassy_address as Embassy_adressClass,ticket_price as Ticket_priceClass
from django.db.models import Q
from itertools import chain
from django.contrib import messages
from django.conf import settings

# Create your views here.
def index(request):
    if request.method == 'POST':
        email = request.POST["email"]
        contact = subscribe(email=email)
        contact.save()
    articles = article.objects.all()
    contents = ContentClass.objects.all()
    livingcosts = LivingcostClass.objects.all()
    earnings = EarningClass.objects.all()
    embassy_addresss = Embassy_adressClass.objects.all()
    ticket_prices = Ticket_priceClass.objects.all()
    return render(request, "demo.html", {
        'articles': articles,
        'contents': contents,
        'livingcosts':livingcosts,
        'earnings':earnings,
        'embassy_address':embassy_addresss,
        'ticket_prices':ticket_prices
    })

def about(request):
    return render(request, "about.html")
def contact(request):
    return render(request, "contact.html")
def submission(request):
    if request.method == 'POST':
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        message= request.POST["message"]
        contact = Contatct(fname=fname,lname=lname,email=email,message=message)
        contact.save()
    return render(request, "contact.html")
def blogger(request,id):
    post = get_object_or_404(article, pk= id)
    if request.method == 'POST':
        message = request.POST['Country']

    context = {
        "post": post,

    }
    return render(request, "blog2.html",context)
def content(request,id):
    pos = get_object_or_404(ContentClass,pk=id)

    context = {
        "pos": pos,

    }
    return render(request, "blog3.html",context)
def livingcost(request,id):
    post = get_object_or_404(LivingcostClass,pk=id)
    first = LivingcostClass.objects.first()
    last = LivingcostClass.objects.last()
    context = {
        "post": post,
        "first": first,
        "last": last

    }
    return render(request, "blog4.html",context)
def earning(request,id):
    post = get_object_or_404(EarningClass,pk=id)
    first = EarningClass.objects.first()
    last = EarningClass.objects.last()
    context = {
        "post": post,
        "first": first,
        "last": last

    }
    return render(request, "blog5.html",context)
def embassy_address(request,id):
    post = get_object_or_404(Embassy_adressClass,pk=id)
    first = Embassy_adressClass.objects.first()
    last = Embassy_adressClass.objects.last()
    context = {
        "post": post,
        "first": first,
        "last": last

    }
    return render(request, "blog6.html",context)
def ticket_price(request,id):
    post = get_object_or_404(Ticket_priceClass,pk=id)
    first = Ticket_priceClass.objects.first()
    last = Ticket_priceClass.objects.last()
    context = {
        "post": post,
        "first": first,
        "last": last

    }
    return render(request, "blog7.html",context)
def count(request):
    return render(request, "count.html")
def counts(request):
    data = request.GET['fulltextarea']
    word_list = data.split()
    list_leanth = len(word_list)
    dat = request.GET['fulltextare']

    return render(request, "counts.html",{'fulltext':data,'word':list_leanth,'fulltex':dat}
)
def search(request):
    if request.method == 'POST':
        srch = request.POST['q']
        if srch:
            match = article.objects.filter(Q(title__icontains=srch) |
                                           Q(body__icontains=srch))
            if match:
                return render(request, 'search.html', {'sr': match})
            else:
                messages.error(request, 'no result found')
        else:
            return HttpResponseRedirect('search')
    return render(request, 'search.html')
