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
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout.strip() if result.returncode == 0 else result.stderr.strip()
    except Exception as e:
        return str(e)

devices_text = None
apps_text = None
app_entry = None

def show_progress(window, progress_bar, progress_label, total_steps):
    for i in range(total_steps + 1):
        progress_bar["value"] = i * (100 / total_steps)
        progress_label["text"] = f"{int(progress_bar['value'])}%"
        window.update_idletasks()
        time.sleep(0.01)

def list_devices():
    progress_window = tk.Toplevel(root)
    progress_window.title("Listando dispositivos...")
    progress_bar = ttk.Progressbar(progress_window, orient="horizontal", length=200, mode="determinate")
    progress_bar.pack(pady=10)
    progress_label = ttk.Label(progress_window, text="0%")
    progress_label.pack()
    show_progress(progress_window, progress_bar, progress_label, 100)
    output = execute_command("adb devices")
    devices_text.delete(1.0, tk.END)
    devices_text.insert(tk.END, output)
    messagebox.showinfo("Listar dispositivos", "Proceso completado.")
    progress_window.destroy()

def list_apps():
    progress_window = tk.Toplevel(root)
    progress_window.title("Listando aplicaciones...")
    progress_bar = ttk.Progressbar(progress_window, orient="horizontal", length=200, mode="determinate")
    progress_bar.pack(pady=10)
    progress_label = ttk.Label(progress_window, text="0%")
    progress_label.pack()
    show_progress(progress_window, progress_bar, progress_label, 100)
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
    apk_path = filedialog.askopenfilename(filetypes=[('Android APK', '*.apk')])
    if apk_path:
        progress_window = tk.Toplevel(root)
        progress_window.title("Instalando APK...")
        progress_bar = ttk.Progressbar(progress_window, orient="horizontal", length=200, mode="determinate")
        progress_bar.pack(pady=10)
        progress_label = ttk.Label(progress_window, text="0%")
        progress_label.pack()
        show_progress(progress_window, progress_bar, progress_label, 100)
        output = execute_command(f"adb install \"{apk_path}\"")
        messagebox.showinfo("Instalación APK", output)
        messagebox.showinfo("Instalar APK", "Proceso completado.")
        progress_window.destroy()

def uninstall_app():
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
            show_progress(progress_window, progress_bar, progress_label, 100)
            output = execute_command(f"adb uninstall {package}")
            messagebox.showinfo("Desinstalar App", output)
            messagebox.showinfo("Desinstalar aplicación", "Desinstalación completada.")
            progress_window.destroy()

def disable_app():
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
            show_progress(progress_window, progress_bar, progress_label, 100)
            output = execute_command(f"adb shell pm disable-user --user 0 {package}")
            messagebox.showinfo("Deshabilitar App", output)
            messagebox.showinfo("Deshabilitar aplicación", "Proceso completado.")
            progress_window.destroy()

def connect_device():
    ip = ip_entry.get().strip()
    port = port_entry.get().strip()
    progress_window = tk.Toplevel(root)
    progress_window.title("Conectando...")
    progress_bar = ttk.Progressbar(progress_window, orient="horizontal", length=200, mode="determinate")
    progress_bar.pack(pady=10)
    progress_label = ttk.Label(progress_window, text="0%")
    progress_label.pack()
    show_progress(progress_window, progress_bar, progress_label, 100)
    output = execute_command(f"adb connect {ip}:{port}")
    messagebox.showinfo("Conexión ADB", output)
    messagebox.showinfo("Conectar dispositivo", "Proceso completado.")
    progress_window.destroy()

def take_screenshot():
    progress_window = tk.Toplevel(root)
    progress_window.title("Tomando captura de pantalla...")
    progress_bar = ttk.Progressbar(progress_window, orient="horizontal", length=200, mode="determinate")
    progress_bar.pack(pady=10)
    progress_label = ttk.Label(progress_window, text="0%")
    progress_label.pack()
    show_progress(progress_window, progress_bar, progress_label, 100)
    try:
        filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if filename:
            output = execute_command(f"adb shell screencap -p /sdcard/screenshot.png && adb pull /sdcard/screenshot.png \"{filename}\"")
            messagebox.showinfo("Captura de pantalla", "Captura de pantalla guardada exitosamente.")
        else:
            messagebox.showinfo("Captura de pantalla", "Captura de pantalla cancelada.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al tomar captura de pantalla: {e}")
    messagebox.showinfo("Captura de pantalla", "Proceso completado.")
    progress_window.destroy()

def on_mouse_wheel(event):
    canvas.yview_scroll(-1 * (event.delta // 120), "units")

# Interfaz gráfica (modo compacto móvil)
root = tb.Window(themename="darkly")
root.title("Droid Specter")
root.geometry("360x640")  # Tamaño tipo app móvil
root.resizable(False, False)
root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))

