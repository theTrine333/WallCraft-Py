from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivymd.uix.imagelist import MDSmartTile
from kivy.properties import StringProperty
from api.api import *
from kivy.uix.image import AsyncImage
Window.size = (360,640)

from kivy.loader import Loader
Loader.num_workers = 2
class ImageCard(MDSmartTile):
    imageLink = StringProperty()
