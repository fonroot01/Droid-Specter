# DroidSpecter

Droid Specter es una herramienta desarrollada en Python que te permite tomar el control de tus dispositivos Android directamente desde tu PC.
Con una interfaz gráfica amigable, podrás gestionar tus dispositivos a través de ADB (Android Debug Bridge) de forma sencilla.
Conecta tus dispositivos, visualiza las aplicaciones instaladas, captura la pantalla, instala o desinstala aplicaciones e incluso deshabilita aquellas que no necesites, todo desde la comodidad de tu PC.

## Funciones

- **Conexión Versátil:**
  - Conéctate con dispositivos Android, incluyendo teléfonos, tabletas y Android TV, mediante ADB a través de conexiones por cable o Wi-Fi.
- **Gestión de Aplicaciones:**
  - Obtén listados detallados de las aplicaciones instaladas en tus dispositivos.
  - Instala archivos APK de manera sencilla y desinstala aplicaciones con un solo clic.
- **Control Avanzado:**
  - Deshabilita aplicaciones según sea necesario para optimizar el rendimiento de tu dispositivo.

## Requisitos del Sistema

- **Python 3.x:** Asegúrate de tener Python instalado en tu PC.
- **Android Debug Bridge (ADB):** ADB debe estar configurado y accesible en tu entorno.
- **Dependencias de Python:** Las siguientes librerías deben estar instaladas: `tkinter`, `ttkbootstrap`, `Pillow`.

## Instrucciones de Instalación

### Clonación del Repositorio
```sh
git clone https://github.com/fonroot01/DroidSpecter.git
```

### Instalación de Dependencias
```sh
pip install ttkbootstrap Pillow
```

## Ejecución

### Desde el Código Fuente (Python)

1. Navega al directorio del repositorio clonado:
   ```sh
   cd DroidSpecter
   ```
2. Ejecuta el script principal:
   ```sh
   python DroidSpecter.py
   ```
3. Conéctate a tu dispositivo Android mediante ADB por USB o Wi-Fi.
4. Utiliza la interfaz gráfica para gestionar las aplicaciones y configuraciones del dispositivo.

### Desde el Archivo .exe (Windows)

1. Ubica el archivo `DroidSpecter.exe` en la carpeta `dist`.
2. Ejecuta el archivo `.exe` haciendo doble clic.
3. Si aparece una advertencia de seguridad de Windows, selecciona **"Ejecutar de todas formas"**.
4. Conéctate a tu dispositivo Android mediante ADB por USB o Wi-Fi.
5. Utiliza la interfaz gráfica para realizar las operaciones necesarias.

## Conexión a Android TV (O cualquier dispositivo Android)

1. **Modo Desarrollador:**
   - Activa el modo desarrollador en tu Android TV accediendo a "Acerca de" y presionando repetidamente "Número de compilación".
2. **Depuración ADB:**
   - Habilita la depuración por USB o la depuración por red en las opciones de desarrollador.
3. **Conexión de Red:**
   - Asegúrate de que tu Android TV y tu PC estén en la misma red Wi-Fi **(FUNDAMENTAL)**.
4. **Dirección IP:**
   - Busca la dirección IP de tu Android TV en la configuración de red.
5. **Conexión en Droid Specter:**
   - Ingresa la dirección IP y el puerto (generalmente `5555`) en Droid Specter y haz clic en "Conectar".

## Capturas de Pantalla

![Interfaz de usuario](https://github.com/user-attachments/assets/f07adff1-5060-4a31-aadd-67b3e94c0683)
![Conexión establecida](https://github.com/user-attachments/assets/6f015480-3783-4d8b-b8ef-606e94d72098)
![Permitir depuración por USB](https://github.com/user-attachments/assets/6678843a-d2c5-43d1-ac07-87d56de6aeb2)
![Selección de instalador APK](https://github.com/user-attachments/assets/6cd6c8ce-a773-46d3-9fa4-d56aaa232f1d)
![Confirmación de instalación](https://github.com/user-attachments/assets/672c93ab-bd3d-4b2a-9a3e-0db694f61621)

## Contribuciones

Las contribuciones son bienvenidas. Si identificas errores o tienes sugerencias de mejora, por favor, abre un "issue" o envía un "pull request".

## Licencia

Este proyecto se distribuye bajo los términos de la licencia [Creative Commons Atribución-No Comercial-Sin Derivadas 4.0 Internacional (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/).

## Autor

- **Nombre:** Alfonso Mosquera
- **Correo Electrónico:** alfomosque22@gmail.com
