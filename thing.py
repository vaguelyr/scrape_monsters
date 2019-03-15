# vague
import time

from requests_html import HTMLSession
session = HTMLSession()
r = session.get('http://monstersvault.com/')
rand_page=list(r.html.find('#random-article')[0].links)[0]
print(rand_page)
r = session.get(rand_page)

# TODO Find a way to check if the element exists without using try/except and use it for each individual field

while True:
    print('==================================================================')
    print(rand_page)
  
    # some pages are inconsistent
    page_title = 'n/a'
    name = 'n/a' 
    author = 'n/a'
    origin = 'n/a'
    #rating_design = 'n/a'
    #rating_originality = 'n/a'
    #rating_survivability = 'n/a'
    #rating_fearfactor = 'n/a'
    #rating_vault = 'n/a'
    #rating_prefer_nightmares = 'n/a'
    #rating_burn_it = 'n/a'
    #rating_keep_one = 'n/a'
    #rating_love = 'n/a'
    #rating_what = 'n/a'

    rating_design = r.html.find('.number')[0].text
    rating_originality = r.html.find('.number')[1].text
    rating_survivability = r.html.find('.number')[2].text
    rating_fearfactor = r.html.find('.number')[3].text
    rating_vault = r.html.find('.number')[4].text
    rating_prefer_nightmares = r.html.find('.number')[5].text
    rating_burn_it = r.html.find('.number')[6].text
    rating_keep_one = r.html.find('.number')[7].text
    rating_love = r.html.find('.number')[8].text
    rating_what = r.html.find('.number')[9].text
    try:
        name=r.html.find('.detail-item')[0].text
        author=r.html.find('.detail-item')[1].text
        origin=r.html.find('.detail-item')[2].text
        page_title = r.html.find('.main-title')[0].text
    except:
        print(r.html.find('.detail-item'))
        pass

    print(page_title)
    print(name)
    print(author)
    print(origin)
    print(rating_design)
    print(rating_originality)
    print(rating_survivability)
    print(rating_fearfactor)
    print(rating_vault)
    print(rating_prefer_nightmares)
    print(rating_burn_it)
    print(rating_keep_one)
    print(rating_love)
    print(rating_what)
    

    rand_page=list(r.html.find('#random-article')[0].links)[0]
    r = session.get(rand_page)
    time.sleep(1)

