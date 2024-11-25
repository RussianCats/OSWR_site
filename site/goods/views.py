from django.shortcuts import render, get_list_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from goods.models import Products

# Create your views here.
def catalog(request, category_slug, page = 1):


    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    # Пагинация
    paginator = Paginator(goods, 3)  # 3 товара на страницу
    page = request.GET.get('page', 1)

    try:
        current_page = paginator.page(int(page))
    except PageNotAnInteger:
        current_page = paginator.page(1)
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)


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

