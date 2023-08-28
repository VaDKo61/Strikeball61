from django.shortcuts import render


def description(request):
    return render(request, 'title_list/index.html')
