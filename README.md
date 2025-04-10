
![banner](https://github.com/user-attachments/assets/e5a6ee23-3769-4a35-8df2-d303730df9a5)

# Droid Specter
Droid Specter es una herramienta desarrollada en Python que te permite tomar el control de tus dispositivos Android directamente desde tu PC.
Con una interfaz gráfica amigable, podrás gestionar tus dispositivos a través de ADB (Android Debug Bridge) de forma sencilla. 
Conecta tus dispositivos, visualiza las aplicaciones instaladas, instala o desinstala aplicaciones, e incluso deshabilita aquellas que no necesites, todo desde la comodidad de tu PC.

## ¿Qué hace Droid Specter?

- Permite conectarte fácilmente a cualquier dispositivo Android (teléfonos, tablets o Android TV) mediante ADB, ya sea por cable USB o por red Wi-Fi.
- Muestra la lista de aplicaciones instaladas en el dispositivo.
- Permite instalar archivos APK y desinstalar aplicaciones con un clic.
- Ofrece la opción de deshabilitar apps que no necesites, ayudando a optimizar el rendimiento del dispositivo.

---

## Requisitos del sistema

- Tener Python 3 instalado en tu PC.
- Tener ADB (Android Debug Bridge) correctamente configurado y accesible desde la terminal.
- Instalar las siguientes librerías de Python: `tkinter`, `ttkbootstrap`, `Pillow`.

---

## Instrucciones de instalación

### 1. Clonar el repositorio
```sh
git clone https://github.com/fonroot01/Droid-Specter.git
```

### 2. Instalar las dependencias
```sh
pip install ttkbootstrap Pillow
```

---

## Cómo ejecutar la aplicación

### Usando Python

1. Abre la terminal y navega a la carpeta del proyecto:
   ```sh
   cd Droid-Specter
   ```
2. Ejecuta el archivo principal:
   ```sh
   python Droid-Specter.py
   ```
3. Conecta tu dispositivo Android mediante USB o red Wi-Fi.
4. Usa la interfaz para gestionar las aplicaciones y configuraciones.

### Usando el archivo .exe (Windows)

1. Abre la carpeta `dist` y busca `Droid-Specter.exe`.
2. Haz doble clic para ejecutarlo.
3. Si aparece una advertencia de seguridad, selecciona "Ejecutar de todas formas".
4. Conecta tu dispositivo Android por USB o Wi-Fi y usa la interfaz.

---

## Conectar Android TV o cualquier dispositivo Android

1. Activa el modo desarrollador en tu Android TV (en “Acerca de”, toca varias veces “Número de compilación”).
2. Activa la depuración por USB o por red desde las opciones de desarrollador.
3. Asegúrete de que tu Android TV y tu PC estén conectados a la misma red Wi-Fi.
4. Busca la IP del Android TV en su configuración de red.
5. Ingresa esa IP y el puerto (por lo general, `5555`) en la app y haz clic en "Conectar".

---

### Interfaz Gráfica

![INTERFAZ](https://github.com/user-attachments/assets/b16bc481-4240-4378-9e18-03d48f16da20)

### Funciones
![FUNCIONES](https://github.com/user-attachments/assets/fd8e3bcc-6eea-4c13-a31e-5e5cd2e6092d)

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más información.

## Autor

Alfonso Mosquera - alfomosque22@gmail.com
