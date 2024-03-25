import requests
from bs4 import BeautifulSoup

def get_gallery(page: int):
    try:
        main_url = f"https://wallpaper.mob.org/gallery/tag=dark/{page}/"
        req = requests.get(main_url)
        soup = BeautifulSoup(req.text,"html.parser")
    
        containers = soup.findAll("div", class_= "image-gallery__items image-gallery-items-container")
        imageLinks = []
        for container in containers:
            images = container.findAll("img")
            for image in images:
                try: 
                    imageLinks.append(image['src'])
                except:
                    continue
        return imageLinks
    except Exception as E:
        print(f"Error: {E}")