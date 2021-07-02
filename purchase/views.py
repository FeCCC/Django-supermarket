from django.shortcuts import render
from .models import Purchase
from stock.models import Stock
from .forms import PurchaseForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.db.models import Q

# Create your views here.


def purchase_view(request):
    context = {'title': '进货清单'}
    purchase_list = Purchase.objects.all()
    paginator = Paginator(purchase_list, 10)

    page = request.GET.get('page')
    purchase = paginator.get_page(page)
    context['purchase'] = purchase
    return render(request, 'purchase.html', context)


def add_purchase(request, purchase_id):
    if str(purchase_id) == '0':
        context = {'title': '商品进货'}
        if request.method == 'POST':
            form = PurchaseForm(request.POST)
            if form.is_valid():
                if Stock.objects.filter(g_id_id=form.data.get('g_id')):
                    stock = Stock.objects.get(g_id_id=form.data.get('g_id'))
                    stock_num = stock.s_num + int(form.data.get('p_num'))
                    stock.s_num = stock_num
                    stock.save()
                    form.save()
                    return HttpResponseRedirect(reverse('purchase'))
                else:
                    stock = {}
                    stock['g_id_id'] =form.data.get('g_id')
                    print(form.data.get('p_num'))
                    stock['s_num'] = form.data.get('p_num')
                    stock['sp_id_id'] = form.data.get('sp_id')
                    Stock.objects.create(**stock)
                    form.save()
                    return HttpResponseRedirect(reverse('purchase'))
        else:
            form = PurchaseForm()
        context['form'] = form
    else:
        context = {'title': '修改记录'}
        purchase = Purchase.objects.get(pk=purchase_id)
        if request.method == 'POST':
            form = PurchaseForm(request.POST, instance=purchase)
            if form.is_valid():
                purchase_num = Purchase.objects.get(pk=purchase_id).p_num
                num_change = int(form.data.get('p_num')) - purchase_num
                stock = Stock.objects.get(g_id_id=form.data.get('g_id'))
                stock.s_num = stock.s_num + num_change
                stock.save()
                form.save()
                return HttpResponseRedirect(reverse('purchase'))
        else:
            form = PurchaseForm(instance=purchase)
        context['form'] = form
        context['purchase'] = purchase
    return render(request, 'add_purchase.html', context)


def delete_purchase(request, purchase_id):
    purchase = Purchase.objects.get(pk=purchase_id)
    purchase.delete()
    return HttpResponseRedirect(reverse('purchase'))


def search_purchase(request):
    search = request.GET.get('search')
    error_msg = ''

    if not search:
        error_msg = '请输入关键词'

    purchase_list = Purchase.objects.filter(
        Q(p_id__icontains=search) | Q(p_num__icontains=search) | Q(p_price__icontains=search) | Q(g_id_id__g_id__icontains=search) | Q(sp_id_id__sp_id__icontains=search) | Q(st_id_id__st_id__icontains=search))
    paginator = Paginator(purchase_list, 10)
    page = request.GET.get('page')
    purchase = paginator.get_page(page)
    context = {'purchase': purchase}
    context['title'] = '搜索结果'
    context['error_msg'] = error_msg
    context['search'] = search
    return render(request, 'purchase.html', context)
