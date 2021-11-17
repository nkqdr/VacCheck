from kivymd.app import MDApp
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.core.window import Window
import cv2

Window.size = (400, 650) # For development only. This simulates a horizontal screen size.

screen_helper = """
<ContentCustomSheet@BoxLayout>:
    orientation: "vertical"
    size_hint_y: None
    height: "400dp"
    MDLabel:
        text: 'Kamera hier einfügen'
        halign: 'center'
    



Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'VacCheck'
                        left_action_items: [["menu", lambda x: app.navigation_draw(nav_drawer)]]
                        elevation: 10
                    MDLabel:
                        text: 'Hello World!'
                        halign: 'center'
                    MDBottomAppBar:
                        MDToolbar:
                            mode: 'center'
                            type: 'bottom'
                            icon: 'camera'
                            on_action_button: app.action_button()
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                padding: '8dp'
                spacing: '8dp'
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Einstellungen'
                            IconLeftWidget:
                                icon: 'cog-outline'
                        OneLineIconListItem:
                            text: 'Hilfe'
                            IconLeftWidget:
                                icon: 'help-circle-outline'
"""
                # MDLabel:
                #     text: 'Einstellungen'
                #     font_style: 'Subtitle1'
                #     size_hint_y: None
                #     height: self.texture_size[1]
                # MDLabel:
                #     text: 'Hilfe'
                #     font_style: 'Subtitle1'
                #     size_hint_y: None
                #     height: self.texture_size[1]

class VacCheckApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Red'
        screen = Builder.load_string(screen_helper)
        return screen

    def navigation_draw(self, nav_drawer):
        """
        Event handler for when the user taps on the menu icon button.
        """
        nav_drawer.set_state('toggle')
        print("Navigation")

    def action_button(self):
        """
        Event handler for when the user taps on the camera icon button.
        """
        print("Action Button pressed")
        # bottom_sheet = MDBottomSheet(radius_from="top", animation=True, duration_opening = 0.5)
        # sheet_content = MDLabel(text="Kamera hier einfügen...")
        # bottom_sheet.add_widget(sheet_content)
        bottom_sheet = MDCustomBottomSheet(screen=Factory.ContentCustomSheet(), radius_from="top", animation=True)
        bottom_sheet.open()

if __name__ == '__main__':
    VacCheckApp().run()