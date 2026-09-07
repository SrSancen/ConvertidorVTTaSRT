import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import os
import re
from datetime import datetime
import webbrowser

class VTTtoSRTConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Convertidor de Subtitulos VTT → SRT")
        self.root.geometry("700x600")
        self.root.minsize(600, 500)
        
        # Configurar tema Nordic
        self.setup_nordic_theme()
        
        # Variables
        self.input_file_path = tk.StringVar()
        self.output_folder_path = tk.StringVar()
        self.file_content = None
        self.original_filename = ""
        
        # Crear interfaz
        self.create_widgets()
        
        # Centrar ventana
        self.center_window()
    
    def setup_nordic_theme(self):
        """Configurar colores estilo Nordic"""
        self.colors = {
            'bg_primary': '#1e222a',
            'bg_secondary': '#2e3440',
            'bg_tertiary': '#3b4252',
            'bg_hover': '#434c5e',
            'bg_input': '#4c566a',
            'text_primary': '#e5e9f0',
            'text_secondary': '#d8dee9',
            'text_muted': '#81a1c1',
            'accent': '#88c0d0',
            'accent_hover': '#81a1c1',
            'success': '#a3be8c',
            'warning': '#ebcb8b',
            'error': '#bf616a',
            'border': '#4c566a'
        }
        
        # Configurar estilos ttk
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configurar colores para widgets ttk
        style.configure('TFrame', background=self.colors['bg_secondary'])
        style.configure('TLabel', background=self.colors['bg_secondary'], 
                       foreground=self.colors['text_primary'])
        style.configure('TButton', background=self.colors['bg_tertiary'],
                       foreground=self.colors['text_primary'],
                       borderwidth=1, focusthickness=3, focuscolor='none')
        style.map('TButton',
                 background=[('active', self.colors['bg_hover']),
                           ('pressed', self.colors['bg_input'])])
        
        # Configurar colores para la ventana principal
        self.root.configure(bg=self.colors['bg_secondary'])
    
    def center_window(self):
        """Centrar la ventana en la pantalla"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_widgets(self):
        # Frame principal con padding
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        title_frame = ttk.Frame(main_frame)
        title_frame.pack(fill=tk.X, pady=(0, 20))
        
        title_label = ttk.Label(title_frame, 
                               text="🎯 Convertidor de Subtitulos VTT → SRT",
                               font=('Segoe UI', 18, 'bold'))
        title_label.pack(side=tk.LEFT)
        
        badge = ttk.Label(title_frame, text="By SrSancen", 
                         font=('Segoe UI', 9, 'bold'),
                         foreground=self.colors['accent'])
        badge.pack(side=tk.RIGHT, padx=(10, 0))
        
        # Separador
        ttk.Separator(main_frame, orient='horizontal').pack(fill=tk.X, pady=(0, 20))
        
        # --- Selección de archivo ---
        file_frame = ttk.LabelFrame(main_frame, text="📂 Selecciona tu archivo .vtt", padding="15")
        file_frame.pack(fill=tk.X, pady=(0, 15))
        
        file_row = ttk.Frame(file_frame)
        file_row.pack(fill=tk.X)
        
        file_entry = ttk.Entry(file_row, textvariable=self.input_file_path,
                              font=('Consolas', 10))
        file_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
        file_btn = ttk.Button(file_row, text="📁 Seleccionar", 
                             command=self.select_input_file)
        file_btn.pack(side=tk.RIGHT)
        
        # --- Selección de carpeta de salida ---
        output_frame = ttk.LabelFrame(main_frame, text="💾 Selecciona la carpeta de destino", padding="15")
        output_frame.pack(fill=tk.X, pady=(0, 15))
        
        output_row = ttk.Frame(output_frame)
        output_row.pack(fill=tk.X)
        
        output_entry = ttk.Entry(output_row, textvariable=self.output_folder_path,
                                font=('Consolas', 10))
        output_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
        output_btn = ttk.Button(output_row, text="📁 Seleccionar",
                               command=self.select_output_folder)
        output_btn.pack(side=tk.RIGHT)
        
        # --- Botones de acción ---
        action_frame = ttk.Frame(main_frame)
        action_frame.pack(fill=tk.X, pady=(0, 15))
        
        convert_btn = ttk.Button(action_frame, text="⚡ Convertir",
                                command=self.convert_file,
                                style='Accent.TButton')
        convert_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        clear_btn = ttk.Button(action_frame, text="🗑️ Limpiar",
                              command=self.clear_all)
        clear_btn.pack(side=tk.LEFT)
        
        # Botón de abrir carpeta de salida
        open_folder_btn = ttk.Button(action_frame, text="📂 Abrir carpeta de destino",
                                    command=self.open_output_folder)
        open_folder_btn.pack(side=tk.RIGHT)
        
        # --- Log / Consola ---
        log_frame = ttk.LabelFrame(main_frame, text="📝 Registros", padding="10")
        log_frame.pack(fill=tk.BOTH, expand=True)
        
        self.log_text = scrolledtext.ScrolledText(
            log_frame,
            bg=self.colors['bg_tertiary'],
            fg=self.colors['text_secondary'],
            font=('Consolas', 9),
            height=10,
            wrap=tk.WORD,
            relief=tk.FLAT,
            borderwidth=0
        )
        self.log_text.pack(fill=tk.BOTH, expand=True)
        
        # Configurar tags para colores en el log
        self.log_text.tag_config('info', foreground=self.colors['text_muted'])
        self.log_text.tag_config('success', foreground=self.colors['success'])
        self.log_text.tag_config('error', foreground=self.colors['error'])
        self.log_text.tag_config('warning', foreground=self.colors['warning'])
        
        # Mensaje inicial
        self.log_message("Esperando archivo...", 'info')
        
        # --- Footer ---
        footer_frame = ttk.Frame(main_frame)
        footer_frame.pack(pady=(10, 0))
        
        # Texto del footer
        footer_text = "🔒 100% local · Sin servidores externos · "
        
        # Estilo del texto
        footer_label = ttk.Label(footer_frame, 
                                text=footer_text,
                                font=('Segoe UI', 8),
                                foreground=self.colors['text_muted'])
        footer_label.pack(side=tk.LEFT)
        
        # Texto con enlace
        link_label = tk.Label(footer_frame,
                             text="Código Fuente",
                             font=('Segoe UI', 8, 'underline'),
                             fg=self.colors['accent'],
                             bg=self.colors['bg_secondary'],
                             cursor='hand2')
        link_label.pack(side=tk.LEFT)
        link_label.bind('<Button-1>', lambda e: self.open_website())
        
    def open_website(self):
        """SrSancen Github"""
        webbrowser.open('https://github.com/SrSancen/ConvertidorVTTaSRT')
    
    def log_message(self, msg, msg_type='info'):
        """Agregar mensaje al log con timestamp"""
        timestamp = datetime.now().strftime('%H:%M:%S')
        
        icons = {
            'info': '📌',
            'success': '✅',
            'error': '❌',
            'warning': '⚠️'
        }
        icon = icons.get(msg_type, '📌')
        
        formatted_msg = f"[{timestamp}] {icon} {msg}\n"
        self.log_text.insert(tk.END, formatted_msg, msg_type)
        self.log_text.see(tk.END)
        self.root.update_idletasks()
    
    def select_input_file(self):
        """Seleccionar archivo .vtt de entrada"""
        file_path = filedialog.askopenfilename(
            title="Seleccionar archivo VTT",
            filetypes=[("Archivos VTT", "*.vtt"), ("Todos los archivos", "*.*")]
        )
        
        if file_path:
            self.input_file_path.set(file_path)
            self.log_message(f"Archivo seleccionado: {os.path.basename(file_path)}", 'info')
            
            # Si no hay carpeta de salida, usar la misma del archivo
            if not self.output_folder_path.get():
                output_dir = os.path.dirname(file_path)
                self.output_folder_path.set(output_dir)
                self.log_message(f"Carpeta de destino: {output_dir}", 'info')
            
            # Cargar el contenido del archivo
            self.load_file_content(file_path)
    
    def select_output_folder(self):
        """Seleccionar carpeta de destino"""
        folder_path = filedialog.askdirectory(
            title="Seleccionar carpeta de destino"
        )
        
        if folder_path:
            self.output_folder_path.set(folder_path)
            self.log_message(f"Carpeta de destino: {folder_path}", 'info')
    
    def load_file_content(self, file_path):
        """Cargar contenido del archivo VTT"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                self.file_content = f.read()
            
            self.original_filename = os.path.splitext(os.path.basename(file_path))[0]
            file_size = os.path.getsize(file_path)
            self.log_message(f"Archivo cargado: {file_size/1024:.1f} KB", 'success')
            
        except Exception as e:
            self.log_message(f"Error al cargar el archivo: {str(e)}", 'error')
            self.file_content = None
    
    def convert_vtt_to_srt(self, vtt_text):
        """Convertir contenido VTT a SRT"""
        lines = vtt_text.split('\n')
        
        # Eliminar BOM si existe
        if lines and lines[0].startswith('\ufeff'):
            lines[0] = lines[0][1:]
        
        # Eliminar cabecera WEBVTT y líneas vacías iniciales
        while lines and (lines[0].strip() == '' or lines[0].strip().upper() == 'WEBVTT'):
            lines.pop(0)
        while lines and lines[0].strip() == '':
            lines.pop(0)
        
        srt_lines = []
        index = 1
        i = 0
        
        while i < len(lines):
            # Saltar líneas vacías
            if lines[i].strip() == '':
                i += 1
                continue
            
            # Buscar línea de tiempo con " --> "
            if ' --> ' in lines[i]:
                # Convertir tiempos: '.' → ',' para milisegundos en SRT
                times = lines[i].strip().replace('.', ',')
                
                text_lines = []
                i += 1
                while i < len(lines) and lines[i].strip() != '' and ' --> ' not in lines[i]:
                    line = lines[i]
                    # Eliminar etiquetas HTML
                    line = re.sub(r'<[^>]+>', '', line).strip()
                    if line:
                        text_lines.append(line)
                    i += 1
                
                if text_lines:
                    srt_lines.append(str(index))
                    srt_lines.append(times)
                    srt_lines.append(' '.join(text_lines))
                    srt_lines.append('')
                    index += 1
            else:
                i += 1
        
        result = '\n'.join(srt_lines)
        return result.strip()
    
    def convert_file(self):
        """Ejecutar la conversión y guardar el archivo"""
        if not self.file_content:
            self.log_message("Primero selecciona un archivo .vtt", 'error')
            return
        
        if not self.output_folder_path.get():
            self.log_message("Selecciona una carpeta de destino", 'error')
            return
        
        try:
            self.log_message("Convirtiendo archivo...", 'info')
            srt_content = self.convert_vtt_to_srt(self.file_content)
            
            if not srt_content:
                self.log_message("La conversión generó un archivo vacío", 'error')
                return
            
            # Generar nombre de archivo de salida
            output_filename = f"{self.original_filename}.srt"
            output_path = os.path.join(self.output_folder_path.get(), output_filename)
            
            # Guardar archivo
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(srt_content)
            
            self.log_message(f"Archivo guardado: {output_filename}", 'success')
            self.log_message(f"Ubicación: {output_path}", 'info')
            
            # Mostrar vista previa
            preview_lines = srt_content.split('\n')[:8]
            preview = '\n'.join(preview_lines)
            if len(preview) > 200:
                preview = preview[:200] + '...'
            self.log_message(f"Vista previa:\n{preview}", 'info')
            
        except Exception as e:
            self.log_message(f"Error durante la conversión: {str(e)}", 'error')
    
    def open_output_folder(self):
        """Abrir la carpeta de destino en el explorador"""
        folder = self.output_folder_path.get()
        if folder and os.path.exists(folder):
            if os.name == 'nt':  # Windows
                os.startfile(folder)
            else:  # Mac/Linux
                os.system(f'open "{folder}"' if os.name == 'posix' else f'xdg-open "{folder}"')
            self.log_message(f"Abriendo carpeta: {folder}", 'info')
        else:
            self.log_message("Carpeta de destino no válida", 'error')
    
    def clear_all(self):
        """Limpiar todos los campos y resetear estado"""
        self.input_file_path.set('')
        self.output_folder_path.set('')
        self.file_content = None
        self.original_filename = ''
        self.log_text.delete(1.0, tk.END)
        self.log_message("Todo limpiado. Selecciona un archivo .vtt", 'info')

def main():
    root = tk.Tk()
    app = VTTtoSRTConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()