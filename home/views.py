from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def home(request):
    people = [
        {'name': 'Harsh', 'age': 22},
        {'name': 'Abhijeet', 'age': 26},
        {'name': 'Praveen', 'age': 31},
        {'name': 'Himan', 'age': 15}
    ]

    text = ("Lorem ipsum dolor sit amet, consectetur adipisicing elit. Beatae in nisi perferendis placeat provident "
            "sequi voluptatibus? Atque deserunt dolorem, dolores eveniet id in maiores, natus, officia quis repellat "
            "voluptate voluptatem.")

    games = ["Valorant", "mlbb", "football", "cricket"]
    page = 'DJANGO BEGINNER'
    return render(request, "home/index.html", context={'page': page, 'people': people, 'text': text, 'games': games})


def about(request):
    context = {'page': 'About'}
    return render(request, "home/about.html", context)


def contact(request):
    context = {'page': 'Contact'}
    return render(request, "home/contact.html", context)


def success_page(request):
    print('*' * 10)
    return HttpResponse("<h1 style='color:red'> Hey This is a success page.</h1>")
