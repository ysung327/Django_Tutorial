from django.http import HttpResponse
from .models import Album
from django.template import loader

def index(request):
    all_albums = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {
        'all_albums': all_albums,
    }

    #below code is what we have to avoid.
    '''
    html = ''
    for album in all_albums:
        url = '/music/' +str(album.id) + '/'
        html += '<a href="' + url + '">' + album.album_title + '</a><br>'
    '''
    return HttpResponse(template.render(context, request))

def detail(request, album_id):
    return HttpResponse("<h2> Details for Album id : " + str(album_id) + "</h2>")

