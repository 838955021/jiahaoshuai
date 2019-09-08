from django.http import HttpResponse

def index(request):
    return HttpResponse('hello world')
def about(request):
    return HttpResponse('吕大秃，你好，我是黄大秃')
def put(requeset):
    return  HttpResponse('抓')
