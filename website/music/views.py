from django.http import HttpResponse
from django.http import Http404
from .models import Album
from django.template import loader
from django.shortcuts import render

def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums,}

    #below code is what we have to avoid.
    '''
    html = ''
    for album in all_albums:
        url = '/music/' +str(album.id) + '/'
        html += '<a href="' + url + '">' + album.album_title + '</a><br>'
    '''

    return render(request, 'music/index.html', context)


def detail(request, album_id):
    template = loader.get_template('music/detail.html')
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request, 'music/detail.html', {'album': album})
