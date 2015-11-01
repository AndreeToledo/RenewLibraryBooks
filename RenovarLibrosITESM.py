# Codigo de Aldo Andreé Toledo Ulloa - Perimetro20
# 2015

from splinter import Browser

browser = Browser()

# Coloca tus datos
apellido = "Tu apellido va aquí"
nip = 'Pon tu nip'
matricula = "Escribe tu matircula"

# Acceder a la página de login de la biblioteca
browser.visit('https://millenium.itesm.mx/patroninfo*spi')

# Llenar los campos de login
browser.fill('name', apellido)
browser.fill('code', matricula)
browser.fill('pin', nip)

# Hacer click en el boton submit
browser.find_by_name('submit').click()

# Ir a libros prestados
browser.click_link_by_partial_href('items')

# Hacer click en el boton de renovar todo
links_found = browser.find_link_by_href('#')
links_found[1].click()

# Confirmar renovación
browser.find_by_name('renewall').click()

if browser.is_text_present('apartado'):
    print "No se pudieron renovar todos los libros por que alguno está apartado"
else:
    print "Exito"

# Cerrar pestaña del navegador
browser.quit()