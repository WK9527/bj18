from django.http import HttpResponse
from django.shortcus import redirecct


def index(request):
    return HttpResponse("ok")
print('你好')
