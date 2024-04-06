from __inits import *
global screenMng
screenMng = ScreenManager()

#254 Club Party Hits(Nairobi Nights Groove) - DJ Meal-tone (Bien, Wakadinali, Lil Maina, Breeder LW)

class WallCraft(MDApp):
    tag = "light"
    @mainthread
    def showSpinner(self,state:bool):
        if state:
            self.spinner = SpinnerPopup()
            self.spinner.open()
        else:
            self.spinner.dismiss()
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = "Dark"
        screenMng.add_widget(Builder.load_file('Screens/main.kv'))
        return screenMng
    urlLinks = []
    @multitasking.task 
    def get_gallery(self,page: int):
        self.showSpinner(True)
        try:
            main_url = f"{url}/gallery/tag={self.tag}/{page}/"
            req = requests.get(main_url,stream=True)
            soup = BeautifulSoup(req.text,"html.parser")
            containers = soup.findAll("div", class_= "image-gallery__items image-gallery-items-container")
            imageLinks = []
            for container in containers:
                images = container.findAll("img")
                for image in images:
                    try: 
                        imageLinks.append(image['src']+"?h=180&r=0.5")
                    except:
                        continue
            req.close()
            self.load_gui(imageLinks)
            self.showSpinner(False)
        except Exception as E:
            self.showSpinner(False)
            print("An Error occured") 
    @multitasking.task 
    def get_more_gallery(self,page: int):
        self.showSpinner(True)
        try:
            main_url = f"{url}/gallery/tag={self.tag}/{page}/"
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
            self.urlLinks = imageLinks
            
            req.close()
            self.load_gui(imageLinks)
            self.showSpinner(False)
        except Exception as E:
            self.showSpinner(False) 
    def on_start(self):
        pass
        self.get_tag()
        self.links = self.get_gallery(1)
    @mainthread
    def load_gui(self,links):
        try:
            for link in links:
                imageCard = ImageCard()
                imageCard.imageLink = link
                screenMng.get_screen("main").ids.images_box.add_widget(imageCard)
        except Exception as E:
            pass
    @multitasking.task
    def load_more_images(self):
        try:
            random_page = random_page+1
            self.get_more_gallery(random_page)
        except:
            random_page = random.randrange(1,50)
            self.get_more_gallery(random_page)
    @multitasking.task
    def get_tag(self):
        #self.showSpinner(True)
        GalleryTags = []
        payLoad = {
            "pc":"", 
            "skip": 10,
            "limit": 50
        }
        post = requests.post(f"{url}/getTagGalleries",data=payLoad)
        req = requests.get(url)
        soup = BeautifulSoup(req.text,"html.parser")
        courasels = soup.findAll("div",class_ = "page-images-landing-carousel")
        for courasel in courasels:
            headings = courasel.find("h2").getText().strip()
            tag_url = courasel.find("img", class_ = "image-gallery-image__image")['src']
            GalleryTags.append([headings,tag_url+"?h=180&r=0.5"])
          
        req.close()   
        self.set_tags(GalleryTags)
        #self.showSpinner(False)
    @mainthread
    def set_tags(self,links):
        try:
            for link in links:
                imageCard = CarouselImage()
                imageCard.imageTag = link[0]
                imageCard.imageLink = link[1]
                screenMng.get_screen("main").ids.gallery_courasel.add_widget(imageCard)
        except:
            pass
    
if __name__ == '__main__':
    LabelBase.register(name="MPoppins",fn_regular="assets/fonts/Poppins-Medium.ttf")
    WallCraft().run()