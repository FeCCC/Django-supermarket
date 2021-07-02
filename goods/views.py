from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Goods
from .forms import GoodsForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def goods_view(request):
    goods_list = Goods.objects.all()
    paginator = Paginator(goods_list, 10)

    page = request.GET.get('page')
    goods = paginator.get_page(page)
    context = {'goods': goods}
    context['title'] = '商品信息'
    return render(request, 'goods.html', context)


@login_required
def add_goods(request, goods_id):
    if str(goods_id) == '0':
        context = {'title': '添加商品'}
        if request.method == 'POST':
            form = GoodsForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('goods'))
        else:
            form = GoodsForm()
        context['form'] = form
    else:
        context = {'title': '修改商品'}
        goods = Goods.objects.get(pk=goods_id)
        if request.method == 'POST':
            form = GoodsForm(request.POST, instance=goods)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('goods'))
        else:
            form = GoodsForm(instance=goods)
        context['form'] = form
        context['goods'] = goods
    return render(request, 'add_goods.html', context)


@login_required
def delete_goods(request, goods_id):
    goods = Goods.objects.get(pk=goods_id)
    goods.delete()
    return HttpResponseRedirect(reverse('goods'))


@login_required
def search_goods(request):
    search = request.GET.get('search')
    error_msg = ''

    if not search:
        error_msg = '请输入关键词'

    goods_list = Goods.objects.filter(Q(g_id__icontains=search) | Q(g_name__icontains=search) | Q(g_type__icontains=search) | Q(
        g_name__icontains=search) | Q(unit__icontains=search) | Q(sp_id__sp_id__icontains=search) | Q(sp_id__sp_name__icontains=search))
    paginator = Paginator(goods_list, 10)
    page = request.GET.get('page')
    goods = paginator.get_page(page)
    context = {'goods': goods}
    context['title'] = '搜索结果'
    context['error_msg'] = error_msg
    context['search'] = search
    return render(request, 'goods.html', context)
