from behave import given, when, then
from pages.login_page import LoginPage
from environment import config


@given('the user opens the login page')
def step_open_login_page(context):
    login_page = LoginPage(context.browser)
    login_page.go_to('https://akyo.com.mx/lab_cypress/login.html') # <-- ver ultimos 15 min de clase para configuracion 05/10/24


@when('the user enters username "{username}"')
def step_enter_credentials_username(context, username):
    login_page = LoginPage(context.browser)
    login_page.enter_username(username)


@when('the user enters password "{password}"')
def step_enter_credentials_password(context, password):
    login_page = LoginPage(context.browser)
    login_page.enter_password(password)


@when('the user clicks on login button')
def step_enter_credentials_click_login_button(context):
    login_page = LoginPage(context.browser)
    login_page.click_login()


@then('the user should see the home page')
def step_go_to_homepage(context):
    login_page = LoginPage(context.browser)
    login_page.welcome_homepage_message()


@then('the user should see an error message')
def step_go_to_homepage(context):
    login_page = LoginPage(context.browser)
    login_page.error_message()


@then('the user should not see the home page')
def step_go_to_homepage(context):
    pass
    # login_page = LoginPage(context.browser)
    # login_page.iniciar_sesion_message

