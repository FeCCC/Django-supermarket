from django.shortcuts import render
from .models import Sale
from stock.models import Stock
from .forms import SalesForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

# Create your views here.


@login_required
def sales_view(request):
    context = {'title': '销售清单'}
    sales_list = Sale.objects.all()
    paginator = Paginator(sales_list, 10)

    page = request.GET.get('page')
    sales = paginator.get_page(page)
    context['sales'] = sales
    return render(request, 'sales.html', context)


@login_required
def add_sales(request, sales_id):
    if str(sales_id) == '0':
        context = {'title': '商品进货'}
        if request.method == 'POST':
            form = SalesForm(request.POST)
            if form.is_valid():
                if Stock.objects.filter(g_id_id=form.data.get('g_id')):
                    stock = Stock.objects.get(g_id_id=form.data.get('g_id'))
                    stock_num = stock.s_num - int(form.data.get('s_num'))
                    if stock_num < 0:
                        messages.error(request, '库存不足!')
                    else:
                        stock.s_num = stock_num
                        stock.save()
                        form.save()
                        return HttpResponseRedirect(reverse('sales'))
                else:
                    messages.error(request, '库存不足!')
        else:
            form = SalesForm()
        context['form'] = form
    else:
        context = {'title': '修改记录'}
        sales = Sale.objects.get(pk=sales_id)
        if request.method == 'POST':
            form = SalesForm(request.POST, instance=sales)
            if form.is_valid():
                sale_num = Sale.objects.get(pk=sales_id).s_num
                num_change = int(form.data.get('s_num')) - sale_num
                stock = Stock.objects.get(g_id_id=form.data.get('g_id'))
                stock_num = stock.s_num - num_change
                if stock_num < 0:
                    messages.error(request, '库存不足!')
                else:
                    stock.s_num = stock_num
                    stock.save()
                    form.save()
                    return HttpResponseRedirect(reverse('sales'))
        else:
            form = SalesForm(instance=sales)
        context['form'] = form
        context['sales'] = sales
    return render(request, 'add_sales.html', context)


@login_required
def delete_sales(request, sales_id):
    sales = Sale.objects.get(pk=sales_id)
    sales.delete()
    return HttpResponseRedirect(reverse('sales'))


@login_required
def search_sales(request):
    search = request.GET.get('search')
    error_msg = ''

    if not search:
        error_msg = '请输入关键词'

    sales_list = Sale.objects.filter(
        Q(sa_id__icontains=search) | Q(s_num__icontains=search) | Q(s_price__icontains=search) | Q(g_id__g_id__icontains=search) | Q(g_id__g_name__icontains=search) | Q(g_id__unit__icontains=search) | Q(st_id__username__icontains=search))
    paginator = Paginator(sales_list, 10)
    page = request.GET.get('page')
    sales = paginator.get_page(page)
    context = {'sales': sales}
    context['title'] = '搜索结果'
    context['error_msg'] = error_msg
    context['search'] = search
    return render(request, 'sales.html', context)
