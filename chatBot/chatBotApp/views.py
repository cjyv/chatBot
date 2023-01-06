from django.shortcuts import render


# 
# views.py(ロジックを作る,controller)
# Create your views here.
def index(request):
 return render(request,'index.html')

def goChatBot(request):
    return render(request,'chatBot.html')