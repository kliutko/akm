from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import *
from news.models import *
from about.models import *
from .models import *
from django.views.generic import DetailView, CreateView




# Create your views here.
def index(request):
    # if request.method == 'POST':
    #     form = FeedbackForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('index')


    news = News.objects.all()
    portfolio = Portfolio.objects.all()
    category_portfolio = Category_Portfolio.objects.all()
    # specialty = Specialty.objects.all()
    #
    # form = FeedbackForm()

    data = {
        # 'form' : form,
        # 'specialty': specialty,

        'news': news,
        'portfolio': portfolio,
        'category_portfolio': category_portfolio,
        'ids_news': '2',   # id for displaying the news on the main page
        'name_site': 'Название сайта',
        'email_header': 'Почта',
        'phoneheader': 'Телефон',
        'tg_url': 'Ссылка на telegram',    # social iconus header
        'fb_url': 'Ссылка на FaceBook',
        'vk_url': 'Ссылка на Vk',
        'ld_url': 'Ссылка на linkedin',
        'inst_url': 'Ссылка на instagram',  # /social iconus header
        'title_main': 'Компания',             # title in string main
        'subtitle_main': 'АРМКРАФТМЕТАЛЛ',        # subtitle us string main
        'image_header': '/static/images/hero_bg_2.jpg',     # image us main
        'text_button_1': 'Download',
        'link_button_1': '#',
        'text_button_2': 'GetInTouch',
        'link_button_2': '#',
        'blok_info_title': 'Пусть цифры говорят за нас.',                               #menu_info_main
        'blok_info_block_1_img': 'flaticon-worker display-3 text-primary', # flaticon
        'blok_info_block_1_num': '20+',
        'blok_info_block_1_title': 'Высококвалифицированные',
        'blok_info_block_1_subtitle': 'Сотрудники.',
        'blok_info_block_2_img': 'flaticon-planet-earth display-3 text-primary',  # flaticon
        'blok_info_block_2_num': '90+',
        'blok_info_block_2_title': 'Города',
        'blok_info_block_2_subtitle': 'по всей Беларуси.',
        'blok_info_block_3_img': 'flaticon-gears display-3 text-primary',  # flaticon
        'blok_info_block_3_num': '1000+',
        'blok_info_block_3_title': 'Готовых',
        'blok_info_block_3_subtitle': 'Проектов.',                                      #/menu_info_main
        'footer_copyright': 'Copyright © 2021 All Rights Reserved',              #footer
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
        'block_0_adres_subtitle_4': '',                      #/footer
        'main_title_specialty': 'Наша специализация',
        'main_subtitle_specialty': 'Подзаголовок о наших специальностях, Подзаголовок о наших специальностях, Подзаголовок о наших специальностях ',
        'block_speciality_id': int(2),     #
        'block_speciality_id_1': int(4),  #вывод первой новость ( id новости )
        'block_speciality_id_2': int(5),  #вывод второй новость ( id новости )
        'block_speciality_id_3': int(6),  #вывод третьей новость ( id новости )
        'block_speciality_id_4': int(7),  #вывод четвертой новость ( id новости )
        'block_news_id': int(2),  # вывод новости  ( id новости ) в блоке news
        'block_news_id_2': int(3),  # вывод новости  ( id новости ) в блоке news2

        'contact_us_text': 'Связяаться с нами!',
        'contact_us_urls': '/contact',
        'vidio_block_us': '<iframe width="560" height="315" src="https://www.youtube.com/embed/_7tsUmTsfwY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',

    }

    return render(request, 'main/index.html', data)

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return dict(list(context.items()))
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return dict(list(context.items()))
    def get_success_url(self):
        return reverse_lazy('index')

def logout_user(request):
    logout(request)
    return redirect('login')



