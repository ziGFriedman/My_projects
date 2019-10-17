import requests
import os

# url = 'https://www.hdwallpapers.in/download/metal_abstract-HD.jpg'
#
# r = requests.get(url, stream=True)    # stream разделить содержимое на куски и закачивает кусками
#
# with open('Parser_img/1.jpg', 'wb') as f:
#     for chunk in r.iter_content(8192):    # указываем сколько байтов будет каждая часть
#         f.write(chunk)

urls = [
        'https://www.hdwallpapers.in/download/metal_abstract-HD.jpg',
        'https://www.hdwallpapers.in/thumbs/2019/ancient_castle_in_winter_snow_4k-t2.jpg',
        'https://www.hdwallpapers.in/thumbs/2019/spring_anime_girl-t2.jpg',
        'https://www.hdwallpapers.in/thumbs/2019/marshmello_american_dj_live_5k-t2.jpg',
        'https://www.hdwallpapers.in/thumbs/2019/horsehead_nebula_radiance_4k-t2.jpg'
]

def get_file(url):
    r = requests.get(url, stream=True)
    return r

def get_name(url):
    # https://www.hdwallpapers.in/download/metal_abstract-HD.jpg
    # name: metal_abstract-HD.jpg
    name = url.split('/')[-1]
    # metal_abstract-HD
    folder = name.split('.')[0]

    if not os.path.exists(folder):
        os.makedirs(folder)

    path = os.path.abspath(folder)

    return path + '\\' + name

def save_img(name, file_object):
    with open(name, 'wb') as f:
        for chunk in file_object.iter_content(8192):
            f.write(chunk)

def main():
    for url in urls:
        save_img(get_name(url), get_file(url))

if __name__ == '__main__':
    main()
