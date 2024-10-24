# Este archivo contiene los elementos genericos para que sean utilizados por las paginas
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.support.ui import Select


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.timeout = 10

    def go_to(self, url):
        self.browser.get(url)

    def espera(self, seconds=10):
        time.sleep(seconds)

    def find_element(self, by_locator):
        try:
            element = WebDriverWait(self.browser, self.timeout).until(
                EC.visibility_of_element_located(by_locator)
            )

            return element
        except TimeoutException:
            print(f"El elemento con el locator {by_locator} no fue encontrado.")
            return None

    def find_elements(self, by_locator):
        try:
            return WebDriverWait(self.browser, self.timeout).until(
                EC.visibility_of_all_elements_located(by_locator)
            )
        except TimeoutException:
            print(f"Los elementos con el locator {by_locator} no fueron encontrados.")
            return []

    def enter_text(self, by_locator, text):
        element = self.find_element(by_locator)
        if element:
            element.clear()
            element.send_keys(text)

    def click(self, by_locator):
        element = self.find_element(by_locator)
        if element:
            element.click()

    def wait_for_element_clickable(self, by_locator):
        try:
            return WebDriverWait(self.browser, self.timeout).until(
                EC.element_to_be_clickable(by_locator)
            )
        except TimeoutException:
            print(f"El elemento con el locator {by_locator} no es clickeable.")
            return None

    def scroll_to_element(self, by_locator):
        element = self.find_element(by_locator)
        if element:
            self.browser.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_to_bottom(self):
        """Hace scroll hasta el final de la página."""
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def switch_to_frame(self, frame_locator):
        frame = self.find_element(frame_locator)
        if frame:
            self.browser.switch_to.frame(frame)

    def switch_to_default_content(self):
        self.browser.switch_to.default_content()

    def accept_alert(self):
        try:
            WebDriverWait(self.browser, self.timeout).until(EC.alert_is_present())
            alert = self.browser.switch_to.alert
            alert.accept()
        except TimeoutException:
            print("No se encontró ninguna alerta.")

    def dismiss_alert(self):
        try:
            WebDriverWait(self.browser, self.timeout).until(EC.alert_is_present())
            alert = self.browser.switch_to.alert
            alert.dismiss()
        except TimeoutException:
            print("No se encontró ninguna alerta.")

    def get_alert_text(self):
        try:
            WebDriverWait(self.browser, self.timeout).until(EC.alert_is_present())
            alert = self.browser.switch_to.alert
            return alert.text
        except TimeoutException:
            print("No se encontró ninguna alerta.")
            return None

    def take_screenshot(self, file_path):
        self.browser.save_screenshot(file_path)

    def element_is_present(self, by_locator):
        """Verifica si un elemento está presente en el DOM."""
        try:
            WebDriverWait(self.browser, self.timeout).until(
                EC.presence_of_element_located(by_locator)
            )
            return True
        except TimeoutException:
            print(f"El elemento con el locator {by_locator} no está presente en el DOM.")
            return False

    def element_is_enabled(self, by_locator):
        """Verifica si un elemento está habilitado para la interacción."""
        element = self.find_element(by_locator)
        return element.is_enabled() if element else False

    def element_is_selected(self, by_locator):
        """Verifica si un checkbox o radio button está seleccionado."""
        element = self.find_element(by_locator)
        return element.is_selected() if element else False

    def get_page_title(self):
        """Obtiene el título de la página."""
        return self.browser.title

    def wait_for_element_to_disappear(self, by_locator):
        """Espera a que un elemento desaparezca del DOM."""
        try:
            WebDriverWait(self.browser, self.timeout).until_not(
                EC.presence_of_element_located(by_locator)
            )
            return True
        except TimeoutException:
            print(f"El elemento con el locator {by_locator} sigue presente.")
            return False

    def switch_to_window(self, window_name):
        """Cambia a otra ventana o pestaña."""
        self.browser.switch_to.window(window_name)

    def get_current_window_handle(self):
        """Obtiene el manejador de la ventana actual."""
        return self.browser.current_window_handle

    def get_all_window_handles(self):
        """Obtiene los manejadores de todas las ventanas abiertas."""
        return self.browser.window_handles

    def element_contains_text(self, by_locator, text):
        """Verifica si un elemento contiene un texto específico."""
        element = self.find_element(by_locator)
        if element:
            return text in element.text
        return False

    def select_option(self, by_locator, option_text=None, option_value=None, option_index=None):
        """Selecciona una opción de un elemento select por texto visible, valor o índice."""
        element = self.find_element(by_locator)
        if element:
            select = Select(element)
            if option_text:
                select.select_by_visible_text(option_text)
            elif option_value:
                select.select_by_value(option_value)
            elif option_index is not None:
                select.select_by_index(option_index)
            else:
                print("Especifica un option_text, option_value o option_index para seleccionar una opción.")
        else:
            print(f"El elemento con el locator {by_locator} no fue encontrado.")

    # def take_screenshot(self, step_name):
    #     """Toma una captura de pantalla y la guarda en el directorio screenshots"""
    #     screenshot_dir = "screenshots"
    #     if not os.path.exists(screenshot_dir):
    #         os.makedirs(screenshot_dir)
    #     screenshot_path = os.path.join(screenshot_dir, f"{step_name}.png")
    #     self.browser.save_screenshot(screenshot_path)
    #     return screenshot_path

