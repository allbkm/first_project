import os
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    context = {
        'pages': [
            {'url': '/current_time/', 'name': 'Текущее время'},
            {'url': '/workdir/', 'name': 'Содержимое рабочей директории'},
        ]
    }
    return render(request, 'home.html', context)

def current_time_view(request):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return HttpResponse(f'Текущее время: {current_time}')

def workdir_view(request):
    files = os.listdir('.')
    files_list = '<br>'.join(files)
    return HttpResponse(f'Файлы в рабочей директории:<br>{files_list}')
