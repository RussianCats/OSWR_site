from django.shortcuts import render, get_list_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from goods.models import Products

from goods.utils import q_search

# Create your views here.
def catalog(request, category_slug=None):

    #получить параметр page из строки запроса (URL)
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)


    if category_slug == 'all':
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    # только со скидкой
    if on_sale:
        goods = goods.filter(discount__gt=0)

    # сортировка по цене
    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    # Пагинация
    paginator = Paginator(goods, 3)  # 3 товара на страницу
    current_page = paginator.page(int(page))

    context = {
        'title': 'Home - Каталог',
        'goods': current_page,
        'slug_url': category_slug
    }
    return render(request, 'goods/catalog.html', context)

def product(request, product_slug):
    
    product = Products.objects.get(slug=product_slug)

    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
        'product': product
    }

    return render(request, 'goods/product.html', context=context)

