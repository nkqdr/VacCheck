from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.navigationdrawer import MDNavigationDrawer, MDNavigationLayout
from kivymd.uix.toolbar import MDToolbar
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.list import MDList, OneLineIconListItem, IconLeftWidget
from kivy.uix.scrollview import ScrollView
from kivy_garden.xcamera import XCamera
from kivy.uix.camera import Camera
from kivy.lang import Builder
from kivy.factory import Factory
from helper.main_screen_helper import screen_helper
from kivy.core.window import Window

#Window.size = (400, 650) # For development only. This simulates a horizontal screen size.

Builder.load_string("""
<MyCamera>:
    id:qrcodecam
    canvas.before:
        PushMatrix
        Rotate:
            angle: -90
            origin: self.center
    canvas.after:
        PopMatrix
""")

class MyCamera(Camera):
    pass


class VacCheckApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Red'
        screen = MDNavigationLayout()
        self.drawer = MDNavigationDrawer()
        drawer_layout = BoxLayout()
        drawer_layout.orientation = "vertical"
        drawer_layout.padding = '8dp'
        drawer_layout.spacing = '8dp'
        drawer_scroll_view = ScrollView()
        drawer_item_list = MDList()
        settings_item = OneLineIconListItem(text="Einstellungen")
        settings_item.add_widget(IconLeftWidget(icon='cog-outline'))
        drawer_item_list.add_widget(settings_item)
        help_item = OneLineIconListItem(text="Hilfe")
        help_item.add_widget(IconLeftWidget(icon="help-circle-outline"))
        drawer_item_list.add_widget(help_item)
        drawer_scroll_view.add_widget(drawer_item_list)
        drawer_layout.add_widget(drawer_scroll_view)
        self.drawer.add_widget(drawer_layout)
        self.screenmanager = ScreenManager()
        main_screen = Screen()
        screen_layout = BoxLayout()
        screen_layout.orientation = 'vertical'
        self.toolbar = MDToolbar(elevation=10, title="VacCheck")
        self.toolbar.left_action_items = [["menu", lambda x: self.navigation_draw()]]
        screen_layout.add_widget(self.toolbar)
        self.camera = MyCamera()
        screen_layout.add_widget(self.camera)
        main_screen.add_widget(screen_layout)
        self.screenmanager.add_widget(main_screen)
        screen.add_widget(self.screenmanager)
        screen.add_widget(self.drawer)
        return screen

    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        # camera = self.ids['camera']
        # timestr = time.strftime("%Y%m%d_%H%M%S")
        # camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")

    def navigation_draw(self):
        """
        Event handler for when the user taps on the menu icon button.
        """
        self.drawer.set_state('toggle')
        print("Navigation")

if __name__ == '__main__':
    VacCheckApp().run()