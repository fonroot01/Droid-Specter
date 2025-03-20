# DroidSpecter
Droid Specter es una herramienta desarrollada en Python que te permite tomar el control de tus dispositivos Android directamente desde tu PC.
Con una interfaz gráfica amigable, podrás gestionar tus dispositivos a través de ADB (Android Debug Bridge) de forma sencilla. 
Conecta tus dispositivos, visualiza las aplicaciones instaladas, instala o desinstala aplicaciones, e incluso deshabilita aquellas que no necesites, todo desde la comodidad de tu PC.

## Funciones 

* **Conexión Versátil:**
    * Vas a poder conectarte con dispositivos Android, incluyendo teléfonos, tabletas y Android TV, mediante ADB a través de conexiones por cable o Wi-Fi.
* **Gestión de Aplicaciones:**
    * Podes obtener listados detallados de las aplicaciones instaladas en sus dispositivos.
    * Vas a poder agregar archivos APK de manera sencilla y desinstalar aplicaciones con un solo clic.
* **Control Avanzado:**
    * Podrás deshabilitar aplicaciones según sea necesario para optimizar el rendimiento de tu dispositivo.

## Requisitos del Sistema

* **Python 3.x:** Valida primero tener Python instalado en el PC.
* **Android Debug Bridge (ADB):** ADB debe estar configurado y accesible en tu entorno.
* **Dependencias de Python:** Las siguientes librerías deben estar instaladas: `tkinter`, `ttkbootstrap` y `Pillow`.

## Instrucciones de Instalación

1.  **Clonación del Repositorio:**
    * Tenés que utilizar el siguiente comando para clonar el repositorio: `git clone https://github.com/fonroot01/DroidSpecter.git`
2.  **Instalación de Dependencias:**
    * Instala las librerías necesarias ejecutando el siguiente comando: `pip install ttkbootstrap Pillow`

### Ejecución desde el Código Fuente (Python)

1.  **Navegación al Directorio:**
    * Te metés a la carpeta del repositorio clonado.
2.  **Ejecución del Script:**
    * Vas a ejecutar el script principal con el siguiente comando: `python DroidSpecter.py`
3.  **Conexión del Dispositivo:**
    * Te vas a conectar a tu dispositivo Android mediante ADB a través de cable USB o Wi-Fi.
4.  **Uso de la Interfaz:**
    * Y por ultimo utilizas la interfaz gráfica para realizar las operaciones que desees.

### Ejecución desde el Archivo .exe (Windows)

1.  **Ubicación del Archivo:**
    * Localiza el archivo `DroidSpecter.exe` en la carpeta `dist`.
2.  **Ejecución del Ejecutable:**
    * Ejecuta el archivo `.exe` haciendo doble clic sobre él.
3.  **Advertencia de Seguridad:**
    * Si aparece una advertencia de seguridad de Windows, selecciona "Ejecutar de todas formas".
4.  **Conexión del Dispositivo:**
    * Conecta tu dispositivo Android mediante ADB a través de cable USB o Wi-Fi.
5.  **Uso de la Interfaz:**
    * Vas a utilizar la interfaz gráfica para realizar las operaciones que quieras.

### Conexión a Android TV (O cualquier dispositivo Android)

1.  **Modo Desarrollador:**
    * Activas el modo desarrollador en tu Android TV accediendo a la sección "Acerca de" y presionando repetidamente "Número de compilación".
2.  **Depuración ADB:**
    * Habilitas la depuración por USB o la depuración por red en las opciones de desarrollador.
3.  **Conexión de Red:**
    * Valida de que tu Android TV y tu PC estén conectados a la misma red Wi-Fi. **(FUNDAMENTAL)**
4.  **Dirección IP:**
    * Despues buscas la dirección IP de tu Android TV desde la configuración de red.
5.  **Conexión en Droid Specter:**
    * Y para terminar, vas la dirección IP y el puerto (generalmente 5555) en Droid Specter y le vas a dar clic en "Conectar".
  
## Mostrando la app funcionando

![Interfaz de usuario](https://github.com/user-attachments/assets/f07adff1-5060-4a31-aadd-67b3e94c0683)
![Conexion establecida](https://github.com/user-attachments/assets/6f015480-3783-4d8b-b8ef-606e94d72098)
![Permitir depuracion por USB](https://github.com/user-attachments/assets/6678843a-d2c5-43d1-ac07-87d56de6aeb2)
![Se busca el instalador APK](https://github.com/user-attachments/assets/6cd6c8ce-a773-46d3-9fa4-d56aaa232f1d)
![En mi caso es este](https://github.com/user-attachments/assets/9db3affa-e221-4696-8efd-cd8348d7071f)
![La app confirma la instalacion](https://github.com/user-attachments/assets/672c93ab-bd3d-4b2a-9a3e-0db694f61621)
![image](https://github.com/user-attachments/assets/ca3c77e1-3f19-46ff-91fe-711accc384fd)

## Contribuciones

Las contribuciones son bienvenidas. Si identifica errores o tiene sugerencias de mejora, por favor, abra un "issue" o envíe un "pull request", saludos. Espero lo disfruten...

## Licencia

Este proyecto se distribuye bajo los términos de la licencia [Creative Commons Atribución-No Comercial-Sin Derivadas 4.0 Internacional (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/).

**Autor:** Alfonso Mosquera
**Correo electrónico:** alfomosque22@gmail.com