#this is my project

from kivymd.app import  MDApp
from kivy.lang import Builder

from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog

Window.size = (500, 600)

helper = """
MDScreen: 
    MDNavigationLayout: 
        MDScreenManager: 
            MDScreen: 
                MDTopAppBar: 
                    title: "menu"
                    left_action_items: [["menu", lambda x:nav_dawer.set_state("open")]]
                    pos_hint: {"top": 1}
                    
                    elevation: 1290
                Widget: 
                
                MDLabel: 
                    text:  "welcome to meter app"  
                    pos_hint: {'center_x':0.8, 'center_y': 0.8}   
                    
                MDTextField:
                    hint_text: "sign in" 
                    helper_text: "click here"
                    pos_hint: {'center_x':0.5, 'center_y': 0.5}
                    helper_text_mode: "persistent"
                    icon_right: "android"
                    size_hint_x: None
                    width: 300     
                    
                MDRectangleFlatButton:
                    text: "enter"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.2} 
                    on_release:self.ent    
                    
                   
                    
    MDNavigationDrawer: 
        id: nav_dawer



"""


class meterapp(MDApp):
    def build(self):
        screen = Builder.load_string( helper)
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Dark"

        return screen

    def ent(self, obj):
        dialog = MDDialog(title="welcome Amigo", text= " welcome")
        dialog.open()

meterapp().run()