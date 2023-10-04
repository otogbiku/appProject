from kivy.lang import Builder
from kivy.properties import ObjectProperty

import sqlite3

from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView
from kivy.core.window import Window
from kivy .properties import StringProperty

Window.size = (300, 600)



import sqlite3

# Create or open a database file
conn = sqlite3.connect("myapp.db")

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table to store your data (e.g., a table for user inputs)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        value TEXT
    )
''')

KV = '''
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "#e7e4c0"
    text_color: "#4a4939"
    icon_color: "#4a4939"
    ripple_color: "#c5bdd2"
    selected_color: "#0c6c4d"


<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: "#4a4939"
    icon_color: "#4a4939"
    focus_behavior: False
    selected_color: "#4a4939"
    _no_ripple_effect: True

MDScreen:

    MDTopAppBar:
        pos_hint: {"top": 1}
        text: "love this" 
        elevation: 10
        title: "Navigate to Meter "
        font_title: 10
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    MDNavigationLayout:

        MDScreenManager:
            id: screen_manager
            
            MDScreen:
                name: "scr 1"
                MDLabel:
                    text: " MAIN TRANSMISSION UNIT "
                    pos_hint: {"center_x": 0.9, "center_y": 0.8} 
                    font_size: 20 
                    size_hint_x: None 
                    width: 500 
                    
                    MDBoxLayout:
                        orientation: "vertical"
                        ScrollView:
                    
                            
                                
                        MDTextField: 
                            id: text_input
                            hint_text: "Enter your Value"
                            
                       
                            
                        MDRaisedButton: 
                            text: "save"
                            on_release: app.save_value() 
                            pos_hint:{"center_x": 0.5, "center_y": 0.5}
                        
                    
                
                    
                                
                
                          
                
                
   

            MDScreen:
                name: "scr 2"
                MDLabel:
                    text: " INFRASTRUCTURE  "
                    pos_hint: {"center_x": 1, "center_y": 0.8} 
                    font_size: 20 
                    size_hint_x: None 
                    width: 500
                
                    
            MDScreen:
                name: "scr 3"
                MDLabel:
                    text: " LONG GOODS  "
                    pos_hint: {"center_x": 1.1, "center_y": 0.8} 
                    font_size: 20
                    size_hint_x: None 
                    width: 500 
                    
                MDRectangleFlatButton:
                    text: "LINE 1"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    
                    
                MDRectangleFlatButton:
                    text: "LINE 2"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                
                    
            MDScreen: 
                name: "scr 4"
                MDLabel: 
                    text: " SHORT GOODS "
                    pos_hint: {"center_x": 1.1, "center_y": 0.8} 
                    font_size: 20 
                    size_hint_x: None
                    width: 500 
                    
                MDRectangleFlatButton:
                    text: "LINE 1"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                MDRectangleFlatButton:
                    text: "LINE 2"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                
                    
                
                    
                
                 
                
                    

        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 5, 5, 0)

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
                
                
<ContentNavigationDrawer>

    MDList:
        MDNavigationDrawerMenu:

        MDNavigationDrawerHeader:
            title: "HELLO"
            title_color: "#4a4939"
            text: "ENGINEERING METER READING"
            spacing: "4dp"
            padding: "12dp", 0, 0, "56dp"
        
        MDNavigationDrawerLabel:
            text: "METER OPTIONS "

        
        
        
        DrawerClickableItem:
            icon: "send"
            text_right: "hello"
            text: "MTU"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 1"
            
                    
            
            

        
        DrawerClickableItem:
            icon: "send"
            text: "INFRASTRUCTURE "
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 2"
        
        
        DrawerClickableItem:
            icon: "send"
            text: "LONG GOODS "
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 3" 
                
        
        DrawerClickableItem: 
            icon: "send"
            text: "SHORT GOODS" 
            on_press: 
                root.nav_drawer.set_state("close") 
                root.screen_manager.current = "scr 4" 
        
        MDNavigationDrawerDivider:

            MDNavigationDrawerLabel:
                text: "Labels"

            DrawerLabelItem:
                icon: "information-outline"
                text: "Label"

            DrawerLabelItem:
                icon: "information-outline"
                text: "Label"             
            

'''


class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class meter(MDApp):
    display_value = StringProperty("")


    def build(self):

        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.material_style = "M2"
        return Builder.load_string(KV)

    def save_value(self):
        value = self.root.ids.text_input.text
        if value:
            self.insert_data(value)
            self.root.ids.text_input.text = ""
            self.update_display()

    def insert_data(self, value):
        conn = sqlite3.connect("myapp.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO user_data (value) VALUES (?)", (value,))
        conn.commit()
        conn.close()

    def update_display(self):
        conn = sqlite3.connect("myapp.db")
        cursor = conn.cursor()
        cursor.execute("SELECT value FROM user_data")
        data = cursor.fetchall()
        conn.close()
        self.display_value = "\n".join([str(item[0]) for item in data])




meter().run()