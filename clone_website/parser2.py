import bs4 as bs
import urllib.request
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "clone_website.settings")
import django
django.setup()

from rental.models import Art, Artist


#defining fuction which extract photos url into dict.
def extract_url():
    with open('clone_website/static/pickart_rental.html') as fp:
        soup = bs.BeautifulSoup(fp, 'lxml')
    url_divs = soup.find_all("div", class_="secondThumbnail")
    #print(url_divs)
    urls = []
    for url_div in url_divs:
        url_ = bs.BeautifulSoup(str(url_div), 'html5lib')
        tag = url_.div
        url_onclick = tag['onclick']
        url_onclick = url_onclick.replace("location.href = '", "").replace("'", "")
        #print(url_onclick)
        if not urls:
            urls = [str(url_onclick)]
        else:
            urls.append(str(url_onclick))
    #print(urls)
    return urls


def extract_detail():
    hrefs = extract_url()
    views =[[]]
    artists=[]
    art_title = []
    size = []
    media = []
    frame = []
    edition = []
    detail = []
    i = 0
    cnt = 0

    for href in hrefs:
        sauce = urllib.request.urlopen('https://pickart.co.kr/{}'.format(href)).read()
        soup = bs.BeautifulSoup(sauce, 'lxml')
        para = soup.find_all('span', attrs={"style": "font-weight:normal;"})
        #print(para)

        #art_title
        if not art_title:
            art_title = [para[0].text]
        else:
            art_title.append(para[0].text)

        #size
        if not size:
            size = [para[2].text]
        else:
            size.append(para[2].text)

        #media
        if not media:
            media = [para[3].text]
        else:
            media.append(para[3].text)

        #frame
        if not frame:
            frame = [para[4].text]
        else:
            frame.append(para[4].text)

        # edition
        if not edition:
            edition = [para[5].text]
        else:
            edition.append(para[5].text)

        # artist
        if not artists:
            artists = [para[1].text]
        else:
            artists.append(para[1].text)


        print(para[0].text)
        print(len(art_title))

        #detail
        para = soup.find_all('p', attrs={"style": "text-align:justify"})
        if not detail:
            detail = [para[1].text]
        else:
            detail.append(para[1].text)


         # views
        view = extract_view(href)
        if cnt == 0:
            views[0] = view
        else:
            views.append(view)
        cnt = cnt + 1

    # print(artists)
    for artist in artists:
        try:
            obj = Artist.objects.get(name_eng=artist)
        except Artist.DoesNotExist:
            obj = Artist(name_eng=artist)
            obj.save()
        artists[i] = obj
        i = i + 1

    print(views)
    dict = {'artist': artists, 'art_title': art_title, 'size': size, 'media': media, 'frame': frame, 'edition': edition, 'detail': detail, 'view': views}
    print(dict)
    return dict



def extract_view(href):

    views = []

    sauce = urllib.request.urlopen('https://pickart.co.kr/{}'.format(href)).read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    paras = soup.find_all('p', attrs={"style": "text-align:center"})
    #print(paras)

    for para in paras:
        para = bs.BeautifulSoup(str(para), 'lxml')
        if para.img != None:
            if not views:
                views = [para.img['src']]
            else:
                views.append(para.img['src'])
    print(views)

    try:
        del views[views.index('https://contents.sixshop.com/thumbnails/uploadedFiles/34398/product/image_1520934322840_1000.png')]
        del views[views.index('https://contents.sixshop.com/thumbnails/uploadedFiles/34398/product/image_1520923180099_1000.jpg')]
    except ValueError:
        pass

    print(views)
    return(views)


#main
if __name__=='__main__':
    dict = {}
    dict = extract_detail()
    for t in range(len(dict['art_title'])):
        Art(artist=dict['artist'][t], art_title=dict['art_title'][t], size=dict['size'][t],
               media=dict['media'][t], frame=dict['frame'][t],
               edition=dict['edition'][t], detail=dict['detail'][t], view=dict['view'][t]).save()

