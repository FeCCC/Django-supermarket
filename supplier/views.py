from django.shortcuts import render
from .models import Supplier
from .forms import SuppliersForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.


@login_required
def suppliers_view(request):
    context = {'title': '供货商信息'}
    suppliers_list = Supplier.objects.all()
    paginator = Paginator(suppliers_list, 10)

    page = request.GET.get('page')
    suppliers = paginator.get_page(page)
    context['suppliers'] = suppliers
    return render(request, 'suppliers.html', context)


@login_required
def add_suppliers(request, suppliers_id):
    if str(suppliers_id) == '0':
        context = {'title': '添加供货商'}
        if request.method == 'POST':
            form = SuppliersForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('suppliers'))
        else:
            form = SuppliersForm()
        context['form'] = form
    else:
        context = {'title': '修改供货商'}
        suppliers = Supplier.objects.get(pk=suppliers_id)
        if request.method == 'POST':
            form = SuppliersForm(request.POST, instance=suppliers)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('suppliers'))
        else:
            form = SuppliersForm(instance=suppliers)
        context['form'] = form
        context['suppliers'] = suppliers
    return render(request, 'add_suppliers.html', context)


@login_required
def delete_suppliers(request, suppliers_id):
    suppliers = Supplier.objects.get(pk=suppliers_id)
    suppliers.delete()
    return HttpResponseRedirect(reverse('suppliers'))


@login_required
def search_suppliers(request):
    search = request.GET.get('search')
    error_msg = ''

    if not search:
        error_msg = '请输入关键词'

    suppliers_list = Supplier.objects.filter(
        Q(sp_id__icontains=search) | Q(sp_name__icontains=search) | Q(address__icontains=search) | Q(c_person__icontains=search) | Q(c_phone__icontains=search))
    paginator = Paginator(suppliers_list, 10)
    page = request.GET.get('page')
    suppliers = paginator.get_page(page)
    context = {'suppliers': suppliers}
    context['title'] = '搜索结果'
    context['error_msg'] = error_msg
    context['search'] = search
    return render(request, 'suppliers.html', context)
