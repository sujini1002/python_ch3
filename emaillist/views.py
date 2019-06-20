from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from emaillist.models import Emaillist


def index(request):
    # id 칼럼을 거꾸로 정렬하여 리스트 출력
    emaillist = Emaillist.objects.all().order_by('-id')
    data = {'emaillist':emaillist}

    return render(request, 'emaillist/index.html',data)

def form(request):
    return render(request, 'emaillist/form.html')

def add(request):
    # 영속성 : DB와 연결된 객체
    emaillist = Emaillist()

    emaillist.first_name = request.POST['fn']
    emaillist.last_name = request.POST['ln']
    emaillist.email = request.POST['email']

    # 자동으로 insert 된다.
    emaillist.save()
    return HttpResponseRedirect('/emaillist')