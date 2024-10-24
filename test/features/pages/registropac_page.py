from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistroPacientesPage(BasePage):

    # Locators
    NEW_PATIENT_BUTTON = (By.ID, 'btnNuevoPaciente')
    NOMBRE_INPUT = (By.ID, 'nombre')
    APELLIDOP_INPUT = (By.ID, 'apellidop')
    APELLIDOM_INPUT = (By.ID, 'apellidm')
    EDAD_INPUT = (By.ID, 'edad')
    GENERO_INPUT = (By.ID, 'gender')
    CP_INPUT = (By.ID, 'CodPostal')
    CELULAR_INPUT = (By.ID, 'telefonocelular')

    BOTON_NEXT = (By.ID, 'button-next')
    BOTON_SAVE = (By.ID, 'button-save')
    PRESION_ARTERIAL_INPUT = (By.ID, 'presionArterial')
    TEMPERATURA_INPUT = (By.ID, 'temperatura')
    PESO_INPUT = (By.ID, 'peso')
    CALZADO_INPUT = (By.ID, 'calzado')
    ULTIMA_VISTA_INPUT = (By.ID, 'ultimavisita')
    MOTIVO_CONSULTA_INPUT = (By.ID, 'motivo')

    DIABETES_INPUT = (By.ID, 'diabetes')
    HIPERTENSION_INPUT = (By.ID, 'hipertension')
    ALERGIAS_INPUT = (By.ID, 'alergias')
    ALERGIAS_AREA_TEXTO_INPUT = (By.ID, 'alergiasTextarea')
    ALERGIAS_ANESTESIA_INPUT = (By.ID, 'anestesia')
    OTROS_PADECIMIENTOS_INPUT = (By.ID, 'otros')
    OTROS_PADECIMIENTOS_AREA_TEXTO_INPUT = (By.ID, 'otrosTextarea')
    EMBARAZO_INPUT = (By.ID, 'embarazo')
    CHECKBOX_HEMM = (By.NAME, 'madre_hematologicos')
    CHECKBOX_HEMP = (By.NAME, 'madre_hematologicos')
    CONFIRMACION_REGISTRO_FOLIO = (By.ID, 'fol')   #FOLIO PACIENTE PRUEBA 665459, SEGUNDO PACIENTE PRUEBA 520478

    FOLIO_NUMBER = (By.ID, 'fol')
    QR_CODE = (By.XPATH, "//img[@alt='Código QR del cliente']")
    SUCCESS_REGISTRATION_MESSAGE = (By.XPATH, "//h2[@class='titulo' and text()='¡Registro Exitoso!']")

    def click_on_new_patient_button(self):
        self.click(self.NEW_PATIENT_BUTTON)

    def click_on_next_button(self):
        self.click(self.BOTON_NEXT)

    def click_on_save_button(self):
        self.click(self.BOTON_SAVE)

    def enter_general_info(self, nombre, apellidop, apellidom, edad, cp, celular):
        self.enter_text(self.NOMBRE_INPUT, nombre)
        self.enter_text(self.APELLIDOP_INPUT, apellidop)
        self.enter_text(self.APELLIDOM_INPUT, apellidom)
        self.enter_text(self.EDAD_INPUT, edad)
        self.enter_text(self.CP_INPUT, cp)
        self.enter_text(self.CELULAR_INPUT, celular)

    def select_gender(self, gen):
        gender_dropdown = self.browser.find_element(*self.GENERO_INPUT)
        select = Select(gender_dropdown)
        select.select_by_visible_text(gen)

    def enter_vital_signs(self, tension, temperature):
        self.enter_text(self.PRESION_ARTERIAL_INPUT, tension)
        self.enter_text(self.TEMPERATURA_INPUT, temperature)

    def enter_clinical_info(self, peso, calzado, ultimav, motivo):
        self.enter_text(self.PESO_INPUT, peso)
        self.enter_text(self.CALZADO_INPUT, calzado)
        self.enter_text(self.ULTIMA_VISTA_INPUT, ultimav)
        self.enter_text(self.MOTIVO_CONSULTA_INPUT, motivo)

    def enter_medical_history(self, fecha, detalles):
        self.enter_text((By.ID, 'history_date'), fecha)
        self.enter_text((By.ID, 'history_details'), detalles)

    def enter_general_history(self, enfermedad, medicamento):
        self.enter_text((By.ID, 'chronic_disease'), enfermedad)
        self.enter_text((By.ID, 'medication'), medicamento)

    def get_generated_folio(self):
        try:
            # Esperar a que el folio esté visible
            folio_element = WebDriverWait(self.browser, 15).until(
                EC.visibility_of_element_located((By.ID, 'fol'))
            )
            return folio_element.text
        except TimeoutException:
            print("El número de folio no fue encontrado a tiempo.")
            return None

    def get_successful_registration_message(self):
        success_message_element = self.find_element((By.XPATH, "//h2[@class='titulo' and text()='¡Registro Exitoso!']"))
        if success_message_element:
            return success_message_element.text
        else:
            return None

    def get_qr_code(self):
        return self.find_element(self.QR_CODE).get_attribute("src")

    def scan_qr_code(self):
        # Aquí iría el código para escanear el QR y retornar los datos
        pass