
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