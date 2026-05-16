from django.shortcuts import render
from .models import User, Media

# Завдання на 3 бали
def home(request):
    user = User(
        first_name='Іван', 
        last_name='Петренко', 
        description='Програміст'
    )
    context = {'user': user}
    return render(request, 'blog/home.html', context)

# Завдання на 4-5 балів
def media_detail(request):
    # Створюємо об'єкт медіа (наприклад, фільм або гра)
    my_media = Media(
        title='Inception',
        description='Науково-фантастичний трилер про подорожі у снах.',
        rating=9,
        studio_name='Warner Bros.'
    )
    context = {'media': my_media}
    return render(request, 'blog/media.html', context)