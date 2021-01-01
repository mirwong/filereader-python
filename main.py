from Kivy.app import App
from Kivy.uix.widget import Widget


class FilereaderScreen(Widget):
    pass


class FilereaderApp(App):
    def build(self):
        return FilereaderScreen()


if __name__ == '__main__':
    FilereaderApp().run()