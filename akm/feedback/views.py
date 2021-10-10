from django.contrib.sites import requests
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import *

from .models import *

# Create your views here.
def send_telegram(text: str):
    token = '2018618673:AAFeAMB9pYqGNAOZpwhd57MsYvtSe_byLWQ'
    url = 'https://api.telegram.org/bot'
    channel_id = '-586479976'
    url += token
    method = url + '/sendmessage'

    r = requests.post(method, data={
        'chat_id': channel_id,
        'text': text,
    })
    if r.status_code != 200:
        raise Exception('Post_text_error')


if __name__ == '__main__':
    send_telegram('hello world')

def feedback(request):
    error_form = ''
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()


            return redirect('feedback')
        else:
            error_form = 'Введены неверные данные!'


    form = FeedbackForm()
    data = {
        'form': form,
        'error_form': error_form,
        'feedback': feedback,

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

        'title_feedback': 'Форма',  # title header string news
        'subtitle_feedback': 'Обратной связи',  # title header string news
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


        'header_block_right': 'Контактная информация',    #block string fadback right
        'title_1_block_right': 'Адрес:',
        'subtitle_1_block_right': '203 Fake St.Mountain View, San Francisco, California, USA',
        'title_2_block_right': 'Телефон',
        'subtitle_2_block_right': '+375 29 3579512',
         'title_3_block_right': 'Email',
        'subtitle_3_block_right': 'Email@domain.by',         #/block string fadback right

        'title_block_2':'Заголовок',    #block2 in feedback
        'subtitle_block_2': 'текст текст текст текст текст текст текст текст текст текст текст ',
        'btn_block_2': 'Перейти ',
        'url_block_2': '#',   #/block2 in feedback
        'feedbackmap1': 'Визит в офис',         #block visitinoffice

        }

    return render(request, 'feedback/contact.html', data)



def feedbackmap(request):
    data = {


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

        'title_feedback': 'Карта',  # title header string news
        'subtitle_feedback': '',  # title header string news
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


        'header_block_right': 'Контактная информация',    #block string fadback right
        'title_1_block_right': 'Адрес:',
        'subtitle_1_block_right': '203 Fake St.Mountain View, San Francisco, California, USA',
        'title_2_block_right': 'Телефон',
        'subtitle_2_block_right': '+375 29 3579512',
         'title_3_block_right': 'Email',
        'subtitle_3_block_right': 'Email@domain.by',         #/block string fadback right

        'title_block_2':'Заголовок',    #block2 in feedback
        'subtitle_block_2': 'текст текст текст текст текст текст текст текст текст текст текст ',
        'btn_block_2': 'Перейти ',
        'url_block_2': '#',   #/block2 in feedback



        }
    return render(request, 'feedback/map.html', data)

