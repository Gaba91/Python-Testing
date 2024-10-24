from behave import given, when, then
from pages.registropac_page import RegistroPacientesPage
from environment import config


@given('the user opens the patient registration page')
def go_to_registration_page(context):
    registropac_page = RegistroPacientesPage(context.browser)
    registropac_page.go_to('https://akyo.com.mx/UAT_AKYO1921Podologia/index.php')


@when('the user clicks the "new patient" button')
def click_on_new_patient_button(context):
    registropac_page = RegistroPacientesPage(context.browser)
    registropac_page.click_on_new_patient_button()


# @when('the user fills the patients general data nombre "{nombre}"')
# def step_enter_general_info(context, nombre):
#     registropac_page = RegistroPacientesPage(context.browser)
#     registropac_page.enter_general_info(nombre)


@when('the user fills the patients general data nombre "{nombre}" apellidop "{apellidop}" apellidom "{apellidom}" '
      'edad "{edad}" genero "{gen}" cp "{cp}" celular "{celular}"')
def step_enter_general_info(context, nombre, apellidop, apellidom, edad, cp, celular, gen):
    registropac_page = RegistroPacientesPage(context.browser)
    registropac_page.enter_general_info(nombre, apellidop, apellidom, edad, cp, celular)
    registropac_page.select_gender(gen)


@when('the user clicks on the "next" button')
def click_on_next_button(context):
    registropac_page = RegistroPacientesPage(context.browser)
    registropac_page.click_on_next_button()


@when('the user fills the vital signs data form tension "{tension}" temperature "{temperature}"')
def step_enter_vital_signs(context, tension, temperature):
    registropac_page = RegistroPacientesPage(context.browser)
    registropac_page.enter_vital_signs(tension, temperature)


# @when('the user clicks on the "next" button')
# def click_on_next_button(context):
#     registropac_page = RegistroPacientesPage(context.browser)
#     registropac_page.click_on_next_button()


@when('the user fills the "clinical data" form peso "{peso}" calzado "{calzado} ultimav "{ultimav}" motivo "{motivo}"')
def step_enter_clinical_info(context, peso, calzado, ultimav, motivo):
    registropac_page = RegistroPacientesPage(context.browser)
    registropac_page.enter_clinical_info(peso, calzado, ultimav, motivo)


# @when('the user clicks on the "next" button')
# def click_on_next_button(context):
#     registropac_page = RegistroPacientesPage(context.browser)
#     registropac_page.click_on_next_button()


# @when('the user clicks on the "next" button')
# def click_on_next_button(context):
#     registropac_page = RegistroPacientesPage(context.browser)
#     registropac_page.click_on_next_button()


@when('the user clicks on the "save" button')
def click_on_save_button(context):
    registropac_page = RegistroPacientesPage(context.browser)
    registropac_page.click_on_save_button()


@then('the system displays the folio number')
def step_verify_folio_generated(context):
    print("Ejecutando paso para verificar folio...")  # Impresión de depuración
    registropac_page = RegistroPacientesPage(context.browser)
    folio_number = registropac_page.get_generated_folio()
    if folio_number:  # Si capturó el folio correctamente
        print(f"El número de folio es: {folio_number}")  # Impresión de depuración
    else:  # Si no se capturó el folio
        print("No se generó el número de folio.")  # Impresión de depuración

# @then('the system displays the folio number')
# def step_verify_folio_generated(context):
#     registropac_page = RegistroPacientesPage(context.browser)
#     folio_number = registropac_page.get_generated_folio()
#     print(f"El número de folio es: {folio_number}")


# @then('And the folio number should be copied')
# def step_verify_folio_copied(context):
#     folio_in_clipboard = pyperclip.paste()
#     folio_generated = context.page.get_generated_folio()
#     assert folio_in_clipboard == folio_generated, "Folio no copiado al portapapeles"


