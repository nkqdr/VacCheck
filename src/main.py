from kivymd.app import MDApp
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.core.window import Window
from helper.main_screen_helper import screen_helper
import cv2

Window.size = (400, 650) # For development only. This simulates a horizontal screen size.


class VacCheckApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Red'
        screen = Builder.load_string(screen_helper)
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
        bottom_sheet = MDCustomBottomSheet(screen=Factory.ContentCustomSheet(), radius_from="top", animation=True)
        bottom_sheet.open()

if __name__ == '__main__':
    VacCheckApp().run()