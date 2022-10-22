from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic


def index(request):
    #return HttpResponse("Hello, world. You're at the tsp index.")
    return render(request, 'tsp/index.html')


class TitleView(generic.TemplateView):
    template_name = 'tsp/title.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_str'] = "TSPのタイトル"
        return context

