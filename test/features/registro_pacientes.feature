Feature: Registro de pacientes en el sistema

  Scenario: Registrar un paciente con datos completos
    Given the user opens the patient registration page
    When the user clicks the "new patient" button
    When the user fills the patients general data nombre "Juan" apellidop "Garza" apellidom "Perez" edad "50" genero "Masculino" cp "Altavista" celular "5599938765"
    And the user clicks on the "next" button
    And the user fills the vital signs data form tension "125/80" temperature "36.2"
    And the user clicks on the "next" button
    And the user fills the "clinical data" form peso "75" calzado "28" ultimav "6" motivo "Dolor"
    And the user clicks on the "next" button
    And the user clicks on the "next" button
    And the user clicks on the "save" button
    Then the system displays the folio number
    And a QR code should be generated
    And the user should see the "registro exitoso" message

#  When the user fills the patients general data nombre "Juan"
#    When the user fills the patients general data apellidop "Garza"
#    When the user fills the patients general data apellidom "Perez"
#    When the user fills the patients general data edad "50"
#    When the user fills the patients general data genero "Masculino"
#    When the user fills the patients general data cp "Altavista"
#    When the user fills the patients general data celular "5599938765"

#  Scenario: Registrar un paciente con datos completos
#    And the user fills the patients general data
#      | Nombre | Apellido Paterno | Apellido Materno | Edad | Genero    | Colonia   | Celular   |
#      | Juan   | Garza            | Perez            | 50   | Masculino | Altavista | 5599938765 |
#    And the user clicks on the "next" button


#    And the user fills the "vital signs data" form
#      | Tension arterial | Temperatura |
#      | 120/80           | 36.2        |
#    And the user clicks on the "next" button
#    And the user fills the "clinical data" form
#      | Peso | No. calzado | Ultima visita | Motivo de consulta |
#      | 80   | 28          | 7             | Dolor              |
#    And the user clicks on the "next" button
#    And the user clicks on the "next" button
#    And the user clicks on the "save" button
#    Then the user should automatically get a "issue/folio number"
#    And the folio number should be copied
#    And a QR code should be generated
#    And the QR code should be validated accordingly
#    And the user should see the "registro exitoso" message

#  Scenario: Validar que el folio es copiado al portapapeles después del registro
#    Given el usuario ha completado el registro del paciente
#    Then el folio se ha copiado correctamente al portapapeles
#
#  Scenario: Validar código QR generado al finalizar registro
#    Given el usuario ha registrado al paciente con éxito
#    Then el código QR debe contener la información del folio
#    And debe poder ser escaneado y validado