from django.shortcuts import render
from django.views import View

from django.http.response import JsonResponse
from django.template.loader import render_to_string

from .models import Topic
from .forms import TopicForm

class BbsView(View):

    def get(self, request, *args, **kwargs):

        topics  = Topic.objects.all()
        context = { "topics":topics }

        return render(request,"posting/index.html",context)

    def post(self, request, *args, **kwargs):

        json    = { "error":True }
        form    = TopicForm(request.POST)

        if not form.is_valid():
            print("Validation Error")
            return JsonResponse(json)

        form.save()
        json["error"]   = False

        topics          = Topic.objects.all()
        context         = { "topics":topics }
        content         = render_to_string("posting/content.html",context,request)

        json["content"] = content

        return JsonResponse(json)

index   = BbsView.as_view()