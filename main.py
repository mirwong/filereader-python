from kivy.app import App
from kivy.uix.widget import Widget


class FilereaderWidget(Widget):
    pass


class FilereaderApp(App):
    def build(self):
        return FilereaderWidget()


if __name__ == '__main__':
    FilereaderApp().run()