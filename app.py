import customtkinter as ctk
from tkinter import messagebox
from youtube_downloader import download_youtube_content
from project_to_text import convert_project_to_text
from remove_background import remove_background
from files_downloads import download_file_from_drive, download_file_from_mega
from instagramTools import download_instagram_media
from pdf_tools import remove_pdf_password

class MultiToolApp:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Multi-Tool Utility")
        self.window.geometry("900x700")  
        
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("green")
        
        # Main container with increased padding
        self.main_container = ctk.CTkFrame(self.window, fg_color="transparent")
        self.main_container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Enhanced sidebar with better styling
        self.sidebar = ctk.CTkFrame(self.main_container, width=250)  # Wider sidebar
        self.sidebar.pack(side="left", fill="y", padx=10, pady=10)
        self.sidebar.pack_propagate(False)  # Prevent sidebar from shrinking
        
        # Content area with rounded corners and subtle border
        self.content_area = ctk.CTkFrame(self.main_container, corner_radius=20)
        self.content_area.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        self.progress_bar = None
        
        self._create_sidebar()
        self._create_welcome_screen()

    def _create_sidebar(self):
        # App title/logo area
        title_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        title_frame.pack(fill="x", pady=(20, 30))
        
        ctk.CTkLabel(title_frame, 
                    text="Multi-Tool", 
                    font=("Arial", 24, "bold")).pack()
        ctk.CTkLabel(title_frame, 
                    text="Utility Suite", 
                    font=("Arial", 16)).pack()

        # Separator
        separator = ctk.CTkFrame(self.sidebar, height=2, fg_color=["#666", "#999"])
        separator.pack(fill="x", padx=20, pady=(0, 20))

        # Tool buttons with enhanced styling
        tools = [
            ("YouTube Downloader", self.show_youtube_tools, "📺"),
            ("Convertir Proyecto", self.show_project_to_text, "📄"),
            ("Quitar Fondo Imagen", self.show_remove_background, "🖼"),
            ("Descargar Archivos", self.show_file_download_tools, "💾"),
            ("Herramientas PDF", self.show_pdf_tools, "📚"),
            ("Herramientas Instagram", self.show_instagram_tools, "📱"),
        ]
        
        for text, command, icon in tools:
            button = ctk.CTkButton(
                self.sidebar,
                text=f"{icon} {text}",
                command=command,
                height=45,
                corner_radius=8,
                font=("Arial", 14),
                fg_color="transparent",
                text_color=["#1f538d", "#2d7cd6"],
                hover_color=["#dae5f5", "#1a222d"]
            )
            button.pack(pady=5, padx=20, fill="x")

    def _clear_content(self):
        for widget in self.content_area.winfo_children():
            widget.destroy()

    def _create_welcome_screen(self):
        welcome_frame = ctk.CTkFrame(self.content_area, fg_color="transparent")
        welcome_frame.pack(fill="both", expand=True, padx=40, pady=40)
        
        # Welcome message with enhanced typography
        ctk.CTkLabel(
            welcome_frame,
            text="Bienvenido a Multi-Tool Utility",
            font=("Arial", 32, "bold")
        ).pack(pady=(0, 10))
        
        ctk.CTkLabel(
            welcome_frame,
            text="Selecciona una herramienta para comenzar",
            font=("Arial", 16)
        ).pack(pady=(0, 40))

        # Feature grid
        features_frame = ctk.CTkFrame(welcome_frame, fg_color="transparent")
        features_frame.pack(fill="x", padx=20)
        
        features = [
            ("📺 YouTube", "Descarga videos y audio"),
            ("📄 Proyectos", "Convierte proyectos a texto"),
            ("🖼 Imágenes", "Elimina fondos de imágenes"),
            ("💾 Archivos", "Descarga desde Drive y MEGA"),
            ("📚 PDF", "Gestiona archivos PDF"),
            ("📱 Instagram", "Descarga contenido de Instagram")
        ]

        for i, (title, desc) in enumerate(features):
            frame = ctk.CTkFrame(features_frame, corner_radius=10)
            frame.grid(row=i//2, column=i%2, padx=10, pady=10, sticky="nsew")
            
            ctk.CTkLabel(frame, text=title, font=("Arial", 16, "bold")).pack(pady=(15, 5))
            ctk.CTkLabel(frame, text=desc, font=("Arial", 12)).pack(pady=(0, 15))

        # Configure grid
        features_frame.grid_columnconfigure(0, weight=1)
        features_frame.grid_columnconfigure(1, weight=1)

    def show_youtube_tools(self):
        self._clear_content()
        frame = ctk.CTkFrame(self.content_area, fg_color="transparent")
        frame.pack(fill="both", expand=True, padx=40, pady=40)
        
        # Header
        ctk.CTkLabel(frame, text="YouTube Downloader", 
                    font=("Arial", 28, "bold")).pack(pady=(0, 30))
        
        # Input container
        input_frame = ctk.CTkFrame(frame, fg_color="transparent")
        input_frame.pack(fill="x", padx=20)
        
        self.url_input = ctk.CTkEntry(
            input_frame,
            placeholder_text="Ingresa URL de YouTube",
            height=45,
            font=("Arial", 14),
            width=500
        )
        self.url_input.pack(pady=(0, 20))
        
        # Progress bar with label
        progress_frame = ctk.CTkFrame(frame, fg_color="transparent")
        progress_frame.pack(fill="x", padx=20, pady=10)
        
        self.progress_bar = ctk.CTkProgressBar(progress_frame, width=500, height=15)
        self.progress_bar.pack()
        self.progress_bar.set(0)
        
        # Buttons container
        button_frame = ctk.CTkFrame(frame, fg_color="transparent")
        button_frame.pack(fill="x", padx=20, pady=20)
        
        ctk.CTkButton(
            button_frame,
            text="Descargar Video",
            command=lambda: self.download_youtube("video"),
            width=200,
            height=45,
            font=("Arial", 14),
            corner_radius=8
        ).pack(side="left", padx=10)
        
        ctk.CTkButton(
            button_frame,
            text="Descargar Audio",
            command=lambda: self.download_youtube("audio"),
            width=200,
            height=45,
            font=("Arial", 14),
            corner_radius=8
        ).pack(side="left", padx=10)

    # The rest of the methods remain unchanged as they're not part of the UI enhancement
    def download_youtube(self, type_download):
        url = self.url_input.get()
        if not url:
            messagebox.showerror("Error", "Por favor ingresa una URL de YouTube.")
            return
        messagebox.showinfo("Descarga iniciada", f"La descarga del {type_download} ha comenzado.")
        resultado = download_youtube_content(url, type_download, self.update_progress)
        if resultado == "Descarga completa":
            messagebox.showinfo("Descarga completa", f"{type_download.capitalize()} descargado con éxito.")
        else:
            messagebox.showerror("Error", f"No se pudo descargar el {type_download}. {resultado}")
        self.progress_bar.set(0)

    def update_progress(self, d):
        if d['status'] == 'downloading':
            downloaded = d.get('downloaded_bytes', 0)
            total = d.get('total_bytes', 1)
            progress = downloaded / total
            self.progress_bar.set(progress)

    def show_project_to_text(self):
        convert_project_to_text("../../laravel/cardioVascular", "estructura_importante_proyecto_cardio.txt")
        messagebox.showinfo("Completo", "Proyecto convertido a texto.")

    def show_remove_background(self):
        remove_background("input_image.png", "output_image.png")
        messagebox.showinfo("Completo", "Fondo eliminado de la imagen.")

    def show_file_download_tools(self):
        self._clear_content()
        frame = ctk.CTkFrame(self.content_area)
        frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        ctk.CTkLabel(frame, text="Descargar Archivos", font=("Arial", 24, "bold")).pack(pady=20)
        
        url_input = ctk.CTkEntry(frame, placeholder_text="Ingresa URL de Drive o MEGA", width=400)
        url_input.pack(pady=10)
        
        ctk.CTkButton(frame, text="Descargar de Google Drive",
                     command=lambda: download_file_from_drive(url_input.get())).pack(pady=5)
        ctk.CTkButton(frame, text="Descargar de MEGA",
                     command=lambda: download_file_from_mega(url_input.get())).pack(pady=5)

    def show_pdf_tools(self):
        self._clear_content()
        frame = ctk.CTkFrame(self.content_area)
        frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        ctk.CTkLabel(frame, text="Herramientas PDF", font=("Arial", 24, "bold")).pack(pady=20)
        
        ctk.CTkButton(frame, text="Quitar Contraseña de PDF",
                     command=lambda: remove_pdf_password("archivo_protegido.pdf", "archivo_sin_contraseña.pdf")).pack(pady=10)

    def show_instagram_tools(self):
        self._clear_content()
        frame = ctk.CTkFrame(self.content_area)
        frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        ctk.CTkLabel(frame, text="Herramientas Instagram", font=("Arial", 24, "bold")).pack(pady=20)
        
        url_input = ctk.CTkEntry(frame, placeholder_text="Ingresa URL de Instagram", width=400)
        url_input.pack(pady=10)
        
        ctk.CTkButton(frame, text="Descargar Imagen/Video",
                     command=lambda: download_instagram_media(url_input.get())).pack(pady=10)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = MultiToolApp()
    app.run()