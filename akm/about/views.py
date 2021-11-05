from django.shortcuts import render, redirect, get_object_or_404

import main
from news.models import News_category
from .models import *


# Create your views here.
def about(request):
    portfolio = Portfolio.objects.all()
    cat = News_category.objects.all()

    data = {

        'cat': cat,
        'portfolio': portfolio,

        'block_1_title': main.mixdata.data['block_1_title'],  # block_1 uslugi
        'block_1_subtitle': main.mixdata.data['block_1_subtitle'],
        'block_1_message': main.mixdata.data['block_1_message'],  # /block_1 uslugi
        'block_2_title': main.mixdata.data['block_2_title'],  # block_2 history
        'block_2_subtitle': main.mixdata.data['block_2_subtitle'],
        'block_2_history_title': main.mixdata.data['block_2_history_title'],
        'block_2_history_message': main.mixdata.data['block_2_history_message'],  # /block_2 history

        'name_site': main.mixdata.data['name_site'],
        'email_header': main.mixdata.data['email_header'],
        'phoneheader': main.mixdata.data['phoneheader'],
        'tg_url': main.mixdata.data['tg_url'],  # social iconus header
        'fb_url': main.mixdata.data['fb_url'],
        'vk_url': main.mixdata.data['vk_url'],
        'ld_url': main.mixdata.data['ld_url'],
        'inst_url': main.mixdata.data['inst_url'],  # /social iconus header
        'title_about': main.mixdata.data['title_about'],  # title in string main
        'subtitle_about': main.mixdata.data['subtitle_about'],  # subtitle us string main
        'image_header_about': main.mixdata.data['image_header_about'],  # image us main
        'text_button_1': 'Download',
        'link_button_1': '#',
        'text_button_2': 'GetInTouch',
        'link_button_2': '#',

        'leadership': main.mixdata.data['leadership'],
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
        'leadership_1': main.mixdata.data['leadership_1'],  # leadership_1
        'leadership_2': main.mixdata.data['leadership_2'],  # leadership_2
        'More_Peopple': main.mixdata.data['More_Peopple'],

        'contact_us_text': main.mixdata.data['contact_us_text'],
        'contact_us_urls': main.mixdata.data['contact_us_urls'],

    }

    return render(request, 'about/about.html', data)


def show_portfolio(request, portfolio_slug):
    post = get_object_or_404(Portfolio, slug=portfolio_slug)
    cat = News_category.objects.all()

    data = {

        'cat': cat,
        'post': post,

        'block_1_title': main.mixdata.data['block_1_title'],  # block_1 uslugi
        'block_1_subtitle': main.mixdata.data['block_1_subtitle'],
        'block_1_message': main.mixdata.data['block_1_message'],  # /block_1 uslugi
        'block_2_title': main.mixdata.data['block_2_title'],  # block_2 history
        'block_2_subtitle': main.mixdata.data['block_2_subtitle'],
        'block_2_history_title': main.mixdata.data['block_2_history_title'],
        'block_2_history_message': main.mixdata.data['block_2_history_message'],  # /block_2 history

        'name_site': main.mixdata.data['name_site'],
        'email_header': main.mixdata.data['email_header'],
        'phoneheader': main.mixdata.data['phoneheader'],
        'tg_url': main.mixdata.data['tg_url'],  # social iconus header
        'fb_url': main.mixdata.data['fb_url'],
        'vk_url': main.mixdata.data['vk_url'],
        'ld_url': main.mixdata.data['ld_url'],
        'inst_url': main.mixdata.data['inst_url'],  # /social iconus header
        'title_about': main.mixdata.data['title_about'],  # title in string main
        'subtitle_about': main.mixdata.data['subtitle_about'],  # subtitle us string main
        'image_header_about': main.mixdata.data['image_header_about'],  # image us main
        'text_button_1': 'Download',
        'link_button_1': '#',
        'text_button_2': 'GetInTouch',
        'link_button_2': '#',

        'leadership': main.mixdata.data['leadership'],
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
        'leadership_1': main.mixdata.data['leadership_1'],  # leadership_1
        'leadership_2': main.mixdata.data['leadership_2'],  # leadership_2
        'More_Peopple': main.mixdata.data['More_Peopple'],

        'contact_us_text': main.mixdata.data['contact_us_text'],
        'contact_us_urls': main.mixdata.data['contact_us_urls'],
    }
    return render(request, 'about/portfolio.html', data)


def show_category_portfolio(request, category_slug):
    category = get_object_or_404(Category_Portfolio, slug=category_slug)
    port = Portfolio.objects.filter(slug=category_slug)
    port1 = Portfolio.objects.all()
    cats = Category_Portfolio.objects.all()
    cat = News_category.objects.all()

    data = {

        'cat': cat,
        'port': port,
        'category': category,
        'cats': cats,
        'cat_selected': category_slug,
        'port1': port1,

        'block_1_title': main.mixdata.data['block_1_title'],  # block_1 uslugi
        'block_1_subtitle': main.mixdata.data['block_1_subtitle'],
        'block_1_message': main.mixdata.data['block_1_message'],  # /block_1 uslugi
        'block_2_title': main.mixdata.data['block_2_title'],  # block_2 history
        'block_2_subtitle': main.mixdata.data['block_2_subtitle'],
        'block_2_history_title': main.mixdata.data['block_2_history_title'],
        'block_2_history_message': main.mixdata.data['block_2_history_message'],  # /block_2 history

        'name_site': main.mixdata.data['name_site'],
        'email_header': main.mixdata.data['email_header'],
        'phoneheader': main.mixdata.data['phoneheader'],
        'tg_url': main.mixdata.data['tg_url'],  # social iconus header
        'fb_url': main.mixdata.data['fb_url'],
        'vk_url': main.mixdata.data['vk_url'],
        'ld_url': main.mixdata.data['ld_url'],
        'inst_url': main.mixdata.data['inst_url'],  # /social iconus header
        'title_about': main.mixdata.data['title_about'],  # title in string main
        'subtitle_about': main.mixdata.data['subtitle_about'],  # subtitle us string main
        'image_header_about': main.mixdata.data['image_header_about'],  # image us main
        'text_button_1': 'Download',
        'link_button_1': '#',
        'text_button_2': 'GetInTouch',
        'link_button_2': '#',

        'leadership': main.mixdata.data['leadership'],
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
        'leadership_1': main.mixdata.data['leadership_1'],  # leadership_1
        'leadership_2': main.mixdata.data['leadership_2'],  # leadership_2
        'More_Peopple': main.mixdata.data['More_Peopple'],

        'contact_us_text': main.mixdata.data['contact_us_text'],
        'contact_us_urls': main.mixdata.data['contact_us_urls'],

    }
    return render(request, 'about/category_portfolio.html', data)
