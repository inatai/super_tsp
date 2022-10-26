from django.views import generic
from django.http import HttpResponse
# application/write_data.pyをインポートする
from .application import write_data


class TitleView(generic.TemplateView):
    template_name = 'tsp/title.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_str'] = "TSPのタイトル"
        return context
    

def call_write_data(req):
       if req.method == 'GET':
        # write_data.pyのwrite_csv()メソッドを呼び出す。
        # ajaxで送信したデータのうち"input_data"を指定して取得する。
        write_data.write_csv(req.GET.get("input_data"))
        return HttpResponse()