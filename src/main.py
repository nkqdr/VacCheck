from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
import cv2

class VacCheckApp(MDApp):
    def build(self):
        label = MDLabel(text='Hello World!', halign='center')
        return label

if __name__ == '__main__':
    VacCheckApp().run()