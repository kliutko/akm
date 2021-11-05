from django.shortcuts import redirect
from django.shortcuts import render
import requests

import main
from news.models import News_category
from .forms import *


# Create your views here.
def send_telegram(text: str):
    token = '2018618673:AAFeAMB9pYqGNAOZpwhd57MsYvtSe_byLWQ' # token
    url = 'https://api.telegram.org/bot'
    channel_id = '-586479976'  # id группы
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
            # Формируем сообщение
            text = f'Сообщение отправлено из формы обратной связи с сайта :\n' \
                   f'Имя: {request.POST["name"]}\nEmail: {request.POST["email"]}\nСообщение:\n{request.POST["message"]}'
            form.save()
            send_telegram(text) # Передаем сообщение в sendmessage
            return redirect('feedback')
        else:
            error_form = 'Введены неверные данные!'

    form = FeedbackForm()
    cat = News_category.objects.all()

    data = {

        'cat': cat,
        'form': form,
        'error_form': error_form,
        'feedback': feedback,


        'name_site': main.mixdata.data['name_site'],
        'email_header': main.mixdata.data['email_header'],
        'phoneheader': main.mixdata.data['phoneheader'],
        'tg_url': main.mixdata.data['tg_url'],  # social iconus header
        'fb_url': main.mixdata.data['fb_url'],
        'vk_url': main.mixdata.data['vk_url'],
        'ld_url': main.mixdata.data['ld_url'],
        'inst_url': main.mixdata.data['inst_url'],  # /social iconus header
        'title_main': main.mixdata.data['title_main'],  # title in string main
        'subtitle_main': main.mixdata.data['subtitle_main'],  # subtitle us string main
        'image_header_feedback': main.mixdata.data['image_header_feedback'],  # image us feedback
        'text_button_1': 'Download',
        'link_button_1': '#',
        'text_button_2': 'GetInTouch',
        'link_button_2': '#',

        'title_feedback_map': main.mixdata.data['title_feedback_map'],  # title header string map
        'subtitle_feedback_map': main.mixdata.data['subtitle_feedback_map'],  # title header string map
        'footer_copyright': main.mixdata.data['footer_copyright'],  # footer
        'blok_adress_title': main.mixdata.data['blok_adress_title'],
        'block_adres_subtitle': main.mixdata.data['block_adres_subtitle'],
        'block_adres_subtitle_1': main.mixdata.data['block_adres_subtitle_1'],
        'block_adres_subtitle_2': main.mixdata.data['block_adres_subtitle_2'],
        'block_adres_subtitle_3': main.mixdata.data['block_adres_subtitle_3'],
        'block_adres_subtitle_4': main.mixdata.data['block_adres_subtitle_4'],
        'blok_0_adress_title': main.mixdata.data['block_adres_subtitle_4'],
        'block_0_adres_subtitle': main.mixdata.data['block_0_adres_subtitle'],
        'block_0_adres_subtitle_1': main.mixdata.data['block_0_adres_subtitle_1'],
        'block_0_adres_subtitle_2': main.mixdata.data['block_0_adres_subtitle_2'],
        'block_0_adres_subtitle_3': main.mixdata.data['block_0_adres_subtitle_3'],
        'block_0_adres_subtitle_4': main.mixdata.data['block_0_adres_subtitle_4'],  # /footer

        'header_block_right': main.mixdata.data['header_block_right'], # block string fadback right
        'title_1_block_right': main.mixdata.data['title_1_block_right'],
        'subtitle_1_block_right': main.mixdata.data['subtitle_1_block_right'],
        'title_2_block_right': main.mixdata.data['title_2_block_right'],
        'subtitle_2_block_right': main.mixdata.data['subtitle_2_block_right'],
        'title_3_block_right': main.mixdata.data['title_3_block_right'],
        'subtitle_3_block_right': main.mixdata.data['subtitle_3_block_right'],  # /block string fadback right

        'title_block_2': main.mixdata.data['title_block_2'],  # block2 in feedback
        'subtitle_block_2': main.mixdata.data['subtitle_block_2'],
        'btn_block_2': main.mixdata.data['btn_block_2'],
        'url_block_2': main.mixdata.data['url_block_2'],  # /block2 in feedback
        'feedbackmap1': main.mixdata.data['feedbackmap1'],  # block visitinoffice

    }

    return render(request, 'feedback/contact.html', data)


def feedbackmap(request):
    cat = News_category.objects.all()

    data = {

        'cat': cat,
        'name_site': main.mixdata.data['name_site'],
        'email_header': main.mixdata.data['email_header'],
        'phoneheader': main.mixdata.data['phoneheader'],
        'tg_url': main.mixdata.data['tg_url'],  # social iconus header
        'fb_url': main.mixdata.data['fb_url'],
        'vk_url': main.mixdata.data['vk_url'],
        'ld_url': main.mixdata.data['ld_url'],
        'inst_url': main.mixdata.data['inst_url'],  # /social iconus header
        'title_main': main.mixdata.data['title_main'],  # title in string main
        'subtitle_main': main.mixdata.data['subtitle_main'],  # subtitle us string main
        'image_header_feedback': main.mixdata.data['image_header_feedback'],  # image us feedback
        'text_button_1': 'Download',
        'link_button_1': '#',
        'text_button_2': 'GetInTouch',
        'link_button_2': '#',

        'title_feedback_map': main.mixdata.data['title_feedback_map'],  # title header string map
        'subtitle_feedback_map': main.mixdata.data['subtitle_feedback_map'],  # title header string map
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

        'header_block_right': main.mixdata.data['header_block_right'], # block string fadback right
        'title_1_block_right': main.mixdata.data['title_1_block_right'],
        'subtitle_1_block_right': main.mixdata.data['subtitle_1_block_right'],
        'title_2_block_right': main.mixdata.data['title_2_block_right'],
        'subtitle_2_block_right': main.mixdata.data['subtitle_2_block_right'],
        'title_3_block_right': main.mixdata.data['title_3_block_right'],
        'subtitle_3_block_right': main.mixdata.data['subtitle_3_block_right'],  # /block string fadback right

        'title_block_2': main.mixdata.data['title_block_2'],  # block2 in feedback
        'subtitle_block_2': main.mixdata.data['subtitle_block_2'],
        'btn_block_2': main.mixdata.data['btn_block_2'],
        'url_block_2': main.mixdata.data['url_block_2'],  # /block2 in feedback
        'feedbackmap1': main.mixdata.data['feedbackmap1'],  # block visitinoffice

    }
    return render(request, 'feedback/map.html', data)




