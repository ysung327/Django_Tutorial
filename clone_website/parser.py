import bs4 as bs
import urllib.request
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "clone_website.settings")
import django
django.setup()

from rental.models import Artist


#defining fuction which extract photos url into dict.
def extract_photo():
    sauce = urllib.request.urlopen('https://pickart.co.kr/artists').read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    photo_divs = soup.find_all("div", class_="galleryThumbnailContent")
    #print(photo_divs)
    urls = []
    for photo_div in photo_divs:
        photo_ = bs.BeautifulSoup(str(photo_div), 'html5lib')
        tag = photo_.div
        photo_style = tag['style']
        #print(photo_style)
        photo_url = photo_style.replace('background-image: url("', '')
        photo_url = photo_url.replace('");', '')
        if not urls:
            urls = [str(photo_url)]
        else:
            urls.append(str(photo_url))
    del urls[14]
    del urls[22]
    #print(len(urls))
    return urls


def extract_href():
    with open('clone_website/static/pickart_artists.html') as fp:
        soup = bs.BeautifulSoup(fp, 'lxml')
    #print(soup)
    as_ = soup.find_all(class_="gallery_img_a", href=True)
    href = []
    for a_ in as_:
        element = bs.BeautifulSoup(str(a_), 'html5lib')
        tag = element.a
        #print(tag)
        artists_href = tag['href']
        if not href:
            href = [str(artists_href)]
        else:
            href.append(str(artists_href))
    href.remove("https://pickart.co.kr/simmanki")
    href.remove("https://pickart.co.kr/shinjapark333")
    #print(len(href))
    return href


def extract_detail():
    hrefs = extract_href()
    name_engs = []
    name_kors = []
    titles = []
    details = []

    for href in hrefs:
        sauce = urllib.request.urlopen(href).read()
        soup = bs.BeautifulSoup(sauce, 'lxml')
        para = soup.find_all("p")

        #titles
        if not titles:
            titles = [para[1].text]
        else:
            titles.append(para[1].text)

        #name_engs
        if not name_engs:
            name_engs = [para[2].text]
        else:
            name_engs.append(para[2].text)

        #name_kors
        if not name_kors:
            name_kors = [para[3].text]
        else:
            name_kors.append(para[3].text)

        #details
        if not details:
            details = [para[4].text]
        else:
            details.append(para[4].text)
        print(para[2].text)
        print(len(name_kors))

    #print(len(details))
    dict = {'title': titles, 'name_eng': name_engs, 'name_kor': name_kors, 'detail': details}
    return dict


#print(dict)

if __name__=='__main__':
    dict = {}
    dict = extract_detail()
    dict['photo'] = extract_photo()

    for t in range(len(dict['name_eng'])):
        Artist(name_eng=dict['name_eng'][t], name_kor=dict['name_kor'][t],
               artist_photo=dict['photo'][t], title=dict['title'][t],
               detail=dict['detail'][t]).save()


