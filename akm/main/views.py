from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

import main.mixdata
from about.models import *
from news.models import *
from .forms import *


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
    cat = News_category.objects.all()

    data = {
        'cat': cat,
        'news': news,
        'portfolio': portfolio,
        'category_portfolio': category_portfolio,
        # 'ids_news': '2',  # id for displaying the news on the main page
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
        'image_header': main.mixdata.data['image_header'],  # image us main
        'blok_info_title': main.mixdata.data['blok_info_title'],  # menu_info_main
        'blok_info_block_1_img': main.mixdata.data['blok_info_block_1_img'],  # flaticon
        'blok_info_block_1_num': main.mixdata.data['blok_info_block_1_num'],
        'blok_info_block_1_title': main.mixdata.data['blok_info_block_1_title'],
        'blok_info_block_1_subtitle': main.mixdata.data['blok_info_block_1_subtitle'],
        'blok_info_block_2_img': main.mixdata.data['blok_info_block_2_img'],  # flaticon
        'blok_info_block_2_num': main.mixdata.data['blok_info_block_2_num'],
        'blok_info_block_2_title': main.mixdata.data['blok_info_block_2_title'],
        'blok_info_block_2_subtitle': main.mixdata.data['blok_info_block_2_subtitle'],
        'blok_info_block_3_img': main.mixdata.data['blok_info_block_3_img'],  # flaticon
        'blok_info_block_3_num': main.mixdata.data['blok_info_block_3_num'],
        'blok_info_block_3_title': main.mixdata.data['blok_info_block_3_title'],
        'blok_info_block_3_subtitle': main.mixdata.data['blok_info_block_3_subtitle'],  # /menu_info_main
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
        'main_title_specialty': main.mixdata.data['main_title_specialty'],
        'main_subtitle_specialty': main.mixdata.data['main_subtitle_specialty'],
        'block_speciality_id': main.mixdata.data['block_speciality_id'],  #
        'block_speciality_id_1': main.mixdata.data['block_speciality_id_1'],  # вывод первой новость ( id новости )
        'block_speciality_id_2': main.mixdata.data['block_speciality_id_2'],  # вывод второй новость ( id новости )
        'block_speciality_id_3': main.mixdata.data['block_speciality_id_3'],  # вывод третьей новость ( id новости )
        'block_speciality_id_4': main.mixdata.data['block_speciality_id_4'],  # вывод четвертой новость ( id новости )
        'block_news_id': main.mixdata.data['block_news_id'],  # вывод новости  ( id новости ) в блоке news
        'block_news_id_2': main.mixdata.data['block_news_id_2'],  # вывод новости  ( id новости ) в блоке news2
        'contact_us_text': main.mixdata.data['contact_us_text'],
        'contact_us_urls': main.mixdata.data['contact_us_urls'],
        'vidio_block_us': main.mixdata.data['vidio_block_us'],

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
