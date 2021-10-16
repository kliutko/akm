


from django.views.generic import ListView, UpdateView

from .models import *
from .forms import *





# Create your views here.
# def send_telegram(text: str):
#     token = '2018618673:AAFeAMB9pYqGNAOZpwhd57MsYvtSe_byLWQ'
#     url = 'https://api.telegram.org/bot'
#     channel_id = '-586479976'
#     url += token
#     method = url + '/sendmessage'
#
#     r = requests.post(method, data={
#         'chat_id': channel_id,
#         'text': text,
#     })
#     if r.status_code != 200:
#         raise Exception('Post_text_error')
#
#
# if __name__ == '__main__':
#     send_telegram('hello world')

class Account(ListView):
    model = Profile.objects.filter()
    template_name = 'account/profile.html'
    context_object_name = 'acc'
    # allow_empty = False

    def get_context_data(self, *, object_list=None, obj=None, **kwargs):

        context = super().get_context_data(**kwargs)
        context['name_site'] = 'АКМ'

        return context

    def get_queryset(self):
        return Profile.objects.all()

class AccountsUpdate(UpdateView):

    form_class = ProfileForm
    template_name = 'account/profile_update.html'
    context_object_name = 'update'
    success_url = 'updates'


    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        # save cleaned post data
        clean = form.cleaned_data
        context = {}
        self.object = context.save(clean)
        return super(AccountsUpdate, self).form_valid(form)

    def get_context_data(self, *, object_list=None, obj=None, **kwargs):

        context = super().get_context_data(**kwargs)
        context['name_site'] = 'АКМ'

        return context



    # data = {
    #     'entityform': entityform,
    #     'subjectform': subjectform,
    #     'serviceform': serviceform,
    #     'error_form': error_form,
    #     'role': role,
    #     'profile': profile,
    #     'entity': entity,
    #     'subject': subject,
    #     'service': service,
    #     'name_site': 'Название сайта',
    #     'email_header': 'Почта',
    #     'phoneheader': 'Телефон',
    #     'fb_url': 'Ссылка на facebook',
    #     'tw_url': 'Ссылка на twitter',
    #     'ld_url': 'Ссылка на linkedin',
    #     'inst_url': 'Ссылка на instagram',
    #     'title_main': 'Специальная технология',  # title in string main
    #     'subtitle_main': 'Обработки металла',  # subtitle us string main
    #     'image_header': '/static/images/hero_bg_2.jpg',  # image us main
    #     'text_button_1': 'Download',
    #     'link_button_1': '#',
    #     'text_button_2': 'GetInTouch',
    #     'link_button_2': '#',
    #     'footer_copyright': 'Copyright © 2021 All Rights Reserved',  # footer
    #     'blok_adress_title': 'Беларусь, Брестская область',
    #     'block_adres_subtitle': 'Кобринский р-н, д. Пески-2',
    #     'block_adres_subtitle_1': ' ул.Луговая 26',
    #     'block_adres_subtitle_2': 'Tel. + 375(29) 112-76-32',
    #     'block_adres_subtitle_3': 'tests@tests.com',
    #     'block_adres_subtitle_4': 'УНП: 291052118',
    #     'blok_0_adress_title': '',
    #     'block_0_adres_subtitle': '',
    #     'block_0_adres_subtitle_1': '',
    #     'block_0_adres_subtitle_2': '',
    #     'block_0_adres_subtitle_3': '',
    #     'block_0_adres_subtitle_4': '',  # /footer
    #
    # }


    # return render(request, 'account/profile.html', data)
