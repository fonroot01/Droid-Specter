# Saludos, soy Alfonso y este proyecto fue hecho con mucho amor para ustedes, espero les sirva
# Puedes contactarme al siguiente correo para brindarte soporte o aclarar cualquier duda: alfomosque22@gmail.com

import os
import subprocess
import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
import tkinter.font as tkfont
import ttkbootstrap as tb
from PIL import Image, ImageTk
import time

def execute_command(command):
    """Ejecuta un comando en la terminal y devuelve la salida."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout.strip() if result.returncode == 0 else result.stderr.strip()
    except Exception as e:
        return str(e)

# Definición de variables globales
devices_text = None
apps_text = None
app_entry = None

def show_progress(window, progress_bar, progress_label, total_steps):
    """Muestra la barra de progreso."""
    for i in range(total_steps + 1):
        progress_bar["value"] = i * (100 / total_steps)
        progress_label["text"] = f"{int(progress_bar['value'])}%"
        window.update_idletasks()
        time.sleep(0.01)  # Simula el progreso

def list_devices():
    """Lista los dispositivos conectados."""
    progress_window = tk.Toplevel(root)
    progress_window.title("Listando dispositivos...")

    progress_bar = ttk.Progressbar(progress_window, orient="horizontal", length=200, mode="determinate")
    progress_bar.pack(pady=10)

    progress_label = ttk.Label(progress_window, text="0%")
    progress_label.pack()

    show_progress(progress_window, progress_bar, progress_label, 100)  # Simula 100 pasos

    output = execute_command("adb devices")
    devices_text.delete(1.0, tk.END)
    devices_text.insert(tk.END, output)

    messagebox.showinfo("Listar dispositivos", "Proceso completado.")
    progress_window.destroy()

def list_apps():
    """Lista las aplicaciones instaladas en el dispositivo."""
    progress_window = tk.Toplevel(root)
    progress_window.title("Listando aplicaciones...")

    progress_bar = ttk.Progressbar(progress_window, orient="horizontal", length=200, mode="determinate")
    progress_bar.pack(pady=10)

    progress_label = ttk.Label(progress_window, text="0%")
    progress_label.pack()

    show_progress(progress_window, progress_bar, progress_label, 100)  # Simula 100 pasos

    try:
        output = execute_command("adb shell pm list packages")
        if "error:" in output.lower():
            messagebox.showerror("Error", f"Error al listar aplicaciones: {output}")
        else:
            apps_text.delete(1.0, tk.END)
            apps_text.insert(tk.END, output)
    except Exception as e:
        messagebox.showerror("Error", f"Error al listar aplicaciones: {e}")

    messagebox.showinfo("Listar aplicaciones", "Proceso completado.")
    progress_window.destroy()

def install_apk():
    """Instala un APK en el dispositivo."""
    apk_path = filedialog.askopenfilename(filetypes=[('Android APK', '*.apk')])
    if apk_path:
        progress_window = tk.Toplevel(root)
        progress_window.title("Instalando APK...")

        progress_bar = ttk.Progressbar(progress_window, orient="horizontal", length=200, mode="determinate")
        progress_bar.pack(pady=10)

        progress_label = ttk.Label(progress_window, text="0%")
        progress_label.pack()

        show_progress(progress_window, progress_bar, progress_label, 100)  # Simula 100 pasos

        output = execute_command(f"adb install \"{apk_path}\"")
        messagebox.showinfo("Instalación APK", output)

        messagebox.showinfo("Instalar APK", "Proceso completado.")
        progress_window.destroy()

def uninstall_app():
    """Desinstala una aplicación en el dispositivo."""
    package = app_entry.get().strip()
    if package:
        confirm = messagebox.askyesno("Confirmar", f"¿Seguro que quieres desinstalar {package}?")
        if confirm:
            progress_window = tk.Toplevel(root)
            progress_window.title("Desinstalando aplicación...")

            progress_bar = ttk.Progressbar(progress_window, orient="horizontal", length=200, mode="determinate")
            progress_bar.pack(pady=10)

            progress_label = ttk.Label(progress_window, text="0%")
            progress_label.pack()

            show_progress(progress_window, progress_bar, progress_label, 100)  # Simula 100 pasos

            output = execute_command(f"adb uninstall {package}")
            messagebox.showinfo("Desinstalar App", output)

            messagebox.showinfo("Desinstalar aplicación", "Desinstalación completada.")
            progress_window.destroy()

def disable_app():
    """Deshabilita una aplicación en el dispositivo con barra de progreso."""
    package = app_entry.get().strip()
    if package:
        confirm = messagebox.askyesno("Confirmar", f"¿Seguro que quieres deshabilitar {package}?")
        if confirm:
            progress_window = tk.Toplevel(root)
            progress_window.title("Deshabilitando...")

            progress_bar = ttk.Progressbar(progress_window, orient="horizontal", length=200, mode="determinate")
            progress_bar.pack(pady=10)

            progress_label = ttk.Label(progress_window, text="0%")
            progress_label.pack()

            show_progress(progress_window, progress_bar, progress_label, 100)  # Simula 100 pasos

            output = execute_command(f"adb shell pm disable-user --user 0 {package}")
            messagebox.showinfo("Deshabilitar App", output)
            
            messagebox.showinfo("Deshabilitar aplicación", "Proceso completado.")
            progress_window.destroy()

def connect_device():
    """Conecta un dispositivo Android vía ADB."""
    ip = ip_entry.get().strip()
    port = port_entry.get().strip()

    progress_window = tk.Toplevel(root)
    progress_window.title("Conectando...")

    progress_bar = ttk.Progressbar(progress_window, orient="horizontal", length=200, mode="determinate")
    progress_bar.pack(pady=10)

    progress_label = ttk.Label(progress_window, text="0%")
    progress_label.pack()

    show_progress(progress_window, progress_bar, progress_label, 100)  # Simula 100 pasos

    output = execute_command(f"adb connect {ip}:{port}")
    messagebox.showinfo("Conexión ADB", output)

    messagebox.showinfo("Conectar dispositivo", "Proceso completado.")
    progress_window.destroy()

def take_screenshot():
    """Toma una captura de pantalla del dispositivo."""
    progress_window = tk.Toplevel(root)
    progress_window.title("Tomando captura de pantalla...")

    progress_bar = ttk.Progressbar(progress_window, orient="horizontal", length=200, mode="determinate")
    progress_bar.pack(pady=10)

    progress_label = ttk.Label(progress_window, text="0%")
    progress_label.pack()

    show_progress(progress_window, progress_bar, progress_label, 100)  # Simula 100 pasos

    try:
        filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if filename:
            output = execute_command(f"adb shell screencap -p /sdcard/screenshot.png && adb pull /sdcard/screenshot.png \"{filename}\"")
            messagebox.showinfo("Captura de pantalla", "Captura de pantalla guardada exitosamente.")
        else:
            messagebox.showinfo("Captura de pantalla", "Captura de pantalla cancelada.")
    except Exception as e:
        messagebox.showerror("Error " + f"Error al tomar captura de pantalla: {e}")
    messagebox.showinfo("Captura de pantalla", "Proceso completado.")
    progress_window.destroy()

# Interfaz gráfica
root = tb.Window(themename="darkly")
root.title("Droid Specter")
root.geometry("800x600")  # Ajuste de dimensiones
root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))

# Cargar el icono para la barra de título (usando PIL para convertir .ico a PNG y redimensionar)
try:
    icon_path = r"C:\Users\Alfonso\OneDrive\Escritorio\Auditorias\1 SCRIPTS PYTHON ORIENTADO A LA C-SEGURIDAD\Droid Specter\Image\Droid_icono.ico"
    pil_image = Image.open(icon_path)
    pil_image = Image.open(icon_path)
    pil_image = pil_image.resize((48, 48), Image.LANCZOS)
    png_image = ImageTk.PhotoImage(pil_image)
    root.iconphoto(True, png_image)
except Exception as e:
    messagebox.showerror("Error", f"No se pudo cargar el icono para la barra de título: {e}")

# Frame principal con grid

main_frame = ttk.Frame(root)
main_frame.pack(fill="both", expand=True)

main_frame.rowconfigure(0, weight=1)
main_frame.columnconfigure(0, weight=1)

canvas = tk.Canvas(main_frame)
canvas.grid(row=0, column=0, sticky="nsew")

scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
scrollbar.grid(row=0, column=1, sticky="ns")

scrollable_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

# Configurar el desplazamiento con la rueda del mouse
def scroll_with_mouse(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

canvas.bind_all("<MouseWheel>", scroll_with_mouse)

# Espacio para el icono de la app (animación)
icon_frame = ttk.Frame(scrollable_frame)
icon_frame.pack(pady=10)

icon_label = ttk.Label(icon_frame)
icon_label.pack()

# Cargar los iconos para la animación
base_path = r"C:\Users\Alfonso\OneDrive\Escritorio\Auditorias\1 SCRIPTS PYTHON ORIENTADO A LA C-SEGURIDAD\Droid Specter\Image"
icon_paths = [
    os.path.join(base_path, "Droid_imagen.png"),
    os.path.join(base_path, "Droid_imagen1.png"),
    os.path.join(base_path, "Droid_imagen2.png"),
    os.path.join(base_path, "Droid_imagen3.png"),
]
icons = []
for path in icon_paths:
    try:
        pil_image = Image.open(path)
        pil_image = pil_image.resize((250, 250), Image.LANCZOS)  # Cambiar a 250x250 píxeles
        photo = ImageTk.PhotoImage(pil_image)
        icons.append(photo)
    except FileNotFoundError:
        messagebox.showerror("Error", f"No se encontró el archivo del icono: {path}")

# Animación de iconos (sin cambio de color)
current_icon_index = 0
def animate_icons():
    global current_icon_index
    if icons:
        icon_label.config(image=icons[current_icon_index])
        icon_label.image = icons[current_icon_index]
        current_icon_index = (current_icon_index + 1) % len(icons)
        root.after(200, animate_icons)  # Cambia el icono cada 200 ms

animate_icons()  # Inicia la animación

# Nombre de la app en el espacio principal
app_name_label = ttk.Label(scrollable_frame, text="Droid Specter", font=("Lato", 24, "bold"))
app_name_label.pack(pady=20)# Entradas para conexión ADB
ttk.Label(scrollable_frame, text="IP del dispositivo:").pack(anchor="w")
ip_entry = ttk.Entry(scrollable_frame)
ip_entry.pack(fill="x", pady=2)

ttk.Label(scrollable_frame, text="Puerto:").pack(anchor="w")
port_entry = ttk.Entry(scrollable_frame) # Mover esta línea aquí
port_entry.pack(fill="x", pady=2)
port_entry.insert(0, "5555")

# Botones
ttk.Button(scrollable_frame, text="Conectar", command=connect_device).pack(fill="x", pady=5)
ttk.Button(scrollable_frame, text="Listar dispositivos", command=list_devices).pack(fill="x", pady=5)
ttk.Button(scrollable_frame, text="Listar aplicaciones", command=list_apps).pack(fill="x", pady=5)
ttk.Button(scrollable_frame, text="Captura de pantalla", command=take_screenshot).pack(fill="x", pady=5)

devices_text = tk.Text(scrollable_frame, height=5, bg="#1e1e1e", fg="white")
devices_text.pack(fill="both", expand=True, pady=5)

ttk.Button(scrollable_frame, text="Instalar APK", command=install_apk).pack(fill="x", pady=5)

ttk.Label(scrollable_frame, text="Paquete de la aplicación:").pack(anchor="w")
app_entry = ttk.Entry(scrollable_frame)
app_entry.pack(fill="x", pady=2)

ttk.Button(scrollable_frame, text="Deshabilitar", command=disable_app).pack(fill="x", pady=5)
ttk.Button(scrollable_frame, text="Desinstalar", command=uninstall_app).pack(fill="x", pady=5)

apps_text = tk.Text(scrollable_frame, height=5, bg="#1e1e1e", fg="white")
apps_text.pack(fill="both", expand=True, pady=5)

root.mainloop()

# Derechos de autor (c) 2025, Alfonso Mosquera 
# Todos los derechos reservados.

# Cualquier copia o distribucion de este software requiere el permiso del autor.