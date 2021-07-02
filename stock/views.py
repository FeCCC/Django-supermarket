from django.shortcuts import render
from .models import Stock
from .forms import StocksForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.


@login_required
def stocks_view(request):
    context = {'title': '库存清单'}
    stocks_list = Stock.objects.all()
    paginator = Paginator(stocks_list, 10)

    page = request.GET.get('page')
    stocks = paginator.get_page(page)
    context['stocks'] = stocks
    return render(request, 'stocks.html', context)


@login_required
def add_stocks(request, stocks_id):
    if str(stocks_id) == '0':
        context = {'title': '添加库存'}
        if request.method == 'POST':
            form = StocksForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('stocks'))
        else:
            form = StocksForm()
        context['form'] = form
    else:
        context = {'title': '修改记录'}
        stocks = Stock.objects.get(pk=stocks_id)
        if request.method == 'POST':
            form = StocksForm(request.POST, instance=stocks)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('stocks'))
        else:
            form = StocksForm(instance=stocks)
        context['form'] = form
        context['stocks'] = stocks
    return render(request, 'add_stocks.html', context)


@login_required
def delete_stocks(request, stocks_id):
    stocks = Stock.objects.get(pk=stocks_id)
    stocks.delete()
    return HttpResponseRedirect(reverse('stocks'))


@login_required
def search_stocks(request):
    search = request.GET.get('search')
    error_msg = ''

    if not search:
        error_msg = '请输入关键词'

    stocks_list = Stock.objects.filter(
        Q(s_id__icontains=search) | Q(s_num__icontains=search) | Q(g_id__g_id__icontains=search) | Q(g_id__g_name__icontains=search) | Q(g_id__g_type__icontains=search) | Q(g_id__unit__icontains=search) | Q(sp_id__sp_id__icontains=search) | Q(sp_id__sp_name__icontains=search))
    paginator = Paginator(stocks_list, 10)
    page = request.GET.get('page')
    stocks = paginator.get_page(page)
    context = {'stocks': stocks}
    context['title'] = '搜索结果'
    context['error_msg'] = error_msg
    context['search'] = search
    return render(request, 'stocks.html', context)
