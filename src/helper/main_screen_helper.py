#from kivy_garden.zbarcam import ZBarCam

#:import ZBarCam kivy_garden.zbarcam.ZBarCam
#  MDBottomAppBar:
#                         MDToolbar:
#                             mode: 'center'
#                             type: 'bottom'
#                             icon: 'camera'
#                             on_action_button: app.action_button()
screen_helper = """
#: import XCamera kivy.garden.xcamera.XCamera
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
                    XCamera:
                        id:qrcodecam
                        canvas.before:
                            PushMatrix
                            Rotate:
                                angle: -90
                                origin: self.center
                        canvas.after:
                            PopMatrix
                    Label:
                        size_hint: None, None
                        size: self.texture_size[0], 50
                        text: 'Test' #' '.join([str(symbol) for symbol in qrcodecam.symbols])    
                   
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