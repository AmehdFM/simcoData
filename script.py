
import os
import requests

baseUrl = 'https://d1fxy698ilbz6u.cloudfront.net/static/'

# Directorio donde se guardarán las imágenes
directory = 'C:/Users/Mendez/Downloads/simco/recursos'
if not os.path.exists(directory):
    os.makedirs(directory)

for i in range(1, 145):
    response = requests.get(f'https://www.simcompanies.com/api/v4/es/0/encyclopedia/resources/1/{i}/')
    resource_data = response.json()

    try:
        image_url = resource_data['image']
    except KeyError:
        print(f"No se encontró una imagen para el recurso {i}")
        continue

    # Obtener el nombre del archivo de la URL de la imagen
    image_filename = os.path.basename(image_url)

    # Construir la URL completa de la imagen
    full_image_url = baseUrl + image_url

    # Realizar la solicitud GET para descargar la imagen
    image_response = requests.get(full_image_url)
    if image_response.status_code == 200:
        # Guardar la imagen en el directorio especificado
        with open(os.path.join(directory, image_filename), 'wb') as f:
            f.write(image_response.content)
        print(f"Imagen {image_filename} descargada exitosamente.")
    else:
        print(f"No se pudo descargar la imagen {image_filename}. Estado de la respuesta: {image_response.status_code}")

print("Proceso completado.")
