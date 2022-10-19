from django.views import generic


class TitleView(generic.TemplateView):
    template_name = 'tsp/title.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_str'] = "TSPのタイトル"
        return context