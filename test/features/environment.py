from selenium import webdriver
import yaml


# Función para cargar la configuración global desde un archivo YAML
def load_config(config_path='config/config.yaml'):    # <--- a veces es necesario quitar los ..al inicio de la ruta
    # ('..config/config.yaml')
    """Carga el archivo config.yml con la configuración global."""
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config


# Cargar la configuración global al inicio
config = load_config()


# Acceder a los valores en todo el framework
base_url = config['base_url']
username = config['username']
password = config['password']


def before_all(context):
    # Configuración inicial del navegador
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()


def after_all(context):
    # Cierra el navegador después de todos los tests
    context.browser.quit()

    # Cerrar el navegador solo si sigue abierto
    if context.browser:
        context.browser.quit()

