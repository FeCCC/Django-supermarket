"""supermarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from index.views import index
import goods.views as goods
import purchase.views as purchase
import sale.views as sales
import supplier.views as suppliers
import stock.views as stocks


urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('goods/', goods.goods_view, name='goods'),
    path('search_goods', goods.search_goods, name='search_goods'),
    path('add_goods/<str:goods_id>', goods.add_goods, name='add_goods'),
    path('delete_goods/<str:goods_id>', goods.delete_goods, name='delete_goods'),
    path('purchase', purchase.purchase_view, name='purchase'),
    path('search_purchase', purchase.search_purchase, name='search_purchase'),
    path('add_purchase/<str:purchase_id>', purchase.add_purchase, name='add_purchase'),
    path('delete_purchase/<str:purchase_id>', purchase.delete_purchase, name='delete_purchase'),
    path('sales', sales.sales_view, name='sales'),
    path('search_sales', sales.search_sales, name='search_sales'),
    path('add_sales/<str:sales_id>', sales.add_sales, name='add_sales'),
    path('delete_sales/<str:sales_id>', sales.delete_sales, name='delete_sales'),
    path('suppliers', suppliers.suppliers_view, name='suppliers'),
    path('search_suppliers', suppliers.search_suppliers, name='search_suppliers'),
    path('add_suppliers/<str:suppliers_id>', suppliers.add_suppliers, name='add_suppliers'),
    path('delete_suppliers/<str:suppliers_id>', suppliers.delete_suppliers, name='delete_suppliers'),
    path('stocks', stocks.stocks_view, name='stocks'),
    path('search_stocks', stocks.search_stocks, name='search_stocks'),
    path('add_stocks/<str:stocks_id>', stocks.add_stocks, name='add_stocks'),
    path('delete_stocks/<str:stocks_id>', stocks.delete_stocks, name='delete_stocks'),
]
