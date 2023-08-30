Instalación y Ejecución del Proyecto
Clonar el repositorio desde GitHub:

Clonar el repositorio desde GitHub:
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio

Crear y activar un entorno virtual (opcional pero recomendado):
python3 -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate

Instalar las dependencias del proyecto:
pip install -r requirements.txt

Parte I: Implementación del Modelo
Transcribir el archivo .ipynb al archivo model.py:

Abre el archivo .ipynb y revisa el código del modelo.
Crea un nuevo archivo llamado model.py.
Copia y pega el código relevante del modelo en model.py.
Corregir errores y elegir el mejor modelo:

Revisa el código copiado y asegúrate de que no haya errores de sintaxis.
Si encuentras errores, corrígelos siguiendo los mensajes de error.
Si el archivo .ipynb propone varios modelos, elige el mejor basado en tus criterios y conocimiento.
Aplicar buenas prácticas de programación:

Asegúrate de que el código sea limpio y legible.
Agrega comentarios descriptivos donde sea necesario.
Utiliza nombres de variables y funciones descriptivos.
Ejecutar pruebas del modelo:

Abre una terminal en la carpeta del proyecto.
Ejecuta el comando make model-test para probar el modelo.
Verifica que todas las pruebas pasen sin errores.
Parte II: Desarrollo de la API con FastAPI
Crear el archivo api.py:

Crea un nuevo archivo llamado api.py en la misma ubicación que model.py.
Copiar y pegar el código proporcionado:

Copia el código proporcionado para la API y pégalo en api.py.
Implementar rutas y funciones:

Completa las rutas y funciones de acuerdo al código proporcionado.
Asegúrate de seguir la estructura del código y definir las rutas correctamente.
Ejecutar pruebas de la API:

Abre una terminal en la carpeta del proyecto.
Ejecuta el comando make api-test para probar la API.
Verifica que todas las pruebas pasen sin errores.
Parte III: Implementación en AWS Lambda
Crear una función Lambda en AWS:

Inicia sesión en tu cuenta de AWS y ve al servicio "Lambda".
Haz clic en "Crear función" y elige "Autor desde cero".
Completa los detalles básicos de la función, como nombre, runtime y rol de ejecución.
Haz clic en "Crear función" para crear la función Lambda.
Copiar el código de api.py en la función Lambda:

Abre el archivo api.py y copia todo el contenido.
Vuelve a la consola de AWS y pega el contenido en la función Lambda.
Configurar una API Gateway:

Desde la consola de AWS, ve al servicio "API Gateway".
Crea una nueva API y configura un recurso y un método POST.
Asocia el método POST con la función Lambda creada.
Probar la API en AWS Lambda:

Utiliza la consola de AWS para probar la función Lambda con un evento de prueba.
Verifica los registros de la función Lambda para obtener los resultados de la prueba.
Parte IV: Configuración de CI/CD
Crear la carpeta .github:

En la carpeta raíz del proyecto, crea una nueva carpeta llamada .github.
Copiar las carpetas workflows dentro de .github:

Descarga las carpetas workflows proporcionadas y cópialas dentro de .github.
Ajustar ci.yml y cd.yml:

Abre los archivos ci.yml y cd.yml dentro de .github/workflows.
Sigue las instrucciones proporcionadas para configurar los flujos de CI/CD.
Enviar el Desafío
Ejecutar el comando curl:

Abre una terminal y ejecuta el comando curl con tus detalles de desafío.
Asegúrate de incluir tu nombre, correo, URL de GitHub y URL de la API implementada.
