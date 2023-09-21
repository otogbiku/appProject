from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager


from kivymd.app import MDApp
from kivy.core.window import Window

from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton


Window.size = (400, 600)






kv = '''
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




MDNavigationLayout:

    MDScreenManager:

        MDScreen:

            MDTopAppBar:
                title: "METER NAVIGATION"
                elevation: 10
                pos_hint: {"top": 1}
                md_bg_color: "#e7e4c0"
                specific_text_color: "#4a4939"
                left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                
            MDTextField: 
                hint_text: "have an account"
                helper_text: "is optional"
                icon_right: "gmail"
                helper_text_mode: "persistent"
                pos_hint: {"center_x": 0.5, "center_y": 0.5}
                size_hint_x: None 
                width: 300
                
                
            
                
                

    MDNavigationDrawer:
        id: nav_drawer
        radius: (0, 16, 16, 0)

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
                right_text:
                text_right_color: "#4a4939"
                text: "MTU"
                id: mtu_screen

            DrawerClickableItem:
                icon: "send"
                text: "INFRASTRUCTURE "
                id: infra_screen
                
                
            DrawerClickableItem:
                icon: "send"
                right_text: "pass"
                text_right_color: "#4a4939"
                text: "LONG GOODS"
                id: long_screen

            DrawerClickableItem:
                icon: "send"
                text: "SHORT GOODS "
                on_release: app.button_click()
                id: short_screen

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

dia = '''
MDFloatLayout:

    MDRectangleFlatButton:
        text: "ALERT DIALOG"
        pos_hint: {'center_x': .5, 'center_y': 0.3}
        on_release: app.show_alert_dialog()
'''

class engineering(MDApp):
    dialog = None
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.primary_hue = "300"


        screen = MDScreen()
        man = Builder.load_string(kv)
        woman = Builder.load_string(dia)


        screen.add_widget(man)
        screen.add_widget(woman)



        return screen

    def button_click(self):

        button = self.root.ids.short_screen
        button.text = "short good button clicked"


    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Welcome",
                text="Discard draft?",
                buttons=[
                    MDRectangleFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                    MDRectangleFlatButton(
                        text="DISCARD",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                ],
            )
        self.dialog.open()












engineering().run()