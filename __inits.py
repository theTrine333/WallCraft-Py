from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.gridlayout import MDGridLayout
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.clock import *
from kivymd.uix.imagelist import MDSmartTile
from kivy.properties import StringProperty
from kivy.uix.image import AsyncImage
from kivy.uix.modalview import ModalView
import multitasking,requests,random
from bs4 import BeautifulSoup

Window.size = (360,640)

from kivy.loader import Loader
initialSize = 24
maxSize = 72
page = 1

url = "https://wallpaper.mob.org"
#Loader.num_workers = 5
#Loader.max_upload_per_frame = 1
Loader.loading_image = 'assets/giphy.gif'
class ImageCard(MDSmartTile):
    imageLink = StringProperty()
    
class SpinnerPopup(ModalView):
    pass

class CarouselImage(MDSmartTile):
    imageLink = StringProperty()
    imageTag = StringProperty()