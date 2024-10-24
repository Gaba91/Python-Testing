# Esta pagina contiene los identificadores y metodos para de la pagina "LOGIN"

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    # Definir los elementos de la pagina
    USER_INPUT = (By.ID, 'username')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login')
    REGISTER_LINK = (By.XPATH, '//a[text()="Registrate aqui"]')
    HOMEPAGE_MESSAGE = (By.XPATH, '//p[text()="Esta es una página segura solo accesible después de iniciar sesión."]')
    ERROR_MESSAGE = (By.ID, 'loginForm')
    INICIAR_SESION_MESSAGE = (By.XPATH, '(//*[text()="Iniciar Sesión"])[1]')


    def enter_username(self, username):
        # Usa el método 'enter_text' de BasePage para ingresar el nombre de usuario
        self.enter_text(self.USER_INPUT, username)

    def enter_password(self, password):
        # Usa el método 'enter_text' de BasePage para ingresar la contraseña
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        # Usa el método 'click' definido en BasePage para hacer clic en el botón de login
        self.click(self.LOGIN_BUTTON)

    def welcome_homepage_message(self):
        self.find_element(self.HOMEPAGE_MESSAGE)

    def error_message(self):
        self.find_element(self.HOMEPAGE_MESSAGE)

    def iniciar_sesion_message(self):
        self.find_element(self.INICIAR_SESION_MESSAGE)

# class LoginPage(BasePage):
#     # Definir los elementos de la pagina
#
#     USER_INPUT = (By.ID, 'username')
#     PASSWORD_INPUT = (By.ID, 'password')
#     LOGIN_BUTTON = (By.ID, 'login')
#     REGISTRATE_LINK = (By.XPATH, '//a[text()="Registrate aqui"]')
#
#     def enter_username(self, username):
#         # self.browser.find_element(*self.USER_INPUT).send_keys(username)
#         # 2da opcion mas corta, una vez que se creo el metodo en base_page
#         self.enter_username(self.USER_INPUT, username)
#
#     def enter_password(self, password):
#         # self.browser.find_element(*self.PASSWORD_INPUT).send_keys(password)
#         self.enter_password(self.PASSWORD_INPUT, password)
#
#     def click_login(self):
#         # self.browser.find_element(*self.LOGIN_BUTTON).click()
#         self.click(self.LOGIN_BUTTON)
