from api.__inits import *

global screenMng
screenMng = ScreenManager()

class WallCraft(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = "Dark"
        
        screenMng.add_widget(Builder.load_file('Screens/main.kv'))
        
        return screenMng
        
    def on_start(self):
        links = get_gallery(1)
        for link in links[:24]:
            imageCard = ImageCard()
            imageCard.imageLink = link
            screenMng.get_screen("main").ids.images_box.add_widget(imageCard)
if __name__ == '__main__':
    LabelBase.register(name="MPoppins",fn_regular="assets/fonts/Poppins-Medium.ttf")
    WallCraft().run()