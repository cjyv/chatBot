from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Contact
from django.urls import reverse
from django.http import HttpResponse # 追記
from chatterbot import ChatBot # 追記
from chatterbot.ext.django_chatterbot import settings # 追記
from django.views.generic.base import TemplateView # 追記
from django.views.generic import View # 追記
# 
# views.py(ロジックを作る,controller)
# Create your views here.
def index(request):

 return render(request,'index.html')

def goChatBot(request):
    return render(request,'chatBot.html')

def ContactInsert(request):
    
    c = Contact(name=request.POST['name'],email=request.POST['email'],phone=request.POST['phone'],comment=request.POST['comment'])
    c.save()
    return render(request,'index.html')

class Home(TemplateView):
    template_name = 'sample_bot/home.html'


class BotResponse(View):
    chatbot = ChatBot(**settings.CHATTERBOT)

    def post(self, request, *args, **kwargs):
        input_data = request.POST.get('input_text')
        if not input_data:
            return HttpResponse('<h2>空のデータを受け取りました。</h2>', status=400)
        bot_response = self.chatbot.get_response(input_data)
        http_response = HttpResponse()
        http_response.write('{} => {}'.format(self.chatbot.name, bot_response,))
        return http_response

    def get(self, request, *args, **kwargs):
        return HttpResponse(self.chatbot.name)