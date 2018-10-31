from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Username:"))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)


class IntoroKivy(App):

    # 画面にHello World!と表示
    def build(self):
        return LoginScreen()


# Main
if __name__ == "__main__":
    # アプリの起動
    IntoroKivy().run()
