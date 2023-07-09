from .models import *

menu = [{'title': "Главная", 'url_name': 'index'},
        {'title': "Добавить отчет", 'url_name': 'add_report'},

]


class DataMixin:
    paginate_by = 20

    def get_user_context(self, **kwargs):
        context = kwargs

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu

        return context
