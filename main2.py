from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import Screen


class LoginScreen(Screen):
    
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.users = {'user': 'user', 'user2': 'password2'}
    
    def verify_credentials(self, username, password):
        # if username not in self.users or password != self.users[username]:
        #    Snackbar(text="Usuario o contraseña incorrectos").open()
        # else:
        self.manager.current = 'InnerScreen'


class InnerScreen(Screen):
    
    def __init__(self, **kwargs):
        super(InnerScreen, self).__init__(**kwargs)
        self.users = {'user': 'user', 'user2': 'password2'}


class MainApp(MDApp):

    def build(self):
        return Builder.load_file('fuente.kv')


if __name__ == "__main__":
    MainApp().run()
