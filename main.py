#Linhas 2 a 5 são pra correção de um bug de opengll
from kivy import Config
Config.set('graphics', 'multisamples', '0')
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

#Imports
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

#Classe que constroi a tela
class Test(App): #A declaração antes de app é o nome da window
    def build(self):
        #Montagem de Botões e Widgets
        box = BoxLayout(orientation= 'vertical')
        button = Button(text= 'Botão 1', font_size= 30, 
        on_release= self.incrementar)
        self.label= Label(text= '1', font_size= 30)
        box.add_widget(self.label)
        box.add_widget (button)

        
        #Montagem da Tela Completa
        
        return box

    def incrementar(self,button):
        button.text= 'soltei'
        self.label.text= str(int(self.label.text)+1)


#Invocar Tela
Test().run()