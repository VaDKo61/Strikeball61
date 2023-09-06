from django.shortcuts import render


def main_page(request):
    return render(request, 'title_list/index.html')
