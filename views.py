from django.shortcuts import render


def index(request):
    return render(request, 'mainApp/homePage.html')

def contact(request):
    return render(request, 'mainApp/basic.html', {'values': ['Если у вас остались вопросы, то задавайте их по телефону','000-000-00',
                                                             'example@mail.ru']})


