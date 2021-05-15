from .models import Team  # models.py의 Blog 테이블를 가져오자
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def home(request):
    blogs = Team.objects.all()  # Blog 테이블에 있는 오브젝트 모두를 불러오기.
    # home.html 과 함께 blogs를 보내준다.
    return render(request, 'home.html', {'blogs': blogs})
