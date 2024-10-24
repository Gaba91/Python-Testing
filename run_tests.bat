@echo off

REM Cambiar al directorio de features
cd test\features

REM Ejecutar pruebas con Behave y generar los resultados para Allure
behave -f allure_behave.formatter:AllureFormatter -o reports/

REM Volver al directorio raíz
cd ..\..

REM Comprobar si la carpeta de resultados de Allure existe
if not exist test\features\reports (
    echo "La carpeta de resultados 'reports' no existe. Verifique los errores de ejecución de Behave."
    pause
    exit /b
)

REM Generar el reporte de Allure y abrirlo en el navegador
allure serve test\features\reports
pause