try:
    icon_path = r"C:\PROYECTOS_Python\Droid Specter\Image\Droid_icono.ico"
    pil_image = Image.open(icon_path)
    pil_image = pil_image.resize((48, 48), Image.LANCZOS)
    png_image = ImageTk.PhotoImage(pil_image)
    root.iconphoto(True, png_image)
except Exception as e:
    messagebox.showerror("Error", f"No se pudo cargar el icono para la barra de título: {e}")

main_frame = ttk.Frame(root)
main_frame.pack(fill="both", expand=True)

main_frame.rowconfigure(0, weight=1)
main_frame.columnconfigure(0, weight=1)

canvas = tk.Canvas(main_frame)
canvas.grid(row=0, column=0, sticky="nsew")

scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
scrollbar.grid(row=0, column=1, sticky="ns")

scrollable_frame = ttk.Frame(canvas)
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"), width=e.width)
)

window_id = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

def resize_scrollable(event):
    canvas.itemconfig(window_id, width=event.width)

canvas.bind("<Configure>", resize_scrollable)

# Vincular el evento de la rueda del ratón al canvas
canvas.bind_all("<MouseWheel>", on_mouse_wheel)

icon_frame = ttk.Frame(scrollable_frame)
icon_frame.pack(pady=10)

icon_label = ttk.Label(icon_frame)
icon_label.pack()

base_path = r"C:\PROYECTOS_Python\Droid Specter\Image"
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
        pil_image = pil_image.resize((150, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(pil_image)
        icons.append(photo)
    except FileNotFoundError:
        messagebox.showerror("Error", f"No se encontró el archivo del icono: {path}")

current_icon_index = 0
def animate_icons():
    global current_icon_index
    if icons:
        icon_label.config(image=icons[current_icon_index])
        icon_label.image = icons[current_icon_index]
        current_icon_index = (current_icon_index + 1) % len(icons)
        root.after(200, animate_icons)

animate_icons()

# Nombre de la app con borde del color del icono
title_frame = tk.Frame(scrollable_frame, bg="#7B7BFF", padx=3, pady=3)
title_frame.pack(pady=10)

title_label = tk.Label(
    title_frame,
    text="Droid Specter",
    font=("SF Pro", 20, "bold"),
    fg="#7B7BFF",
    bg="#1e1e1e",
    padx=10,
    pady=5
)
title_label.pack()

ttk.Label(scrollable_frame, text="IP del dispositivo:").pack(fill="x", anchor="w", padx=10)
ip_entry = ttk.Entry(scrollable_frame)
ip_entry.pack(fill="x", pady=2, padx=10)

ttk.Label(scrollable_frame, text="Puerto:").pack(fill="x", anchor="w", padx=10)
port_entry = ttk.Entry(scrollable_frame)
port_entry.pack(fill="x", pady=2, padx=10)
port_entry.insert(0, "5555")

ttk.Button(scrollable_frame, text="Conectar", command=connect_device).pack(fill="x", pady=5, padx=10)
ttk.Button(scrollable_frame, text="Listar dispositivos", command=list_devices).pack(fill="x", pady=5, padx=10)
ttk.Button(scrollable_frame, text="Listar aplicaciones", command=list_apps).pack(fill="x", pady=5, padx=10)
ttk.Button(scrollable_frame, text="Captura de pantalla", command=take_screenshot).pack(fill="x", pady=5, padx=10)

devices_text = tk.Text(scrollable_frame, height=5, bg="#1e1e1e", fg="white")
devices_text.pack(fill="both", expand=True, pady=5, padx=10)

ttk.Button(scrollable_frame, text="Instalar APK", command=install_apk).pack(fill="x", pady=5, padx=10)

ttk.Label(scrollable_frame, text="Paquete de la aplicación:").pack(fill="x", anchor="w", padx=10)
app_entry = ttk.Entry(scrollable_frame)
app_entry.pack(fill="x", pady=2, padx=10)

ttk.Button(scrollable_frame, text="Deshabilitar", command=disable_app).pack(fill="x", pady=5, padx=10)
ttk.Button(scrollable_frame, text="Desinstalar", command=uninstall_app).pack(fill="x", pady=5, padx=10)

apps_text = tk.Text(scrollable_frame, height=5, bg="#1e1e1e", fg="white")
apps_text.pack(fill="both", expand=True, pady=5, padx=10)

root.mainloop()

# Derechos de autor (c) 2025, Alfonso Mosquera 
# Todos los derechos reservados.
# Cualquier copia o distribución de este software requiere el permiso del autor.
