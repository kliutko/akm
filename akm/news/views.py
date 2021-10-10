from urllib import request
from .models import *
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView



from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



# Create your views here.



def news(request):
    '''Show all news'''
    news_list = News.objects.filter(is_published=True).order_by('-time_create')
    paginator = Paginator(news_list, 3)
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    data = {
        'news': news,
        'ids_news': '2',  # id for displaying the news on the main page
        'name_site': 'Название сайта',
        'email_header': 'Почта',
        'phoneheader': 'Телефон',
        'fb_url': 'Ссылка на facebook',
        'tw_url': 'Ссылка на twitter',
        'ld_url': 'Ссылка на linkedin',
        'inst_url': 'Ссылка на instagram',
        'title_main': 'Специальная технология',  # title in string main
        'subtitle_main': 'Обработки металла',  # subtitle us string main
        'image_header': '/static/images/hero_bg_2.jpg',  # image us main
        'text_button_1': 'Download',
        'link_button_1': '#',
        'text_button_2': 'GetInTouch',
        'link_button_2': '#',
        'title_news': 'Наши', # title header string news
        'subtitle_news': 'Новости',  # title header string news
        'image_header': '/static/images/hero_bg_2.jpg',
        'footer_copyright': 'Copyright © 2021 All Rights Reserved',  # footer
        'blok_adress_title': 'Беларусь, Брестская область',
        'block_adres_subtitle': 'Кобринский р-н, д. Пески-2',
        'block_adres_subtitle_1': ' ул.Луговая 26',
        'block_adres_subtitle_2': 'Tel. + 375(29) 112-76-32',
        'block_adres_subtitle_3': 'tests@tests.com',
        'block_adres_subtitle_4': 'УНП: 291052118',
        'blok_0_adress_title': '',
        'block_0_adres_subtitle': '',
        'block_0_adres_subtitle_1': '',
        'block_0_adres_subtitle_2': '',
        'block_0_adres_subtitle_3': '',
        'block_0_adres_subtitle_4': '',  # /footer
    }
    return render(request, 'news/news.html', data)



def show_news(request, news_slug):
    post = get_object_or_404(News, slug=news_slug)

    data = {
        'post': post,
        'title': post.title,
        'ids_news': '2',  # id for displaying the news on the main page
        'name_site': 'Название сайта',
        'email_header': 'Почта',
        'phoneheader': 'Телефон',
        'fb_url': 'Ссылка на facebook',
        'tw_url': 'Ссылка на twitter',
        'ld_url': 'Ссылка на linkedin',
        'inst_url': 'Ссылка на instagram',
        'title_main': 'Специальная технология',  # title in string main
        'subtitle_main': 'Обработки металла',  # subtitle us string main
        'image_header': '/static/images/hero_bg_2.jpg',  # image us main
        'text_button_1': 'Download',
        'link_button_1': '#',
        'text_button_2': 'GetInTouch',
        'link_button_2': '#',
        'title_news': 'Наши',  # title header string news
        'subtitle_news': 'Новости',  # title header string news
        'image_header': '/static/images/hero_bg_2.jpg',
        'footer_copyright': 'Copyright © 2021 All Rights Reserved',  # footer
        'blok_adress_title': 'Беларусь, Брестская область',
        'block_adres_subtitle': 'Кобринский р-н, д. Пески-2',
        'block_adres_subtitle_1': ' ул.Луговая 26',
        'block_adres_subtitle_2': 'Tel. + 375(29) 112-76-32',
        'block_adres_subtitle_3': 'tests@tests.com',
        'block_adres_subtitle_4': 'УНП: 291052118',
        'blok_0_adress_title': '',
        'block_0_adres_subtitle': '',
        'block_0_adres_subtitle_1': '',
        'block_0_adres_subtitle_2': '',
        'block_0_adres_subtitle_3': '',
        'block_0_adres_subtitle_4': '',  # /footer

    }
    return render(request, 'news/news-detail.html', data)

def show_categori(request, category_slug):
    post = get_object_or_404(News, slug=category_slug)
    data = {
        'post': post,
        'title': post.title,
        'content': post.content,


    }
    return render(request, 'news/news.html', data)
