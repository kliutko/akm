from urllib import request

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods

import main
from .models import *
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .forms import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from main.models import *



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
    cat = News_category.objects.all()
    reklama = ReklamaPost.objects.filter(is_published=True)

    data = {
        'reklama': reklama,

        'cat': cat,
        'news': news,

        'ids_news': '2',  # id for displaying the news on the main page
        'name_site': main.mixdata.data['name_site'],
        'email_header': main.mixdata.data['email_header'],
        'phoneheader': main.mixdata.data['phoneheader'],
        'tg_url': main.mixdata.data['tg_url'],  # social iconus header
        'fb_url': main.mixdata.data['fb_url'],
        'vk_url': main.mixdata.data['vk_url'],
        'ld_url': main.mixdata.data['ld_url'],
        'inst_url': main.mixdata.data['inst_url'],  # /social iconus header
        'text_button_1_news': 'Download',
        'link_button_1_news': '#',
        'text_button_2_news': 'GetInTouch',
        'link_button_2_news': '#',
        'title_news': main.mixdata.data['title_news'], # title header string news
        'subtitle_news': main.mixdata.data['subtitle_news'],  # title header string news
        'image_header_news': main.mixdata.data['image_header_news'],
        'footer_copyright': main.mixdata.data['footer_copyright'],  # footer
        'blok_adress_title': main.mixdata.data['blok_adress_title'],
        'block_adres_subtitle': main.mixdata.data['block_adres_subtitle'],
        'block_adres_subtitle_1': main.mixdata.data['block_adres_subtitle_1'],
        'block_adres_subtitle_2': main.mixdata.data['block_adres_subtitle_2'],
        'block_adres_subtitle_3': main.mixdata.data['block_adres_subtitle_3'],
        'block_adres_subtitle_4': main.mixdata.data['block_adres_subtitle_4'],
        'blok_0_adress_title': main.mixdata.data['blok_0_adress_title'],
        'block_0_adres_subtitle': main.mixdata.data['block_0_adres_subtitle'],
        'block_0_adres_subtitle_1': main.mixdata.data['block_0_adres_subtitle_1'],
        'block_0_adres_subtitle_2': main.mixdata.data['block_0_adres_subtitle_2'],
        'block_0_adres_subtitle_3': main.mixdata.data['block_0_adres_subtitle_3'],
        'block_0_adres_subtitle_4': main.mixdata.data['block_0_adres_subtitle_4'],  # /footer
    }
    return render(request, 'news/news.html', data)

# show cat

# def show_categori(request, category_slug):
#     post = get_object_or_404(News, slug=category_slug)
#     data = {
#         'post': post,
#         'title': post.title,
#         'content': post.content,
#
#
#     }
#     return render(request, 'news/news.html', data)
def show_category(request, category_slug):
    '''Show all news'''
    cat = News_category.objects.all()
    news_list = News.objects.filter(name_category__slug=category_slug, is_published=True).order_by('-time_create')
    paginator = Paginator(news_list, 3)
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    cat = News_category.objects.all()

    data = {
        'cat': cat,
        'news': news,
        # 'title': post.title,
        # 'content': post.content,

        'name_site': main.mixdata.data['name_site'],
        'email_header': main.mixdata.data['email_header'],
        'phoneheader': main.mixdata.data['phoneheader'],
        'tg_url': main.mixdata.data['tg_url'],  # social iconus header
        'fb_url': main.mixdata.data['fb_url'],
        'vk_url': main.mixdata.data['vk_url'],
        'ld_url': main.mixdata.data['ld_url'],
        'inst_url': main.mixdata.data['inst_url'],  # /social iconus header
        'text_button_1_news': 'Download',
        'link_button_1_news': '#',
        'text_button_2_news': 'GetInTouch',
        'link_button_2_news': '#',
        'title_news': main.mixdata.data['title_news'], # title header string news
        'subtitle_news': main.mixdata.data['subtitle_news'],  # title header string news
        'image_header_news': main.mixdata.data['image_header_news'],
        'footer_copyright': main.mixdata.data['footer_copyright'],  # footer
        'blok_adress_title': main.mixdata.data['blok_adress_title'],
        'block_adres_subtitle': main.mixdata.data['block_adres_subtitle'],
        'block_adres_subtitle_1': main.mixdata.data['block_adres_subtitle_1'],
        'block_adres_subtitle_2': main.mixdata.data['block_adres_subtitle_2'],
        'block_adres_subtitle_3': main.mixdata.data['block_adres_subtitle_3'],
        'block_adres_subtitle_4': main.mixdata.data['block_adres_subtitle_4'],
        'blok_0_adress_title': main.mixdata.data['blok_0_adress_title'],
        'block_0_adres_subtitle': main.mixdata.data['block_0_adres_subtitle'],
        'block_0_adres_subtitle_1': main.mixdata.data['block_0_adres_subtitle_1'],
        'block_0_adres_subtitle_2': main.mixdata.data['block_0_adres_subtitle_2'],
        'block_0_adres_subtitle_3': main.mixdata.data['block_0_adres_subtitle_3'],
        'block_0_adres_subtitle_4': main.mixdata.data['block_0_adres_subtitle_4'],  # /footer
    }
    return render(request, 'news/news.html', data)


