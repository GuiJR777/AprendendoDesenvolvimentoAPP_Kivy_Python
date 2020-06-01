#Linhas 2 a 5 são pra correção de um bug de opengll
from kivy import Config
Config.set('graphics', 'multisamples', '0')
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

#Imports
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

#Montador Kivy
class Incrementador (BoxLayout):
    pass

class Test(App):
    def build(self):
        return Incrementador()

Test().run()