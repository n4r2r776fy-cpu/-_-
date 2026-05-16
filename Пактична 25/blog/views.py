from django.shortcuts import render
from .models import Media

def media_by_index(request, index):
    all_media = Media.objects.all()
    try:
        # Беремо об'єкт за індексом зі списку всіх медіа
        current_media = all_media[int(index)]
    except (IndexError, ValueError):
        return render(request, 'blog/404.html', status=404)

    return render(request, 'blog/media_detail.html', {'media': current_media})