# @login_required
# @require_http_methods(["POST"])
def show_news(request, news_slug):
    post = get_object_or_404(News, slug=news_slug)
    comments = NewsComment.objects.filter(name_news=post)
    error_form = ''
    if request.method == 'POST':
        form = NewsCommentForms(request.POST)
        if form.is_valid():
            form_comment = form.save(commit=False)
            form_comment.autor_comm = request.user
            form_comment.name_news = post
            form_comment.save()
        # return redirect('show_news')
        else:
            error_form = 'Введены неверные данные!'

    form_comment = NewsCommentForms()
    cat = News_category.objects.all()

    reklama = ReklamaPost.objects.filter(is_published=True)

    data = {
        'reklama': reklama,

        'cat': cat,
        'post': post,
        'form_coment': form_comment,
        'title': post.title,
        'comments': comments,
        'error_form': error_form,


        'name_site': main.mixdata.data['name_site'],
        'email_header': main.mixdata.data['email_header'],
        'phoneheader': main.mixdata.data['phoneheader'],
        'tg_url': main.mixdata.data['tg_url'],  # social iconus header
        'fb_url': main.mixdata.data['fb_url'],
        'vk_url': main.mixdata.data['vk_url'],
        'ld_url': main.mixdata.data['ld_url'],
        'inst_url': main.mixdata.data['inst_url'],  # /social iconus header
        'text_button_1_news': 'Download',
        'link_button_1_news': '#',
        'text_button_2_news': 'GetInTouch',
        'link_button_2_news': '#',
        'title_news': main.mixdata.data['title_news'], # title header string news
        'subtitle_news': main.mixdata.data['subtitle_news'],  # title header string news
        'image_header_news': main.mixdata.data['image_header_news'],
        'footer_copyright': main.mixdata.data['footer_copyright'],  # footer
        'blok_adress_title': main.mixdata.data['blok_adress_title'],
        'block_adres_subtitle': main.mixdata.data['block_adres_subtitle'],
        'block_adres_subtitle_1': main.mixdata.data['block_adres_subtitle_1'],
        'block_adres_subtitle_2': main.mixdata.data['block_adres_subtitle_2'],
        'block_adres_subtitle_3': main.mixdata.data['block_adres_subtitle_3'],
        'block_adres_subtitle_4': main.mixdata.data['block_adres_subtitle_4'],
        'blok_0_adress_title': main.mixdata.data['blok_0_adress_title'],
        'block_0_adres_subtitle': main.mixdata.data['block_0_adres_subtitle'],
        'block_0_adres_subtitle_1': main.mixdata.data['block_0_adres_subtitle_1'],
        'block_0_adres_subtitle_2': main.mixdata.data['block_0_adres_subtitle_2'],
        'block_0_adres_subtitle_3': main.mixdata.data['block_0_adres_subtitle_3'],
        'block_0_adres_subtitle_4': main.mixdata.data['block_0_adres_subtitle_4'],  # /footer

    }
    return render(request, 'news/news-detail.html', data)