@then('a QR code should be generated')
def step_verify_qr_generated(context):
    registropac_page = RegistroPacientesPage(context.browser)
    qr_code = registropac_page.get_qr_code()
    assert qr_code is not None, "Código QR no generado"


@then('the user should see the "registro exitoso" message')
def step_verify_succesful_registration_message(context):
    registropac_page = RegistroPacientesPage(context.browser)
    sr_message = registropac_page.get_successful_registration_message()
    print(f"{sr_message}")

# @when('the user fills the patients general data apellidop "{apellidop}"')
# def step_enter_general_info(context, apellidop):
#     registropac_page = RegistroPacientesPage(context.browser)
#     registropac_page.enter_general_info(apellidop)
#
#
# @when('the user fills the patients general data apellidom "{apellidom}"')
# def step_enter_general_info(context, apellidom):
#     registropac_page = RegistroPacientesPage(context.browser)
#     registropac_page.enter_general_info(apellidom)
#
#
# @when('the user fills the patients general data edad "{edad}"')
# def step_enter_general_info(context, edad):
#     registropac_page = RegistroPacientesPage(context.browser)
#     registropac_page.enter_general_info(edad)
#
#
# @when('the user fills the patients general data genero "{gen}"')
# def step_enter_general_info(context, gen):
#     registropac_page = RegistroPacientesPage(context.browser)
#     registropac_page.enter_general_info(gen)
#
#
# @when('the user fills the patients general data cp "{cp}"')
# def step_enter_general_info(context, cp):
#     registropac_page = RegistroPacientesPage(context.browser)
#     registropac_page.enter_general_info(cp)
#
#
# @when('the user fills the patients general data celular "{celular}"')
# def step_enter_general_info(context, celular):
#     registropac_page = RegistroPacientesPage(context.browser)
#     registropac_page.enter_general_info(celular)

# @when('the user fills the patients general data')
# def step_enter_general_info(context, nombre, apellidop, apellidom, edad, gen, cp, celular):
#     registropac_page = RegistroPacientesPage(context.browser)
#     registropac_page.enter_general_info(nombre, apellidop, apellidom, edad, gen, cp, celular)

# @when('the user fills the vital signs data form')
# def step_enter_vital_signs(context):
#     context.page.enter_vital_signs("130/80", 36.3)
#
#
# @when('the user clicks on the "next" button')
# def click_on_next_button(context):
#     registropac_page = RegistroPacientesPage(context.browser)
#     registropac_page.click_on_next_button()
#
#
# @when('the user fills the "clinical data" form')
# def step_enter_clinical_info(context):
#     context.page.enter_clinical_info(89, 27, 6, "Dolor")


# @when('el usuario ingresa el historial clínico')
# def step_enter_medical_history(context):
#     context.page.enter_medical_history("2022", "Cirugía")
#
#
# @when('el usuario ingresa los antecedentes generales')
# def step_enter_general_history(context):
#     context.page.enter_general_history("Diabetes", "Metformina")
#
#
# @then('el sistema debe generar un folio único')
# def step_verify_folio_generated(context):
#     folio = context.page.get_generated_folio()
#     assert folio is not None, "Folio no generado"
#
#
# @then('el folio se debe copiar automáticamente al portapapeles')
# def step_verify_folio_copied(context):
#     folio_in_clipboard = pyperclip.paste()
#     folio_generated = context.page.get_generated_folio()
#     assert folio_in_clipboard == folio_generated, "Folio no copiado al portapapeles"
#
#
# @then('se debe generar un código QR')
# def step_verify_qr_generated(context):
#     qr_code = context.page.get_qr_code()
#     assert qr_code is not None, "Código QR no generado"
#
#
# @then('el código QR debe ser validado correctamente')
# def step_validate_qr_code(context):
#     qr_data = context.page.scan_qr_code()
#     folio_generated = context.page.get_generated_folio()
#     assert qr_data == folio_generated, "Código QR no es válido"
