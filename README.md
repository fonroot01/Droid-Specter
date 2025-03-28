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
https://github.com/fonroot01/Droid-Specter.git
```

### Instalación de Dependencias
```sh
pip install ttkbootstrap Pillow
```

## Ejecución

### Desde el Código Fuente (Python)

1. Navega al directorio del repositorio clonado:
   ```sh
   cd Droid_Specter
   ```
2. Ejecuta el script principal:
   ```sh
   python Droid-Specter.py
   ```
3. Conéctate a tu dispositivo Android mediante ADB por USB o Wi-Fi.
4. Utiliza la interfaz gráfica para gestionar las aplicaciones y configuraciones del dispositivo.

### Desde el Archivo .exe (Windows)

1. Ubica el archivo `Droid-Specter.exe` en la carpeta `dist`.
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
### Interfaz
![1_Interfaz](https://github.com/user-attachments/assets/9f8abe5b-8b3c-4a31-8df4-2ddf8d632c6b)

### Ingreso de IP
![2_IP_y_Conexion](https://github.com/user-attachments/assets/b4118293-ccd2-40ed-93ff-773cb0ac8c28)

### Permitir depuracion por USB
![3_Permitir depuracion por USB](https://github.com/user-attachments/assets/bd19b427-56c4-4e70-a6ef-63e37a23f97f)

### Conexion establecida
![4_Conexion establecida](https://github.com/user-attachments/assets/f99cd2d7-780f-4b13-bf25-9b70c56f59bd)

### Opcion para buscar APK
![5_I_APK](https://github.com/user-attachments/assets/2aa17eeb-71b7-47b0-a498-5c4d1661bd0a)

### Buscamos e instalamos
![6_Se busca el instalador APK](https://github.com/user-attachments/assets/553c7fe3-4a53-4c4a-beff-52bf2d66aab0)

### APK Instalado
![7_APK_Instalado](https://github.com/user-attachments/assets/03fb2ea3-dc77-417c-a593-99e21f8eb18b)

### Validamos que se haya instalado
![8_Instalacion correcta](https://github.com/user-attachments/assets/521f08b7-143e-46fa-b26a-46b317c66121)

### Excelente, app instala!!!
![Listo](https://github.com/user-attachments/assets/73890a9f-a233-492b-916b-f946214fbcfd)


## Contribuciones

Las contribuciones son bienvenidas. Si identificas errores o tienes sugerencias de mejora, por favor, abre un "issue" o envía un "pull request".

## Licencia

Este proyecto se distribuye bajo los términos de la licencia [Creative Commons Atribución-No Comercial-Sin Derivadas 4.0 Internacional (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/).

## Autor

- **Nombre:** Alfonso Mosquera
- **Correo Electrónico:** alfomosque22@gmail.com
