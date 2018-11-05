from kivy.config import Config
Config.set("graphics", "resizable", False)
Config.set("graphics", "width", 640)
Config.set("graphics", "height", 480)
from kivy.app import App
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.uix.screenmanager import ScreenManager, Screen

LabelBase.register(DEFAULT_FONT, "ipaexg.ttf")
sm = ScreenManager()

USER_ID = "test" #追加
PASSWORD = "test" #追加
ERROR_MESSAGE = "ログインエラー"
class LoginScreen(Screen):
    def loginButtonClicked(self):
        userID = self.ids["text_userID"].text  # この行を追加
        password = self.ids["text_password"].text
        if USER_ID == userID and password == PASSWORD:  # このブロックを追加
            sm.current = "input"
        else:
            self.ids["error_message"].text = ERROR_MESSAGE
        pass
class InputScreen(Screen):
    def ReturnButtonClicked(self):
        sm.current = "login"


class ExpenseApp(App):
    def build(self):
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(InputScreen(name="input"))
        return sm


if __name__ == '__main__':
    ExpenseApp().run()
