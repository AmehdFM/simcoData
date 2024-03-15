from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Ruta del ChromeDriver
chromedriver_path = "C:/Users/Mendez/Downloads\\prueba\\chromedriver.exe"

# Lista de códigos de edificios
edificiosCode = ["P","W","E","O","R","S","G","C","A","F","6","M","Y","L","T","H","1","2","p","h","b","c","s","a","f","l","q","3","4","5","D","7","8","9","0","B","Q","o","x","g","d","n","e","i","j","k","m","r"]

# Diccionario base para almacenar datos
edificio_base = {
    'id': "",
    'name': "",
    'resourcesNeed': {},
    'timeNeed': 0,
    'baseSalary': 0,
    'producedAt': {},
    'referenceValue': 0,
}

# Lista para almacenar los datos de todos los edificios
edificiosList = []

# Crear una instancia del navegador
driver = webdriver.Chrome(executable_path=chromedriver_path)

# Acceder a la URL
driver.get("https://www.simcompanies.com/es/encyclopedia/1/building/S/")

for codigo in edificiosCode:
    # Reemplazar la "S" en la URL por el código actual
    driver.get(f"https://www.simcompanies.com/es/encyclopedia/1/building/{codigo}/")

    # Esperar a que la página se cargue
    sleep(10)

    # Obtener el nombre del edificio
    try:
        nombre_edificio = driver.find_element(By.XPATH, '//*[@id="page"]/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div/h3').text
        print(nombre_edificio)
    except Exception as e:
        nombre_edificio = driver.find_element(By.XPATH,'//*[@id="page"]/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div/h3').text
        print(nombre_edificio)

    # Obtener los recursos necesarios para la construcción
    bloques = driver.find_element(By.XPATH,'//*[@id="page"]/div/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[2]/td/div[2]').text
    tablones = driver.find_element(By.XPATH,'//*[@id="page"]/div/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[3]/td/div[1]').text
    UC = driver.find_element(By.XPATH,'//*[@id="page"]/div/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[3]/td/div[2]').text
    RC = driver.find_element(By.XPATH,'//*[@id="page"]/div/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[2]/td/div[1]').text

    recursos_necesarios = {
                        'construction-units':UC.replace('x','') ,
                        'reinforced-concrete':RC.replace('x','') ,
                        'bricks':bloques.replace('x','') ,
                        'planks':tablones.replace('x','')
                    }
    print(recursos_necesarios)

    # Obtener el tiempo de construcción
    tiempo_construccion = (driver.find_element(By.XPATH, '//*[@id="page"]/div/div/div/div[2]/div/div[2]/div[2]/div/div[4]/div/table/tbody/tr[1]/td[2]').text)
    tiempo_construccion = tiempo_construccion.replace(':00h','')
    print(tiempo_construccion)

    # Obtener el salario base
    try:
        salario_base = (driver.find_element(By.XPATH, '//*[@id="page"]/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div').text)
        salario_base = salario_base.replace('Salarios de los trabajadores: $','')
        salario_base = salario_base.replace(nombre_edificio,'')
        salario_base = salario_base.replace('/hour','')
        salarioDia = salario_base[2:]
    except Exception as e:
        salario_base = driver.find_element(By.XPATH,'//*[@id="page"]/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div').text
        salario_base = salario_base.replace('Salarios de los trabajadores: $','')
        salario_base = salario_base.replace('/hour','')
        salario_base = salario_base.replace(nombre_edificio,'')
        salarioDia = salario_base[2:]

    # Obtener los lugares de producción
    lugares_produccion = {}

    # Obtener el valor de referencia
    valor_referencia = (driver.find_element(By.XPATH, '//*[@id="page"]/div/div/div/div[2]/div/div[2]/div[2]/div/div[3]/div/table/tbody/tr[1]/td[2]').text)
    valor_referencia = valor_referencia.replace('$','')
    valor_referencia = valor_referencia.replace('.','')
    print(valor_referencia)

    # Crear un diccionario con los datos del edificio actual
    edificio = edificio_base.copy()
    edificio['id'] = codigo
    edificio['name'] = nombre_edificio
    edificio['resourcesNeed'] = recursos_necesarios
    edificio['timeNeed'] = tiempo_construccion
    edificio['baseSalary'] = salarioDia
    edificio['producedAt'] = lugares_produccion
    edificio['referenceValue'] = valor_referencia

    # Agregar el diccionario a la lista
    edificiosList.append(edificio)

# Cerrar el navegador
driver.quit()

# Imprimir la lista de edificios
print(edificiosList)
