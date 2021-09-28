from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.
def about(request):
    portfolio = Portfolio.objects.all()
    data = {
        'portfolio': portfolio,

        'ids_news': '2',     # id for displaying the news on the main page
        'name_site': 'Название сайта',
        'email_header': 'Почта',
        'phoneheader': 'Телефон',
        'fb_url': 'Ссылка на facebook',
        'tw_url': 'Ссылка на twitter',
        'ld_url': 'Ссылка на linkedin',
        'inst_url': 'Ссылка на instagram',
        'title_main': 'Информация',  # title in string main
        'subtitle_main': 'о компании',  # subtitle us string main
        'image_header': '/static/images/hero_bg_2.jpg',  # image us main
        'text_button_1': 'Download',
        'link_button_1': '#',
        'text_button_2': 'GetInTouch',
        'link_button_2': '#',
        'leadership': 'Руководство',

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
        'leadership_1': int(1),  # leadership_1
        'leadership_2': int(2),  #leadership_2
        'More_Peopple': 'Наши сотрудники',

        'contact_us_text': 'Связяаться с нами!',
        'contact_us_urls': '/contact',

    }


    return render(request, 'about/about.html', data)




def show_portfolio(request, portfolio_slug):
    post = get_object_or_404(Portfolio, slug=portfolio_slug)

    data = {
        'post': post,

        'ids_news': '2',  # id for displaying the news on the main page
        'name_site': 'Название сайта',
        'email_header': 'Почта',
        'phoneheader': 'Телефон',
        'fb_url': 'Ссылка на facebook',
        'tw_url': 'Ссылка на twitter',
        'ld_url': 'Ссылка на linkedin',
        'inst_url': 'Ссылка на instagram',
        'title_main': 'Информация',  # title in string main
        'subtitle_main': 'о компании',  # subtitle us string main
        'image_header': '/static/images/hero_bg_2.jpg',  # image us main
        'text_button_1': 'Download',
        'link_button_1': '#',
        'text_button_2': 'GetInTouch',
        'link_button_2': '#',
        'leadership': 'Руководство',

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
        'leadership_1': int(1),  # leadership_1
        'leadership_2': int(2),  # leadership_2
        'More_Peopple': 'Наши сотрудники',

        'contact_us_text': 'Связяаться с нами!',
        'contact_us_urls': '/contact',
    }
    return render(request, 'about/portfolio.html', data)

def show_category_portfolio(request, category_slug):
    category = get_object_or_404(Category_Portfolio, slug=category_slug)
    portfolio = Portfolio.objects.all()
    data = {
        'portfolio': portfolio,
        'category': category,
        'ids_news': '2',  # id for displaying the news on the main page
        'name_site': 'Название сайта',
        'email_header': 'Почта',
        'phoneheader': 'Телефон',
        'fb_url': 'Ссылка на facebook',
        'tw_url': 'Ссылка на twitter',
        'ld_url': 'Ссылка на linkedin',
        'inst_url': 'Ссылка на instagram',
        'title_main': 'Информация',  # title in string main
        'subtitle_main': 'о компании',  # subtitle us string main
        'image_header': '/static/images/hero_bg_2.jpg',  # image us main
        'text_button_1': 'Download',
        'link_button_1': '#',
        'text_button_2': 'GetInTouch',
        'link_button_2': '#',
        'leadership': 'Руководство',

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
        'leadership_1': int(1),  # leadership_1
        'leadership_2': int(2),  # leadership_2
        'More_Peopple': 'Наши сотрудники',

        'contact_us_text': 'Связяаться с нами!',
        'contact_us_urls': '/contact',


    }
    return render(request, 'about/category_portfolio.html', data)