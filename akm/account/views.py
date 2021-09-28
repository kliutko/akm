
from django.shortcuts import render, redirect
from .models import *
from .forms import *




# Create your views here.


def account(request):
    error_form = ''
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account')
        else:
            error_form = 'Введены неверные данные!'

    role = Role.objects.all()
    profile = Profile.objects.all()
    entity = Entity.objects.all()
    subject = Subject.objects.all()
    service = Service.objects.all()
    serviceform = ServiceForm()
    subjectform = SubjectForm()
    entityform = EntityForm()

    data = {
        'entityform': entityform,
        'subjectform': subjectform,
        'serviceform': serviceform,
        'error_form': error_form,
        'role': role,
        'profile': profile,
        'entity': entity,
        'subject': subject,
        'service': service,
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


    return render(request, 'account/profile.html', data)
