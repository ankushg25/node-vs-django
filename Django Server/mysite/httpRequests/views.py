from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from utils import query_debugger

@query_debugger
def get_request(request):
    user_list = User.objects.all().values()
    return HttpResponse('GET Request View.' + str(user_list))


def post_request(request):
    return HttpResponse('POST Request View.')