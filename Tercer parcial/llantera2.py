import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import os
from datetime import datetime
from typing import Dict, List, Any

class LlanteraStyles:
    """Estilos modernos para la aplicación de llantera"""
    
    # Colores específicos para llantera
    PRIMARY = "#1a237e"        # Azul profundo
    SECONDARY = "#3949ab"      # Azul medio
    ACCENT = "#ff6f00"         # Naranja (color llanta)
    SUCCESS = "#2e7d32"        # Verde
    WARNING = "#f57c00"        # Naranja oscuro
    DANGER = "#c62828"         # Rojo
    
    # Colores de fondo
    BG_PRIMARY = "#f5f5f5"     # Gris claro
    BG_CARD = "#ffffff"        # Blanco
    BG_HOVER = "#e3f2fd"       # Azul muy claro
    
    # Texto
    TEXT_PRIMARY = "#212121"
    TEXT_SECONDARY = "#757575"
    TEXT_WHITE = "#ffffff"

class DataManager:
    """Gestor de datos JSON para la llantera"""
    
    def __init__(self, filename="llantera_data.json"):
        self.filename = filename
        self.data = self.cargar_datos()
    
    def cargar_datos(self) -> Dict[str, Any]:
        """Carga datos desde archivo JSON"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                pass
        
        # Datos iniciales para llantera
        return {
            "llantas": [
                {"id": 1, "marca": "Michelin", "modelo": "Primacy 4", "medida": "205/55R16", 
                 "precio": 2500.0, "stock": 20, "categoria": "Turismo"},
                {"id": 2, "marca": "Bridgestone", "modelo": "Turanza T005", "medida": "225/45R17", 
                 "precio": 3200.0, "stock": 15, "categoria": "Turismo"},
                {"id": 3, "marca": "Continental", "modelo": "CrossContact", "medida": "265/70R16", 
                 "precio": 4500.0, "stock": 8, "categoria": "SUV"},
                {"id": 4, "marca": "Pirelli", "modelo": "Scorpion Verde", "medida": "235/60R18", 
                 "precio": 5200.0, "stock": 12, "categoria": "SUV"},
                {"id": 5, "marca": "Goodyear", "modelo": "EfficientGrip", "medida": "195/65R15", 
                 "precio": 1800.0, "stock": 3, "categoria": "Económica"}
            ],
            "servicios": [
                {"id": 1, "nombre": "Montaje de llantas", "precio": 150.0},
                {"id": 2, "nombre": "Balanceo", "precio": 80.0},
                {"id": 3, "nombre": "Alineación", "precio": 200.0},
                {"id": 4, "nombre": "Rotación de llantas", "precio": 100.0},
                {"id": 5, "nombre": "Revisión de presión", "precio": 50.0}
            ],
            "ventas": [],
            "clientes": [],
            "citas": []
        }
    
    def guardar_datos(self):
        """Guarda datos en archivo JSON"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar: {e}")

class SistemaLlantera:
    """Sistema principal de gestión para llantera"""
    
    def __init__(self):
        self.data_manager = DataManager()
        self.usuario_actual = None
        self.root = None
        
        # Usuarios del sistema
        self.usuarios = {
            "admin": {"password": "admin123", "rol": "Administrador"},
            "ventas": {"password": "ventas123", "rol": "Vendedor"},
            "gerente": {"password": "gerente123", "rol": "Gerente"},
            "mecanico": {"password": "mec123", "rol": "Mecánico"}
        }
    
    def iniciar_aplicacion(self):
        """Inicia la aplicación con login"""
        self.ventana_login()
    
    def ventana_login(self):
        """Ventana de inicio de sesión"""
        login_window = tk.Tk()
        login_window.title("🛞 Sistema Llantera - Login")
        login_window.geometry("400x500")
        login_window.configure(bg=LlanteraStyles.BG_PRIMARY)
        login_window.resizable(False, False)
        
        # Centrar ventana
        login_window.eval('tk::PlaceWindow . center')
        
        # Frame principal
        main_frame = tk.Frame(login_window, bg=LlanteraStyles.BG_CARD, padx=40, pady=40)
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Logo/Título
        title_label = tk.Label(main_frame, text="🛞 LlanteraPardo", 
                              font=("Arial", 24, "bold"), 
                              fg=LlanteraStyles.PRIMARY, bg=LlanteraStyles.BG_CARD)
        title_label.pack(pady=(0, 30))
        
        subtitle_label = tk.Label(main_frame, text="Sistema de Gestión", 
                                 font=("Arial", 12), 
                                 fg=LlanteraStyles.TEXT_SECONDARY, bg=LlanteraStyles.BG_CARD)
        subtitle_label.pack(pady=(0, 40))
        
        # Campos de entrada
        tk.Label(main_frame, text="Usuario:", font=("Arial", 12, "bold"), 
                fg=LlanteraStyles.TEXT_PRIMARY, bg=LlanteraStyles.BG_CARD).pack(anchor='w', pady=(0, 5))
        
        entry_usuario = tk.Entry(main_frame, font=("Arial", 12), width=25, relief='flat', bd=10)
        entry_usuario.pack(pady=(0, 20), ipady=8)
        
        tk.Label(main_frame, text="Contraseña:", font=("Arial", 12, "bold"), 
                fg=LlanteraStyles.TEXT_PRIMARY, bg=LlanteraStyles.BG_CARD).pack(anchor='w', pady=(0, 5))
        
        entry_password = tk.Entry(main_frame, font=("Arial", 12), width=25, show="*", relief='flat', bd=10)
        entry_password.pack(pady=(0, 30), ipady=8)
        
        def login():
            usuario = entry_usuario.get().strip()
            password = entry_password.get().strip()
            
            if usuario in self.usuarios and self.usuarios[usuario]["password"] == password:
                self.usuario_actual = {"username": usuario, "rol": self.usuarios[usuario]["rol"]}
                login_window.destroy()
                self.ventana_principal()
            else:
                messagebox.showerror("Error", "Usuario o contraseña incorrectos")
        
        # Botón de login
        btn_login = tk.Button(main_frame, text="INGRESAR", command=login,
                             font=("Arial", 12, "bold"), fg=LlanteraStyles.TEXT_WHITE,
                             bg=LlanteraStyles.PRIMARY, width=20, height=2,
                             relief='flat', cursor='hand2')
        btn_login.pack(pady=(0, 20))
        
        # Info de usuarios
        info_frame = tk.Frame(main_frame, bg=LlanteraStyles.BG_CARD)
        info_frame.pack(fill='x', pady=20)
        
        tk.Label(info_frame, text="Usuarios de prueba:", font=("Arial", 10, "bold"), 
                fg=LlanteraStyles.TEXT_SECONDARY, bg=LlanteraStyles.BG_CARD).pack()
        
        usuarios_info = [
            "admin / admin123 (Administrador)",
            "ventas / ventas123 (Vendedor)",
            "gerente / gerente123 (Gerente)",
            "mecanico / mec123 (Mecánico)"
        ]
        
        for info in usuarios_info:
            tk.Label(info_frame, text=info, font=("Arial", 9), 
                    fg=LlanteraStyles.TEXT_SECONDARY, bg=LlanteraStyles.BG_CARD).pack()
        
        # Enter para login
        entry_password.bind('<Return>', lambda e: login())
        entry_usuario.focus()
        
        login_window.mainloop()
    
    def ventana_principal(self):
        """Ventana principal del sistema"""
        self.root = tk.Tk()
        self.root.title(f"🛞 Llantera Pro - {self.usuario_actual['rol']}")
        self.root.geometry("1400x800")
        self.root.configure(bg=LlanteraStyles.BG_PRIMARY)
        self.root.state('zoomed')  # Maximizada
        
        # Barra superior
        self.crear_barra_superior()
        
        # Contenedor principal
        self.main_container = tk.Frame(self.root, bg=LlanteraStyles.BG_PRIMARY)
        self.main_container.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Sidebar
        self.crear_sidebar()
        
        # Área de contenido
        self.content_frame = tk.Frame(self.main_container, bg=LlanteraStyles.BG_CARD, relief='raised', bd=1)
        self.content_frame.pack(side='right', fill='both', expand=True, padx=(10, 0))
        
        # Mostrar dashboard inicial
        self.mostrar_dashboard()
        
        self.root.mainloop()
    
    def crear_barra_superior(self):
        """Crea la barra superior con información del usuario"""
        top_bar = tk.Frame(self.root, bg=LlanteraStyles.PRIMARY, height=60)
        top_bar.pack(fill='x')
        top_bar.pack_propagate(False)
        
        # Título
        title_label = tk.Label(top_bar, text="🛞 LLANTERA PRO", 
                              font=("Arial", 18, "bold"), 
                              fg=LlanteraStyles.TEXT_WHITE, bg=LlanteraStyles.PRIMARY)
        title_label.pack(side='left', padx=20, pady=15)
        
        # Info usuario
        user_info = tk.Label(top_bar, 
                            text=f"👤 {self.usuario_actual['username']} - {self.usuario_actual['rol']}", 
                            font=("Arial", 12), 
                            fg=LlanteraStyles.TEXT_WHITE, bg=LlanteraStyles.PRIMARY)
        user_info.pack(side='right', padx=20, pady=15)
        
        # Fecha/hora
        fecha_actual = datetime.now().strftime("%d/%m/%Y - %H:%M")
        date_label = tk.Label(top_bar, text=f"📅 {fecha_actual}", 
                             font=("Arial", 10), 
                             fg=LlanteraStyles.TEXT_WHITE, bg=LlanteraStyles.PRIMARY)
        date_label.pack(side='right', padx=20, pady=15)
    
    def crear_sidebar(self):
        """Crea el menú lateral"""
        sidebar = tk.Frame(self.main_container, bg=LlanteraStyles.BG_CARD, width=250, relief='raised', bd=1)
        sidebar.pack(side='left', fill='y')
        sidebar.pack_propagate(False)
        
        # Título del menú
        menu_title = tk.Label(sidebar, text="MENÚ PRINCIPAL", 
                             font=("Arial", 14, "bold"), 
                             fg=LlanteraStyles.TEXT_PRIMARY, bg=LlanteraStyles.BG_CARD)
        menu_title.pack(pady=20)
        
        # Opciones de menú según rol
        menu_options = self.obtener_opciones_menu()
        
        self.menu_buttons = {}
        for option, (text, icon, command) in menu_options.items():
            btn = tk.Button(sidebar, text=f"{icon} {text}", 
                           command=command, font=("Arial", 11), 
                           fg=LlanteraStyles.TEXT_PRIMARY, bg=LlanteraStyles.BG_CARD,
                           width=28, height=2, anchor='w', padx=20,
                           relief='flat', cursor='hand2',
                           activebackground=LlanteraStyles.BG_HOVER)
            btn.pack(pady=2, padx=10, fill='x')
            self.menu_buttons[option] = btn
        
        # Botón de cerrar sesión
        tk.Frame(sidebar, height=20, bg=LlanteraStyles.BG_CARD).pack(fill='x')
        
        btn_logout = tk.Button(sidebar, text="🚪 Cerrar Sesión", 
                              command=self.cerrar_sesion,
                              font=("Arial", 11, "bold"), 
                              fg=LlanteraStyles.TEXT_WHITE, bg=LlanteraStyles.DANGER,
                              width=28, height=2, relief='flat', cursor='hand2')
        btn_logout.pack(side='bottom', pady=20, padx=10, fill='x')
    
    def obtener_opciones_menu(self) -> Dict[str, tuple]:
        """Retorna las opciones de menú según el rol del usuario"""
        base_options = {
            "dashboard": ("Dashboard", "📊", self.mostrar_dashboard)
        }
        
        rol = self.usuario_actual['rol']
        
        if rol == "Administrador":
            base_options.update({
                "llantas": ("Gestión Llantas", "🛞", self.mostrar_llantas),
                "servicios": ("Servicios", "🔧", self.mostrar_servicios),
                "ventas": ("Punto de Venta", "🛒", self.mostrar_ventas),
                "reportes": ("Reportes", "📈", self.mostrar_reportes),
                "citas": ("Citas", "📅", self.mostrar_citas)
            })
        elif rol == "Vendedor":
            base_options.update({
                "llantas": ("Consultar Llantas", "🛞", self.mostrar_llantas),
                "ventas": ("Punto de Venta", "🛒", self.mostrar_ventas),
                "citas": ("Citas", "📅", self.mostrar_citas)
            })
        elif rol == "Gerente":
            base_options.update({
                "llantas": ("Consultar Llantas", "🛞", self.mostrar_llantas),
                "reportes": ("Reportes", "📈", self.mostrar_reportes),
                "servicios": ("Servicios", "🔧", self.mostrar_servicios)
            })
        elif rol == "Mecánico":
            base_options.update({
                "servicios": ("Servicios", "🔧", self.mostrar_servicios),
                "citas": ("Citas del Día", "📅", self.mostrar_citas)
            })
        
        return base_options
    
    def limpiar_contenido(self):
        """Limpia el área de contenido"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def crear_tarjeta_estadistica(self, parent, titulo, valor, icono, color):
        """Crea una tarjeta de estadística"""
        card = tk.Frame(parent, bg=color, relief='raised', bd=2)
        card.pack(side='left', fill='both', expand=True, padx=10, pady=10)
        
        # Icono
        icon_label = tk.Label(card, text=icono, font=("Arial", 24), 
                             fg=LlanteraStyles.TEXT_WHITE, bg=color)
        icon_label.pack(pady=(20, 10))
        
        # Valor
        value_label = tk.Label(card, text=str(valor), font=("Arial", 20, "bold"), 
                              fg=LlanteraStyles.TEXT_WHITE, bg=color)
        value_label.pack()
        
        # Título
        title_label = tk.Label(card, text=titulo, font=("Arial", 12), 
                              fg=LlanteraStyles.TEXT_WHITE, bg=color)
        title_label.pack(pady=(5, 20))
        
        return card
    
    def mostrar_dashboard(self):
        """Muestra el dashboard principal"""
        self.limpiar_contenido()
        
        # Título
        title_frame = tk.Frame(self.content_frame, bg=LlanteraStyles.BG_CARD)
        title_frame.pack(fill='x', padx=20, pady=20)
        
        tk.Label(title_frame, text="📊 DASHBOARD PRINCIPAL", 
                font=("Arial", 18, "bold"), 
                fg=LlanteraStyles.PRIMARY, bg=LlanteraStyles.BG_CARD).pack(anchor='w')
        
        # Estadísticas principales
        stats_frame = tk.Frame(self.content_frame, bg=LlanteraStyles.BG_CARD, height=150)
        stats_frame.pack(fill='x', padx=20, pady=10)
        stats_frame.pack_propagate(False)
        
        # Calcular estadísticas
        llantas = self.data_manager.data['llantas']
        ventas = self.data_manager.data['ventas']
        total_llantas = len(llantas)
        stock_bajo = len([l for l in llantas if l.get('stock', 0) <= 5])
        total_ventas = len(ventas)
        ingresos_hoy = sum(v.get('total', 0) for v in ventas 
                          if v.get('fecha', '').startswith(datetime.now().strftime('%Y-%m-%d')))
        
        # Tarjetas de estadísticas
        self.crear_tarjeta_estadistica(stats_frame, "Total Llantas", total_llantas, "🛞", LlanteraStyles.PRIMARY)
        self.crear_tarjeta_estadistica(stats_frame, "Stock Bajo", stock_bajo, "⚠️", LlanteraStyles.WARNING)
        self.crear_tarjeta_estadistica(stats_frame, "Ventas Hoy", total_ventas, "🛒", LlanteraStyles.SUCCESS)
        self.crear_tarjeta_estadistica(stats_frame, f"Ingresos Hoy\n${ingresos_hoy:,.2f}", "", "💰", LlanteraStyles.ACCENT)
        
        # Lista de llantas con stock bajo
        if stock_bajo > 0:
            warning_frame = tk.Frame(self.content_frame, bg=LlanteraStyles.BG_CARD)
            warning_frame.pack(fill='both', expand=True, padx=20, pady=20)
            
            tk.Label(warning_frame, text="⚠️ LLANTAS CON STOCK BAJO", 
                    font=("Arial", 14, "bold"), 
                    fg=LlanteraStyles.DANGER, bg=LlanteraStyles.BG_CARD).pack(anchor='w', pady=(0, 10))
            
            # Tabla de stock bajo
            columns = ('Marca', 'Modelo', 'Medida', 'Stock', 'Precio')
            tree = ttk.Treeview(warning_frame, columns=columns, show='headings', height=8)
            
            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, width=120)
            
            for llanta in llantas:
                if llanta.get('stock', 0) <= 5:
                    tree.insert('', 'end', values=(
                        llanta.get('marca', ''),
                        llanta.get('modelo', ''),
                        llanta.get('medida', ''),
                        llanta.get('stock', 0),
                        f"${llanta.get('precio', 0):,.2f}"
                    ))
            
            tree.pack(fill='both', expand=True)
            
            # Scrollbar
            scrollbar = ttk.Scrollbar(warning_frame, orient='vertical', command=tree.yview)
            scrollbar.pack(side='right', fill='y')
            tree.configure(yscrollcommand=scrollbar.set)
    
    def mostrar_llantas(self):
        """Muestra la gestión de llantas"""
        self.limpiar_contenido()
        
        # Título
        title_frame = tk.Frame(self.content_frame, bg=LlanteraStyles.BG_CARD)
        title_frame.pack(fill='x', padx=20, pady=20)
        
        tk.Label(title_frame, text="🛞 GESTIÓN DE LLANTAS", 
                font=("Arial", 18, "bold"), 
                fg=LlanteraStyles.PRIMARY, bg=LlanteraStyles.BG_CARD).pack(side='left')
        
        # Botones de acción (solo para admin)
        if self.usuario_actual['rol'] == "Administrador":
            btn_frame = tk.Frame(title_frame, bg=LlanteraStyles.BG_CARD)
            btn_frame.pack(side='right')
            
            tk.Button(btn_frame, text="➕ Nueva Llanta", command=self.nueva_llanta,
                     font=("Arial", 10, "bold"), fg=LlanteraStyles.TEXT_WHITE,
                     bg=LlanteraStyles.SUCCESS, padx=20, pady=5, 
                     relief='flat', cursor='hand2').pack(side='left', padx=5)
            
            tk.Button(btn_frame, text="🔄 Actualizar Stock", command=self.actualizar_stock,
                     font=("Arial", 10, "bold"), fg=LlanteraStyles.TEXT_WHITE,
                     bg=LlanteraStyles.SECONDARY, padx=20, pady=5, 
                     relief='flat', cursor='hand2').pack(side='left', padx=5)
        
        # Tabla de llantas
        table_frame = tk.Frame(self.content_frame, bg=LlanteraStyles.BG_CARD)
        table_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        columns = ('ID', 'Marca', 'Modelo', 'Medida', 'Categoría', 'Stock', 'Precio')
        self.tree_llantas = ttk.Treeview(table_frame, columns=columns, show='headings')
        
        for col in columns:
            self.tree_llantas.heading(col, text=col)
            if col == 'ID':
                self.tree_llantas.column(col, width=50)
            elif col == 'Precio':
                self.tree_llantas.column(col, width=100)
            elif col == 'Stock':
                self.tree_llantas.column(col, width=80)
            else:
                self.tree_llantas.column(col, width=130)
        
        # Cargar datos
        self.cargar_llantas()
        
        self.tree_llantas.pack(fill='both', expand=True)
        
        # Scrollbar
        scrollbar_v = ttk.Scrollbar(table_frame, orient='vertical', command=self.tree_llantas.yview)
        scrollbar_v.pack(side='right', fill='y')
        self.tree_llantas.configure(yscrollcommand=scrollbar_v.set)
        
        # Menú contextual para admin
        if self.usuario_actual['rol'] == "Administrador":
            self.tree_llantas.bind('<Button-3>', self.menu_contextual_llantas)
    
    def cargar_llantas(self):
        """Carga las llantas en la tabla"""
        # Limpiar tabla
        for item in self.tree_llantas.get_children():
            self.tree_llantas.delete(item)
        
        # Cargar datos
        for llanta in self.data_manager.data['llantas']:
            stock = llanta.get('stock', 0)
            # Colorear filas con stock bajo
            tags = ('stock_bajo',) if stock <= 5 else ()
            
            self.tree_llantas.insert('', 'end', values=(
                llanta.get('id', ''),
                llanta.get('marca', ''),
                llanta.get('modelo', ''),
                llanta.get('medida', ''),
                llanta.get('categoria', ''),
                stock,
                f"${llanta.get('precio', 0):,.2f}"
            ), tags=tags)
        
        # Configurar tags
        self.tree_llantas.tag_configure('stock_bajo', background='#ffebee')
    
    def nueva_llanta(self):
        """Diálogo para agregar nueva llanta"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Nueva Llanta")
        dialog.geometry("400x500")
        dialog.configure(bg=LlanteraStyles.BG_CARD)
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Centrar diálogo
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (400 // 2)
        y = (dialog.winfo_screenheight() // 2) - (500 // 2)
        dialog.geometry(f"400x500+{x}+{y}")
        
        # Campos
        fields = {}
        
        tk.Label(dialog, text="NUEVA LLANTA", font=("Arial", 16, "bold"), 
                fg=LlanteraStyles.PRIMARY, bg=LlanteraStyles.BG_CARD).pack(pady=20)
        
        # Crear campos
        campos = [
            ("Marca:", "marca"),
            ("Modelo:", "modelo"),
            ("Medida:", "medida"),
            ("Categoría:", "categoria"),
            ("Stock:", "stock"),
            ("Precio:", "precio")
        ]
        
        for label_text, field_name in campos:
            frame = tk.Frame(dialog, bg=LlanteraStyles.BG_CARD)
            frame.pack(fill='x', padx=40, pady=10)
            
            tk.Label(frame, text=label_text, font=("Arial", 11, "bold"), 
                    fg=LlanteraStyles.TEXT_PRIMARY, bg=LlanteraStyles.BG_CARD).pack(anchor='w')
            
            entry = tk.Entry(frame, font=("Arial", 11), width=30)
            entry.pack(fill='x', pady=(5, 0))
            fields[field_name] = entry
        
        def guardar_llanta():
            try:
                # Validar datos
                marca = fields['marca'].get().strip()
                modelo = fields['modelo'].get().strip()
                medida = fields['medida'].get().strip()
                categoria = fields['categoria'].get().strip()
                stock = int(fields['stock'].get().strip())
                precio = float(fields['precio'].get().strip())
                
                if not all([marca, modelo, medida, categoria]):
                    raise ValueError("Todos los campos son obligatorios")
                
                if stock < 0 or precio <= 0:
                    raise ValueError("Stock y precio deben ser valores válidos")
                
                # Generar ID
                llantas = self.data_manager.data['llantas']
                nuevo_id = max([l.get('id', 0) for l in llantas], default=0) + 1
                
                # Crear nueva llanta
                nueva_llanta = {
                    'id': nuevo_id,
                    'marca': marca,
                    'modelo': modelo,
                    'medida': medida,
                    'categoria': categoria,
                    'stock': stock,
                    'precio': precio
                }
                
                llantas.append(nueva_llanta)
                self.data_manager.guardar_datos()
                self.cargar_llantas()
                
                dialog.destroy()
                messagebox.showinfo("Éxito", "Llanta agregada correctamente")
                
            except ValueError as e:
                messagebox.showerror("Error", str(e))
        
        # Botones
        btn_frame = tk.Frame(dialog, bg=LlanteraStyles.BG_CARD)
        btn_frame.pack(pady=30)
        
        tk.Button(btn_frame, text="Guardar", command=guardar_llanta,
                 font=("Arial", 12, "bold"), fg=LlanteraStyles.TEXT_WHITE,
                 bg=LlanteraStyles.SUCCESS, padx=30, pady=10, 
                 relief='flat', cursor='hand2').pack(side='left', padx=10)
        
        tk.Button(btn_frame, text="Cancelar", command=dialog.destroy,
                 font=("Arial", 12, "bold"), fg=LlanteraStyles.TEXT_WHITE,
                 bg=LlanteraStyles.DANGER, padx=30, pady=10, 
                 relief='flat', cursor='hand2').pack(side='left', padx=10)
    
    def actualizar_stock(self):
        """Diálogo para actualizar stock de llanta seleccionada"""
        selected = self.tree_llantas.selection()
        if not selected:
            messagebox.showwarning("Advertencia", "Seleccione una llanta")
            return
        
        item = self.tree_llantas.item(selected[0])
        llanta_id = int(item['values'][0])
        
        # Encontrar la llanta
        llanta = next((l for l in self.data_manager.data['llantas'] if l['id'] == llanta_id), None)
        if not llanta:
            return
        
        nuevo_stock = simpledialog.askinteger("Actualizar Stock", 
                                            f"Stock actual: {llanta['stock']}\nNuevo stock:",
                                            minvalue=0, maxvalue=1000)
        if nuevo_stock is not None:
            llanta['stock'] = nuevo_stock
            self.data_manager.guardar_datos()
            self.cargar_llantas()
            messagebox.showinfo("Éxito", "Stock actualizado correctamente")
    
    def menu_contextual_llantas(self, event):
        """Menú contextual para llantas"""
        selected = self.tree_llantas.selection()
        if not selected:
            return
        
        menu = tk.Menu(self.root, tearoff=0)
        menu.add_command(label="✏️ Editar", command=self.editar_llanta)
        menu.add_command(label="🗑️ Eliminar", command=self.eliminar_llanta)
        menu.add_separator()
        menu.add_command(label="📦 Actualizar Stock", command=self.actualizar_stock)
        
        try:
            menu.tk_popup(event.x_root, event.y_root)
        finally:
            menu.grab_release()
    
    def editar_llanta(self):
        """Editar llanta seleccionada"""
        selected = self.tree_llantas.selection()
        if not selected:
            return
        
        item = self.tree_llantas.item(selected[0])
        llanta_id = int(item['values'][0])
        
        # Encontrar la llanta
        llanta = next((l for l in self.data_manager.data['llantas'] if l['id'] == llanta_id), None)
        if not llanta:
            return
        
        # Diálogo de edición similar a nueva_llanta pero con datos precargados
        dialog = tk.Toplevel(self.root)
        dialog.title("Editar Llanta")
        dialog.geometry("400x500")
        dialog.configure(bg=LlanteraStyles.BG_CARD)
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Centrar diálogo
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (400 // 2)
        y = (dialog.winfo_screenheight() // 2) - (500 // 2)
        dialog.geometry(f"400x500+{x}+{y}")
        
        # Campos
        fields = {}
        
        tk.Label(dialog, text="EDITAR LLANTA", font=("Arial", 16, "bold"), 
                fg=LlanteraStyles.PRIMARY, bg=LlanteraStyles.BG_CARD).pack(pady=20)
        
        # Crear campos con datos actuales
        campos = [
            ("Marca:", "marca", llanta.get('marca', '')),
            ("Modelo:", "modelo", llanta.get('modelo', '')),
            ("Medida:", "medida", llanta.get('medida', '')),
            ("Categoría:", "categoria", llanta.get('categoria', '')),
            ("Stock:", "stock", str(llanta.get('stock', 0))),
            ("Precio:", "precio", str(llanta.get('precio', 0)))
        ]
        
        for label_text, field_name, current_value in campos:
            frame = tk.Frame(dialog, bg=LlanteraStyles.BG_CARD)
            frame.pack(fill='x', padx=40, pady=10)
            
            tk.Label(frame, text=label_text, font=("Arial", 11, "bold"), 
                    fg=LlanteraStyles.TEXT_PRIMARY, bg=LlanteraStyles.BG_CARD).pack(anchor='w')
            
            entry = tk.Entry(frame, font=("Arial", 11), width=30)
            entry.pack(fill='x', pady=(5, 0))
            entry.insert(0, current_value)
            fields[field_name] = entry
        
        def actualizar_llanta():
            try:
                # Validar datos
                marca = fields['marca'].get().strip()
                modelo = fields['modelo'].get().strip()
                medida = fields['medida'].get().strip()
                categoria = fields['categoria'].get().strip()
                stock = int(fields['stock'].get().strip())
                precio = float(fields['precio'].get().strip())
                
                if not all([marca, modelo, medida, categoria]):
                    raise ValueError("Todos los campos son obligatorios")
                
                if stock < 0 or precio <= 0:
                    raise ValueError("Stock y precio deben ser valores válidos")
                
                # Actualizar llanta
                llanta.update({
                    'marca': marca,
                    'modelo': modelo,
                    'medida': medida,
                    'categoria': categoria,
                    'stock': stock,
                    'precio': precio
                })
                
                self.data_manager.guardar_datos()
                self.cargar_llantas()
                
                dialog.destroy()
                messagebox.showinfo("Éxito", "Llanta actualizada correctamente")
                
            except ValueError as e:
                messagebox.showerror("Error", str(e))
        
        # Botones
        btn_frame = tk.Frame(dialog, bg=LlanteraStyles.BG_CARD)
        btn_frame.pack(pady=30)
        
        tk.Button(btn_frame, text="Actualizar", command=actualizar_llanta,
                 font=("Arial", 12, "bold"), fg=LlanteraStyles.TEXT_WHITE,
                 bg=LlanteraStyles.SUCCESS, padx=30, pady=10, 
                 relief='flat', cursor='hand2').pack(side='left', padx=10)
        
        tk.Button(btn_frame, text="Cancelar", command=dialog.destroy,
                 font=("Arial", 12, "bold"), fg=LlanteraStyles.TEXT_WHITE,
                 bg=LlanteraStyles.DANGER, padx=30, pady=10, 
                 relief='flat', cursor='hand2').pack(side='left', padx=10)
    
    def eliminar_llanta(self):
        """Eliminar llanta seleccionada"""
        selected = self.tree_llantas.selection()
        if not selected:
            return
        
        item = self.tree_llantas.item(selected[0])
        llanta_id = int(item['values'][0])
        
        if messagebox.askyesno("Confirmar", "¿Está seguro de eliminar esta llanta?"):
            self.data_manager.data['llantas'] = [l for l in self.data_manager.data['llantas'] 
                                               if l['id'] != llanta_id]
            self.data_manager.guardar_datos()
            self.cargar_llantas()
            messagebox.showinfo("Éxito", "Llanta eliminada correctamente")
    
    def mostrar_servicios(self):
        """Muestra la gestión de servicios"""
        self.limpiar_contenido()
        
        # Título
        title_frame = tk.Frame(self.content_frame, bg=LlanteraStyles.BG_CARD)
        title_frame.pack(fill='x', padx=20, pady=20)
        
        tk.Label(title_frame, text="🔧 SERVICIOS DE LLANTERA", 
                font=("Arial", 18, "bold"), 
                fg=LlanteraStyles.PRIMARY, bg=LlanteraStyles.BG_CARD).pack(side='left')
        
        # Botón de nuevo servicio (solo para admin)
        if self.usuario_actual['rol'] == "Administrador":
            tk.Button(title_frame, text="➕ Nuevo Servicio", command=self.nuevo_servicio,
                     font=("Arial", 10, "bold"), fg=LlanteraStyles.TEXT_WHITE,
                     bg=LlanteraStyles.SUCCESS, padx=20, pady=5, 
                     relief='flat', cursor='hand2').pack(side='right')
        
        # Tabla de servicios
        table_frame = tk.Frame(self.content_frame, bg=LlanteraStyles.BG_CARD)
        table_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        columns = ('ID', 'Servicio', 'Precio')
        self.tree_servicios = ttk.Treeview(table_frame, columns=columns, show='headings')
        
        for col in columns:
            self.tree_servicios.heading(col, text=col)
            if col == 'ID':
                self.tree_servicios.column(col, width=80)
            elif col == 'Precio':
                self.tree_servicios.column(col, width=150)
            else:
                self.tree_servicios.column(col, width=300)
        
        # Cargar servicios
        for servicio in self.data_manager.data['servicios']:
            self.tree_servicios.insert('', 'end', values=(
                servicio.get('id', ''),
                servicio.get('nombre', ''),
                f"${servicio.get('precio', 0):,.2f}"
            ))
        
        self.tree_servicios.pack(fill='both', expand=True)
        
        # Scrollbar
        scrollbar_v = ttk.Scrollbar(table_frame, orient='vertical', command=self.tree_servicios.yview)
        scrollbar_v.pack(side='right', fill='y')
        self.tree_servicios.configure(yscrollcommand=scrollbar_v.set)
        
        # Menú contextual para admin
        if self.usuario_actual['rol'] == "Administrador":
            self.tree_servicios.bind('<Button-3>', self.menu_contextual_servicios)
    
    def nuevo_servicio(self):
        """Diálogo para agregar nuevo servicio"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Nuevo Servicio")
        dialog.geometry("350x300")
        dialog.configure(bg=LlanteraStyles.BG_CARD)
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Centrar diálogo
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (350 // 2)
        y = (dialog.winfo_screenheight() // 2) - (300 // 2)
        dialog.geometry(f"350x300+{x}+{y}")
        
        tk.Label(dialog, text="NUEVO SERVICIO", font=("Arial", 16, "bold"), 
                fg=LlanteraStyles.PRIMARY, bg=LlanteraStyles.BG_CARD).pack(pady=20)
        
        # Campos
        frame_nombre = tk.Frame(dialog, bg=LlanteraStyles.BG_CARD)
        frame_nombre.pack(fill='x', padx=40, pady=10)
        
        tk.Label(frame_nombre, text="Nombre del servicio:", font=("Arial", 11, "bold"), 
                fg=LlanteraStyles.TEXT_PRIMARY, bg=LlanteraStyles.BG_CARD).pack(anchor='w')
        
        entry_nombre = tk.Entry(frame_nombre, font=("Arial", 11), width=30)
        entry_nombre.pack(fill='x', pady=(5, 0))
        
        frame_precio = tk.Frame(dialog, bg=LlanteraStyles.BG_CARD)
        frame_precio.pack(fill='x', padx=40, pady=10)
        
        tk.Label(frame_precio, text="Precio:", font=("Arial", 11, "bold"), 
                fg=LlanteraStyles.TEXT_PRIMARY, bg=LlanteraStyles.BG_CARD).pack(anchor='w')
        
        entry_precio = tk.Entry(frame_precio, font=("Arial", 11), width=30)
        entry_precio.pack(fill='x', pady=(5, 0))
        
        def guardar_servicio():
            try:
                nombre = entry_nombre.get().strip()
                precio = float(entry_precio.get().strip())
                
                if not nombre:
                    raise ValueError("El nombre del servicio es obligatorio")
                
                if precio <= 0:
                    raise ValueError("El precio debe ser mayor a 0")
                
                # Generar ID
                servicios = self.data_manager.data['servicios']
                nuevo_id = max([s.get('id', 0) for s in servicios], default=0) + 1
                
                # Crear nuevo servicio
                nuevo_servicio = {
                    'id': nuevo_id,
                    'nombre': nombre,
                    'precio': precio
                }
                
                servicios.append(nuevo_servicio)
                self.data_manager.guardar_datos()
                
                dialog.destroy()
                self.mostrar_servicios()  # Recargar vista
                messagebox.showinfo("Éxito", "Servicio agregado correctamente")
                
            except ValueError as e:
                messagebox.showerror("Error", str(e))
        
        # Botones
        btn_frame = tk.Frame(dialog, bg=LlanteraStyles.BG_CARD)
        btn_frame.pack(pady=30)
        
        tk.Button(btn_frame, text="Guardar", command=guardar_servicio,
                 font=("Arial", 12, "bold"), fg=LlanteraStyles.TEXT_WHITE,
                 bg=LlanteraStyles.SUCCESS, padx=30, pady=10, 
                 relief='flat', cursor='hand2').pack(side='left', padx=10)
        
        tk.Button(btn_frame, text="Cancelar", command=dialog.destroy,
                 font=("Arial", 12, "bold"), fg=LlanteraStyles.TEXT_WHITE,
                 bg=LlanteraStyles.DANGER, padx=30, pady=10, 
                 relief='flat', cursor='hand2').pack(side='left', padx=10)
    
    def menu_contextual_servicios(self, event):
        """Menú contextual para servicios"""
        selected = self.tree_servicios.selection()
        if not selected:
            return
        
        menu = tk.Menu(self.root, tearoff=0)
        menu.add_command(label="✏️ Editar Precio", command=self.editar_precio_servicio)
        menu.add_command(label="🗑️ Eliminar", command=self.eliminar_servicio)
        
        try:
            menu.tk_popup(event.x_root, event.y_root)
        finally:
            menu.grab_release()
    
    def editar_precio_servicio(self):
        """Editar precio de servicio seleccionado"""
        selected = self.tree_servicios.selection()
        if not selected:
            return
        
        item = self.tree_servicios.item(selected[0])
        servicio_id = int(item['values'][0])
        
        # Encontrar el servicio
        servicio = next((s for s in self.data_manager.data['servicios'] if s['id'] == servicio_id), None)
        if not servicio:
            return
        
        nuevo_precio = simpledialog.askfloat("Editar Precio", 
                                           f"Servicio: {servicio['nombre']}\nPrecio actual: ${servicio['precio']:.2f}\nNuevo precio:",
                                           minvalue=0.01, maxvalue=10000.0)
        if nuevo_precio is not None:
            servicio['precio'] = nuevo_precio
            self.data_manager.guardar_datos()
            self.mostrar_servicios()  # Recargar vista
            messagebox.showinfo("Éxito", "Precio actualizado correctamente")
    
    def eliminar_servicio(self):
        """Eliminar servicio seleccionado"""
        selected = self.tree_servicios.selection()
        if not selected:
            return
        
        item = self.tree_servicios.item(selected[0])
        servicio_id = int(item['values'][0])
        
        if messagebox.askyesno("Confirmar", "¿Está seguro de eliminar este servicio?"):
            self.data_manager.data['servicios'] = [s for s in self.data_manager.data['servicios'] 
                                                 if s['id'] != servicio_id]
            self.data_manager.guardar_datos()
            self.mostrar_servicios()  # Recargar vista
            messagebox.showinfo("Éxito", "Servicio eliminado correctamente")
    
    def mostrar_ventas(self):
        """Muestra el punto de venta"""
        self.limpiar_contenido()
        
        # Título
        title_frame = tk.Frame(self.content_frame, bg=LlanteraStyles.BG_CARD)
        title_frame.pack(fill='x', padx=20, pady=20)
        
        tk.Label(title_frame, text="🛒 PUNTO DE VENTA", 
                font=("Arial", 18, "bold"), 
                fg=LlanteraStyles.PRIMARY, bg=LlanteraStyles.BG_CARD).pack()
        
        # Contenedor principal dividido
        main_container = tk.Frame(self.content_frame, bg=LlanteraStyles.BG_CARD)
        main_container.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Panel izquierdo - Productos
        left_panel = tk.Frame(main_container, bg=LlanteraStyles.BG_CARD, relief='raised', bd=1)
        left_panel.pack(side='left', fill='both', expand=True, padx=(0, 10))
        
        tk.Label(left_panel, text="LLANTAS DISPONIBLES", font=("Arial", 14, "bold"), 
                fg=LlanteraStyles.PRIMARY, bg=LlanteraStyles.BG_CARD).pack(pady=10)
        
        # Tabla de llantas disponibles
        columns_productos = ('ID', 'Marca', 'Modelo', 'Medida', 'Stock', 'Precio')
        self.tree_productos_venta = ttk.Treeview(left_panel, columns=columns_productos, show='headings', height=15)
        
        for col in columns_productos:
            self.tree_productos_venta.heading(col, text=col)
            if col == 'ID':
                self.tree_productos_venta.column(col, width=40)
            elif col in ['Stock']:
                self.tree_productos_venta.column(col, width=60)
            elif col == 'Precio':
                self.tree_productos_venta.column(col, width=100)
            else:
                self.tree_productos_venta.column(col, width=120)
        
        # Cargar productos disponibles
        for llanta in self.data_manager.data['llantas']:
            if llanta.get('stock', 0) > 0:  # Solo mostrar con stock
                self.tree_productos_venta.insert('', 'end', values=(
                    llanta.get('id', ''),
                    llanta.get('marca', ''),
                    llanta.get('modelo', ''),
                    llanta.get('medida', ''),
                    llanta.get('stock', 0),
                    f"${llanta.get('precio', 0):,.2f}"
                ))
        
        self.tree_productos_venta.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Botón agregar al carrito
        tk.Button(left_panel, text="🛒 Agregar al Carrito", command=self.agregar_al_carrito,
                 font=("Arial", 12, "bold"), fg=LlanteraStyles.TEXT_WHITE,
                 bg=LlanteraStyles.SUCCESS, padx=20, pady=10, 
                 relief='flat', cursor='hand2').pack(pady=10)
        
        # Panel derecho - Carrito
        right_panel = tk.Frame(main_container, bg=LlanteraStyles.BG_CARD, relief='raised', bd=1, width=400)
        right_panel.pack(side='right', fill='y')
        right_panel.pack_propagate(False)
        
        tk.Label(right_panel, text="CARRITO DE COMPRAS", font=("Arial", 14, "bold"), 
                fg=LlanteraStyles.PRIMARY, bg=LlanteraStyles.BG_CARD).pack(pady=10)
        
        # Tabla del carrito
        columns_carrito = ('Producto', 'Cant.', 'Precio', 'Total')
        self.tree_carrito = ttk.Treeview(right_panel, columns=columns_carrito, show='headings', height=10)
        
        for col in columns_carrito:
            self.tree_carrito.heading(col, text=col)
            if col == 'Cant.':
                self.tree_carrito.column(col, width=50)
            elif col in ['Precio', 'Total']:
                self.tree_carrito.column(col, width=80)
            else:
                self.tree_carrito.column(col, width=140)
        
        self.tree_carrito.pack(fill='x', padx=10, pady=10)
        
        # Inicializar carrito
        self.carrito = []
        
        # Botones del carrito
        btn_carrito_frame = tk.Frame(right_panel, bg=LlanteraStyles.BG_CARD)
        btn_carrito_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Button(btn_carrito_frame, text="🗑️ Quitar", command=self.quitar_del_carrito,
                 font=("Arial", 10), fg=LlanteraStyles.TEXT_WHITE,
                 bg=LlanteraStyles.DANGER, padx=15, pady=5, 
                 relief='flat', cursor='hand2').pack(side='left', padx=5)
        
        tk.Button(btn_carrito_frame, text="🧹 Limpiar", command=self.limpiar_carrito,
                 font=("Arial", 10), fg=LlanteraStyles.TEXT_WHITE,
                 bg=LlanteraStyles.WARNING, padx=15, pady=5, 
                 relief='flat', cursor='hand2').pack(side='left', padx=5)
        
        # Total
        self.total_frame = tk.Frame(right_panel, bg=LlanteraStyles.PRIMARY, relief='raised', bd=2)
        self.total_frame.pack(fill='x', padx=10, pady=20)
        
        self.label_total = tk.Label(self.total_frame, text="TOTAL: $0.00", 
                                   font=("Arial", 16, "bold"), 
                                   fg=LlanteraStyles.TEXT_WHITE, bg=LlanteraStyles.PRIMARY)
        self.label_total.pack(pady=15)
        
        # Datos del cliente
        cliente_frame = tk.Frame(right_panel, bg=LlanteraStyles.BG_CARD)
        cliente_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Label(cliente_frame, text="DATOS DEL CLIENTE", font=("Arial", 12, "bold"), 
                fg=LlanteraStyles.TEXT_PRIMARY, bg=LlanteraStyles.BG_CARD).pack()
        
        tk.Label(cliente_frame, text="Nombre:", font=("Arial", 10), 
                fg=LlanteraStyles.TEXT_PRIMARY, bg=LlanteraStyles.BG_CARD).pack(anchor='w', padx=5)
        
        self.entry_cliente_nombre = tk.Entry(cliente_frame, font=("Arial", 10), width=30)
        self.entry_cliente_nombre.pack(fill='x', padx=5, pady=2)
        
        tk.Label(cliente_frame, text="Teléfono:", font=("Arial", 10), 
                fg=LlanteraStyles.TEXT_PRIMARY, bg=LlanteraStyles.BG_CARD).pack(anchor='w', padx=5)
        
        self.entry_cliente_telefono = tk.Entry(cliente_frame, font=("Arial", 10), width=30)
        self.entry_cliente_telefono.pack(fill='x', padx=5, pady=2)
        
        # Botón de venta
        tk.Button(right_panel, text="💰 PROCESAR VENTA", command=self.procesar_venta,
                 font=("Arial", 14, "bold"), fg=LlanteraStyles.TEXT_WHITE,
                 bg=LlanteraStyles.ACCENT, padx=20, pady=15, 
                 relief='flat', cursor='hand2').pack(fill='x', padx=10, pady=20)
    
    def agregar_al_carrito(self):
        """Agregar producto seleccionado al carrito"""
        selected = self.tree_productos_venta.selection()
        if not selected:
            messagebox.showwarning("Advertencia", "Seleccione una llanta")
            return
        
        item = self.tree_productos_venta.item(selected[0])
        llanta_id = int(item['values'][0])
        
        # Encontrar la llanta
        llanta = next((l for l in self.data_manager.data['llantas'] if l['id'] == llanta_id), None)
        if not llanta or llanta.get('stock', 0) <= 0:
            messagebox.showerror("Error", "Llanta no disponible")
            return
        
        # Pedir cantidad
        cantidad = simpledialog.askinteger("Cantidad", 
                                         f"Stock disponible: {llanta['stock']}\nCantidad a agregar:",
                                         minvalue=1, maxvalue=llanta['stock'])
        if cantidad is None:
            return
        
        # Verificar si ya está en el carrito
        for i, item_carrito in enumerate(self.carrito):
            if item_carrito['id'] == llanta_id:
                nueva_cantidad = item_carrito['cantidad'] + cantidad
                if nueva_cantidad > llanta['stock']:
                    messagebox.showerror("Error", "Cantidad excede el stock disponible")
                    return
                self.carrito[i]['cantidad'] = nueva_cantidad
                break
        else:
            # Agregar nuevo item al carrito
            self.carrito.append({
                'id': llanta_id,
                'marca': llanta['marca'],
                'modelo': llanta['modelo'],
                'medida': llanta['medida'],
                'precio': llanta['precio'],
                'cantidad': cantidad
            })
        
        self.actualizar_carrito()
    
    def actualizar_carrito(self):
        """Actualiza la vista del carrito"""
        # Limpiar carrito
        for item in self.tree_carrito.get_children():
            self.tree_carrito.delete(item)
        
        total = 0
        for item in self.carrito:
            producto = f"{item['marca']} {item['modelo']} {item['medida']}"
            subtotal = item['precio'] * item['cantidad']
            total += subtotal
            
            self.tree_carrito.insert('', 'end', values=(
                producto,
                item['cantidad'],
                f"${item['precio']:,.2f}",
                f"${subtotal:,.2f}"
            ))
        
        self.label_total.config(text=f"TOTAL: ${total:,.2f}")
    
    def quitar_del_carrito(self):
        """Quitar item seleccionado del carrito"""
        selected = self.tree_carrito.selection()
        if not selected:
            messagebox.showwarning("Advertencia", "Seleccione un item")
            return
        
        index = self.tree_carrito.index(selected[0])
        del self.carrito[index]
        self.actualizar_carrito()
    
    def limpiar_carrito(self):
        """Limpiar todo el carrito"""
        if self.carrito and messagebox.askyesno("Confirmar", "¿Limpiar todo el carrito?"):
            self.carrito.clear()
            self.actualizar_carrito()
    
    def procesar_venta(self):
        """Procesar la venta actual"""
        if not self.carrito:
            messagebox.showwarning("Advertencia", "El carrito está vacío")
            return
        
        nombre_cliente = self.entry_cliente_nombre.get().strip()
        telefono_cliente = self.entry_cliente_telefono.get().strip()
        
        if not nombre_cliente:
            messagebox.showwarning("Advertencia", "Ingrese el nombre del cliente")
            return
        
        try:
            # Calcular total
            total = sum(item['precio'] * item['cantidad'] for item in self.carrito)
            
            # Verificar stock disponible
            for item in self.carrito:
                llanta = next((l for l in self.data_manager.data['llantas'] if l['id'] == item['id']), None)
                if not llanta or llanta.get('stock', 0) < item['cantidad']:
                    messagebox.showerror("Error", f"Stock insuficiente para {item['marca']} {item['modelo']}")
                    return
            
            # Confirmar venta
            if not messagebox.askyesno("Confirmar Venta", f"Total: ${total:,.2f}\n¿Procesar venta?"):
                return
            
            # Actualizar stock
            for item in self.carrito:
                llanta = next((l for l in self.data_manager.data['llantas'] if l['id'] == item['id']), None)
                if llanta:
                    llanta['stock'] -= item['cantidad']
            
            # Registrar venta
            venta_id = len(self.data_manager.data['ventas']) + 1
            venta = {
                'id': venta_id,
                'fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'cliente': nombre_cliente,
                'telefono': telefono_cliente,
                'items': self.carrito.copy(),
                'total': total,
                'vendedor': self.usuario_actual['username']
            }
            
            self.data_manager.data['ventas'].append(venta)
            
            # Registrar cliente si es nuevo
            clientes = self.data_manager.data['clientes']
            if not any(c.get('nombre') == nombre_cliente for c in clientes):
                cliente = {
                    'id': len(clientes) + 1,
                    'nombre': nombre_cliente,
                    'telefono': telefono_cliente,
                    'fecha_registro': datetime.now().strftime('%Y-%m-%d')
                }
                clientes.append(cliente)
            
            # Guardar datos
            self.data_manager.guardar_datos()
            
            # Limpiar carrito y campos
            self.carrito.clear()
            self.actualizar_carrito()
            self.entry_cliente_nombre.delete(0, tk.END)
            self.entry_cliente_telefono.delete(0, tk.END)
            
            # Actualizar tabla de productos
            self.mostrar_ventas()  # Recargar vista
            
            messagebox.showinfo("Éxito", f"Venta procesada correctamente\nTicket #{venta_id}\nTotal: ${total:,.2f}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al procesar venta: {str(e)}")
    
    def mostrar_reportes(self):
        """Muestra los reportes y estadísticas"""
        self.limpiar_contenido()
        
        # Título
        title_frame = tk.Frame(self.content_frame, bg=LlanteraStyles.BG_CARD)
        title_frame.pack(fill='x', padx=20, pady=20)
        
        tk.Label(title_frame, text="📈 REPORTES Y ESTADÍSTICAS", 
                font=("Arial", 18, "bold"), 
                fg=LlanteraStyles.PRIMARY, bg=LlanteraStyles.BG_CARD).pack()
        
        # Contenedor principal
        main_container = tk.Frame(self.content_frame, bg=LlanteraStyles.BG_CARD)
        main_container.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Estadísticas generales
        stats_frame = tk.Frame(main_container, bg=LlanteraStyles.BG_CARD)
        stats_frame.pack(fill='x', pady=20)
        
        # Calcular estadísticas
        llantas = self.data_manager.data['llantas']
        ventas = self.data_manager.data['ventas']
        clientes = self.data_manager.data['clientes']
        
        total_llantas = len(llantas)
        total_stock = sum(l.get('stock', 0) for l in llantas)
        total_ventas = len(ventas)
        total_ingresos = sum(v.get('total', 0) for v in ventas)
        total_clientes = len(clientes)
        
        # Ventas del día
        hoy = datetime.now().strftime('%Y-%m-%d')
        ventas_hoy = [v for v in ventas if v.get('fecha', '').startswith(hoy)]
        ingresos_hoy = sum(v.get('total', 0) for v in ventas_hoy)
        
        # Tarjetas de estadísticas
        self.crear_tarjeta_estadistica(stats_frame, "Total Llantas", total_llantas, "🛞", LlanteraStyles.PRIMARY)
        self.crear_tarjeta_estadistica(stats_frame, "Stock Total", total_stock, "📦", LlanteraStyles.SECONDARY)
        self.crear_tarjeta_estadistica(stats_frame, "Total Ventas", total_ventas, "🛒", LlanteraStyles.SUCCESS)
        self.crear_tarjeta_estadistica(stats_frame, "Total Clientes", total_clientes, "👥", LlanteraStyles.ACCENT)
        
        # Segunda fila de estadísticas
        stats_frame2 = tk.Frame(main_container, bg=LlanteraStyles.BG_CARD)
        stats_frame2.pack(fill='x', pady=10)
        
        self.crear_tarjeta_estadistica(stats_frame2, f"Ingresos Totales\n${total_ingresos:,.2f}", "", "💰", LlanteraStyles.SUCCESS)
        self.crear_tarjeta_estadistica(stats_frame2, f"Ventas Hoy\n{len(ventas_hoy)}", "", "📅", LlanteraStyles.WARNING)
        self.crear_tarjeta_estadistica(stats_frame2, f"Ingresos Hoy\n${ingresos_hoy:,.2f}", "", "💵", LlanteraStyles.ACCENT)
        
        # Productos más vendidos
        productos_vendidos = {}
        for venta in ventas:
            for item in venta.get('items', []):
                key = f"{item['marca']} {item['modelo']}"
                if key in productos_vendidos:
                    productos_vendidos[key] += item['cantidad']
                else:
                    productos_vendidos[key] = item['cantidad']
        
        if productos_vendidos:
            top_frame = tk.Frame(main_container, bg=LlanteraStyles.BG_CARD)
            top_frame.pack(fill='both', expand=True, pady=20)
            
            tk.Label(top_frame, text="🏆 PRODUCTOS MÁS VENDIDOS", 
                    font=("Arial", 14, "bold"), 
                    fg=LlanteraStyles.PRIMARY, bg=LlanteraStyles.BG_CARD).pack(pady=10)
            
            # Tabla de productos más vendidos
            columns_top = ('Producto', 'Cantidad Vendida')
            tree_top = ttk.Treeview(top_frame, columns=columns_top, show='headings', height=8)
            
            for col in columns_top:
                tree_top.heading(col, text=col)
                if col == 'Cantidad Vendida':
                    tree_top.column(col, width=150)
                else:
                    tree_top.column(col, width=300)
            
            # Ordenar y mostrar top 10
            top_productos = sorted(productos_vendidos.items(), key=lambda x: x[1], reverse=True)[:10]
            for producto, cantidad in top_productos:
                tree_top.insert('', 'end', values=(producto, cantidad))
            
            tree_top.pack(fill='both', expand=True, padx=20)
        
        # Botones de reportes adicionales
        btn_frame = tk.Frame(main_container, bg=LlanteraStyles.BG_CARD)
        btn_frame.pack(fill='x', pady=20)
        
        tk.Button(btn_frame, text="📊 Reporte de Inventario", command=self.reporte_inventario,
                 font=("Arial", 12, "bold"), fg=LlanteraStyles.TEXT_WHITE,
                 bg=LlanteraStyles.PRIMARY, padx=20, pady=10, 
                 relief='flat', cursor='hand2').pack(side='left', padx=10)
        
        tk.Button(btn_frame, text="💰 Reporte de Ventas", command=self.reporte_ventas,
                 font=("Arial", 12, "bold"), fg=LlanteraStyles.TEXT_WHITE,
                 bg=LlanteraStyles.SUCCESS, padx=20, pady=10, 
                 relief='flat', cursor='hand2').pack(side='left', padx=10)
    
    def reporte_inventario(self):
        """Ventana de reporte detallado de inventario"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Reporte de Inventario")
        dialog.geometry("800x600")
        dialog.configure(bg=LlanteraStyles.BG_CARD)
        
        tk.Label(dialog, text="📦 REPORTE DETALLADO DE INVENTARIO", 
                font=("Arial", 16, "bold"), 
                fg=LlanteraStyles.PRIMARY, bg=LlanteraStyles.BG_CARD).pack(pady=20)
        
        # Tabla detallada
        columns = ('Marca', 'Modelo', 'Medida', 'Categoría', 'Stock', 'Precio', 'Valor Total')
        tree = ttk.Treeview(dialog, columns=columns, show='headings')
        
        for col in columns:
            tree.heading(col, text=col)
            if col in ['Stock', 'Precio', 'Valor Total']:
                tree.column(col, width=100)
            else:
                tree.column(col, width=120)
        
        valor_total_inventario = 0
        for llanta in self.data_manager.data['llantas']:
            stock = llanta.get('stock', 0)
            precio = llanta.get('precio', 0)
            valor_total = stock * precio
            valor_total_inventario += valor_total
            
            tree.insert('', 'end', values=(
                llanta.get('marca', ''),
                llanta.get('modelo', ''),
                llanta.get('medida', ''),
                llanta.get('categoria', ''),
                stock,
                f"${precio:,.2f}",
                f"${valor_total:,.2f}"
            ))
        
        tree.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Total del inventario
        total_label = tk.Label(dialog, text=f"VALOR TOTAL DEL INVENTARIO: ${valor_total_inventario:,.2f}", 
                              font=("Arial", 14, "bold"), 
                              fg=LlanteraStyles.SUCCESS, bg=LlanteraStyles.BG_CARD)
        total_label.pack(pady=20)
    
    def reporte_ventas(self):
        """Ventana de reporte detallado de ventas"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Reporte de Ventas")
        dialog.geometry("900x600")
        dialog.configure(bg=LlanteraStyles.BG_CARD)
        
        tk.Label(dialog, text="💰 REPORTE DETALLADO DE VENTAS", 
                font=("Arial", 16, "bold"), 
                fg=LlanteraStyles.PRIMARY, bg=LlanteraStyles.BG_CARD).pack(pady=20)
        
        # Tabla de ventas
        columns = ('ID', 'Fecha', 'Cliente', 'Items', 'Total', 'Vendedor')
        tree = ttk.Treeview(dialog, columns=columns, show='headings')
        
        for col in columns:
            tree.heading(col, text=col)
            if col == 'ID':
                tree.column(col, width=50)
            elif col == 'Items':
                tree.column(col, width=60)
            elif col == 'Total':
                tree.column(col, width=100)
            elif col == 'Fecha':
                tree.column(col, width=130)
            else:
                tree.column(col, width=150)
        
        for venta in reversed(self.data_manager.data['ventas']):  # Más recientes primero
            fecha = venta.get('fecha', '')
            if len(fecha) > 16:
                fecha = fecha[:16]  # Truncar fecha para que quepa
            
            tree.insert('', 'end', values=(
                venta.get('id', ''),
                fecha,
                venta.get('cliente', ''),
                len(venta.get('items', [])),
                f"${venta.get('total', 0):,.2f}",
                venta.get('vendedor', '')
            ))
        
        tree.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Total de ventas
        total_ventas = sum(v.get('total', 0) for v in self.data_manager.data['ventas'])
        total_label = tk.Label(dialog, text=f"TOTAL DE INGRESOS: ${total_ventas:,.2f}", 
                              font=("Arial", 14, "bold"), 
                              fg=LlanteraStyles.SUCCESS, bg=LlanteraStyles.BG_CARD)
        total_label.pack(pady=20)
    
    def mostrar_citas(self):
        """Muestra la gestión de citas"""
        self.limpiar_contenido()
        
        # Título
        title_frame = tk.Frame(self.content_frame, bg=LlanteraStyles.BG_CARD)
        title_frame.pack(fill='x', padx=20, pady=20)
        
        tk.Label(title_frame, text="📅 GESTIÓN DE CITAS", 
                font=("Arial", 18, "bold"), 
                fg=LlanteraStyles.PRIMARY, bg=LlanteraStyles.BG_CARD).pack(side='left')
        
        # Botón nueva cita
        if self.usuario_actual['rol'] in ["Administrador", "Vendedor", "Mecánico"]:
            tk.Button(title_frame, text="➕ Nueva Cita", command=self.nueva_cita,
                     font=("Arial", 10, "bold"), fg=LlanteraStyles.TEXT_WHITE,
                     bg=LlanteraStyles.SUCCESS, padx=20, pady=5, 
                     relief='flat', cursor='hand2').pack(side='right')
        
        # Filtros
        filter_frame = tk.Frame(self.content_frame, bg=LlanteraStyles.BG_CARD)
        filter_frame.pack(fill='x', padx=20, pady=10)
        
        tk.Label(filter_frame, text="Filtrar por fecha:", font=("Arial", 11, "bold"), 
                fg=LlanteraStyles.TEXT_PRIMARY, bg=LlanteraStyles.BG_CARD).pack(side='left', padx=10)
        
        self.fecha_filtro = tk.StringVar(value=datetime.now().strftime('%Y-%m-%d'))
        entry_fecha = tk.Entry(filter_frame, textvariable=self.fecha_filtro, font=("Arial", 11), width=12)
        entry_fecha.pack(side='left', padx=5)
        
        tk.Button(filter_frame, text="🔍 Filtrar", command=self.filtrar_citas,
                 font=("Arial", 10), fg=LlanteraStyles.TEXT_WHITE,
                 bg=LlanteraStyles.SECONDARY, padx=15, pady=3, 
                 relief='flat', cursor='hand2').pack(side='left', padx=5)
        
        tk.Button(filter_frame, text="📅 Hoy", command=lambda: self.filtrar_por_fecha('hoy'),
                 font=("Arial", 10), fg=LlanteraStyles.TEXT_WHITE,
                 bg=LlanteraStyles.ACCENT, padx=15, pady=3, 
                 relief='flat', cursor='hand2').pack(side='left', padx=5)
        
        # Tabla de citas
        table_frame = tk.Frame(self.content_frame, bg=LlanteraStyles.BG_CARD)
        table_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        columns = ('ID', 'Fecha', 'Hora', 'Cliente', 'Servicio', 'Estado', 'Notas')
        self.tree_citas = ttk.Treeview(table_frame, columns=columns, show='headings')
        
        for col in columns:
            self.tree_citas.heading(col, text=col)
            if col == 'ID':
                self.tree_citas.column(col, width=50)
            elif col in ['Fecha', 'Hora']:
                self.tree_citas.column(col, width=100)
            elif col == 'Estado':
                self.tree_citas.column(col, width=120)
            else:
                self.tree_citas.column(col, width=150)
        
        # Cargar citas
        self.cargar_citas()
        
        self.tree_citas.pack(fill='both', expand=True)
        
        # Scrollbar
        scrollbar_v = ttk.Scrollbar(table_frame, orient='vertical', command=self.tree_citas.yview)
        scrollbar_v.pack(side='right', fill='y')
        self.tree_citas.configure(yscrollcommand=scrollbar_v.set)
        
        # Menú contextual
        self.tree_citas.bind('<Button-3>', self.menu_contextual_citas)
    
    def cargar_citas(self, fecha_filtro=None):
        """Carga las citas en la tabla"""
        # Limpiar tabla
        for item in self.tree_citas.get_children():
            self.tree_citas.delete(item)
        
        # Filtrar citas
        citas = self.data_manager.data.get('citas', [])
        if fecha_filtro:
            citas = [c for c in citas if c.get('fecha', '').startswith(fecha_filtro)]
        
        # Cargar datos
        for cita in sorted(citas, key=lambda x: (x.get('fecha', ''), x.get('hora', ''))):
            estado = cita.get('estado', 'Pendiente')
            tags = ()
            if estado == 'Completada':
                tags = ('completada',)
            elif estado == 'Cancelada':
                tags = ('cancelada',)
            
            self.tree_citas.insert('', 'end', values=(
                cita.get('id', ''),
                cita.get('fecha', ''),
                cita.get('hora', ''),
                cita.get('cliente', ''),
                cita.get('servicio', ''),
                estado,
                cita.get('notas', '')[:30] + '...' if len(cita.get('notas', '')) > 30 else cita.get('notas', '')
            ), tags=tags)
        
        # Configurar tags
        self.tree_citas.tag_configure('completada', background='#e8f5e8')
        self.tree_citas.tag_configure('cancelada', background='#ffebee')
    
    def filtrar_citas(self):
        """Filtrar citas por fecha"""
        fecha = self.fecha_filtro.get()
        try:
            # Validar formato de fecha
            datetime.strptime(fecha, '%Y-%m-%d')
            self.cargar_citas(fecha)
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha inválido. Use YYYY-MM-DD")
    
    def filtrar_por_fecha(self, tipo):
        """Filtrar por fecha específica"""
        if tipo == 'hoy':
            fecha = datetime.now().strftime('%Y-%m-%d')
            self.fecha_filtro.set(fecha)
            self.cargar_citas(fecha)
    
    def nueva_cita(self):
        """Diálogo para crear nueva cita"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Nueva Cita")
        dialog.geometry("450x600")
        dialog.configure(bg=LlanteraStyles.BG_CARD)
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Centrar diálogo
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (450 // 2)
        y = (dialog.winfo_screenheight() // 2) - (600 // 2)
        dialog.geometry(f"450x600+{x}+{y}")
        
        tk.Label(dialog, text="NUEVA CITA", font=("Arial", 16, "bold"), 
                fg=LlanteraStyles.PRIMARY, bg=LlanteraStyles.BG_CARD).pack(pady=20)
        
        # Campos
        fields = {}
        
        # Cliente
        frame_cliente = tk.Frame(dialog, bg=LlanteraStyles.BG_CARD)
        frame_cliente.pack(fill='x', padx=40, pady=10)
        
        tk.Label(frame_cliente, text="Cliente:", font=("Arial", 11, "bold"), 
                fg=LlanteraStyles.TEXT_PRIMARY, bg=LlanteraStyles.BG_CARD).pack(anchor='w')
        
        fields['cliente'] = tk.Entry(frame_cliente, font=("Arial", 11), width=35)
        fields['cliente'].pack(fill='x', pady=(5, 0))
        
        # Teléfono
        frame_telefono = tk.Frame(dialog, bg=LlanteraStyles.BG_CARD)
        frame_telefono.pack(fill='x', padx=40, pady=10)
        
        tk.Label(frame_telefono, text="Teléfono:", font=("Arial", 11, "bold"), 
                fg=LlanteraStyles.TEXT_PRIMARY, bg=LlanteraStyles.BG_CARD).pack(anchor='w')
        
        fields['telefono'] = tk.Entry(frame_telefono, font=("Arial", 11), width=35)
        fields['telefono'].pack(fill='x', pady=(5, 0))
        
        # Fecha
        frame_fecha = tk.Frame(dialog, bg=LlanteraStyles.BG_CARD)
        frame_fecha.pack(fill='x', padx=40, pady=10)
        
        tk.Label(frame_fecha, text="Fecha (YYYY-MM-DD):", font=("Arial", 11, "bold"), 
                fg=LlanteraStyles.TEXT_PRIMARY, bg=LlanteraStyles.BG_CARD).pack(anchor='w')
        
        fields['fecha'] = tk.Entry(frame_fecha, font=("Arial", 11), width=35)
        fields['fecha'].pack(fill='x', pady=(5, 0))
        fields['fecha'].insert(0, datetime.now().strftime('%Y-%m-%d'))
        
        # Hora
        frame_hora = tk.Frame(dialog, bg=LlanteraStyles.BG_CARD)
        frame_hora.pack(fill='x', padx=40, pady=10)
        
        tk.Label(frame_hora, text="Hora (HH:MM):", font=("Arial", 11, "bold"), 
                fg=LlanteraStyles.TEXT_PRIMARY, bg=LlanteraStyles.BG_CARD).pack(anchor='w')
        
        fields['hora'] = tk.Entry(frame_hora, font=("Arial", 11), width=35)
        fields['hora'].pack(fill='x', pady=(5, 0))
        
        # Servicio
        frame_servicio = tk.Frame(dialog, bg=LlanteraStyles.BG_CARD)
        frame_servicio.pack(fill='x', padx=40, pady=10)
        
        tk.Label(frame_servicio, text="Servicio:", font=("Arial", 11, "bold"), 
                fg=LlanteraStyles.TEXT_PRIMARY, bg=LlanteraStyles.BG_CARD).pack(anchor='w')
        
        servicios_nombres = [s['nombre'] for s in self.data_manager.data['servicios']]
        fields['servicio'] = ttk.Combobox(frame_servicio, values=servicios_nombres, 
                                        font=("Arial", 11), width=32, state="readonly")
        fields['servicio'].pack(fill='x', pady=(5, 0))
        
        # Notas
        frame_notas = tk.Frame(dialog, bg=LlanteraStyles.BG_CARD)
        frame_notas.pack(fill='x', padx=40, pady=10)
        
        tk.Label(frame_notas, text="Notas:", font=("Arial", 11, "bold"), 
                fg=LlanteraStyles.TEXT_PRIMARY, bg=LlanteraStyles.BG_CARD).pack(anchor='w')
        
        fields['notas'] = tk.Text(frame_notas, font=("Arial", 11), width=35, height=4)
        fields['notas'].pack(fill='x', pady=(5, 0))
        
        def guardar_cita():
            try:
                cliente = fields['cliente'].get().strip()
                telefono = fields['telefono'].get().strip()
                fecha = fields['fecha'].get().strip()
                hora = fields['hora'].get().strip()
                servicio = fields['servicio'].get().strip()
                notas = fields['notas'].get(1.0, tk.END).strip()
                
                if not all([cliente, fecha, hora, servicio]):
                    raise ValueError("Todos los campos obligatorios deben completarse")
                
                # Validar formato de fecha
                datetime.strptime(fecha, '%Y-%m-%d')
                
                # Validar formato de hora
                datetime.strptime(hora, '%H:%M')
                
                # Generar ID
                citas = self.data_manager.data.get('citas', [])
                nuevo_id = max([c.get('id', 0) for c in citas], default=0) + 1
                
                # Crear nueva cita
                nueva_cita = {
                    'id': nuevo_id,
                    'cliente': cliente,
                    'telefono': telefono,
                    'fecha': fecha,
                    'hora': hora,
                    'servicio': servicio,
                    'notas': notas,
                    'estado': 'Pendiente',
                    'creada_por': self.usuario_actual['username'],
                    'fecha_creacion': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
                
                citas.append(nueva_cita)
                self.data_manager.data['citas'] = citas
                self.data_manager.guardar_datos()
                self.cargar_citas()
                
                dialog.destroy()
                messagebox.showinfo("Éxito", "Cita creada correctamente")
                
            except ValueError as e:
                messagebox.showerror("Error", str(e))
        
        # Botones
        btn_frame = tk.Frame(dialog, bg=LlanteraStyles.BG_CARD)
        btn_frame.pack(pady=30)
        
        tk.Button(btn_frame, text="Guardar", command=guardar_cita,
                 font=("Arial", 12, "bold"), fg=LlanteraStyles.TEXT_WHITE,
                 bg=LlanteraStyles.SUCCESS, padx=30, pady=10, 
                 relief='flat', cursor='hand2').pack(side='left', padx=10)
        
        tk.Button(btn_frame, text="Cancelar", command=dialog.destroy,
                 font=("Arial", 12, "bold"), fg=LlanteraStyles.TEXT_WHITE,
                 bg=LlanteraStyles.DANGER, padx=30, pady=10, 
                 relief='flat', cursor='hand2').pack(side='left', padx=10)
    
    def menu_contextual_citas(self, event):
        """Menú contextual para citas"""
        selected = self.tree_citas.selection()
        if not selected:
            return
        
        menu = tk.Menu(self.root, tearoff=0)
        menu.add_command(label="✅ Marcar Completada", command=lambda: self.cambiar_estado_cita('Completada'))
        menu.add_command(label="⏳ Marcar Pendiente", command=lambda: self.cambiar_estado_cita('Pendiente'))
        menu.add_command(label="❌ Cancelar Cita", command=lambda: self.cambiar_estado_cita('Cancelada'))
        menu.add_separator()
        menu.add_command(label="🗑️ Eliminar", command=self.eliminar_cita)
        
        try:
            menu.tk_popup(event.x_root, event.y_root)
        finally:
            menu.grab_release()
    
    def cambiar_estado_cita(self, nuevo_estado):
        """Cambiar estado de la cita seleccionada"""
        selected = self.tree_citas.selection()
        if not selected:
            return
        
        item = self.tree_citas.item(selected[0])
        cita_id = int(item['values'][0])
        
        # Encontrar la cita
        cita = next((c for c in self.data_manager.data.get('citas', []) if c['id'] == cita_id), None)
        if cita:
            cita['estado'] = nuevo_estado
            self.data_manager.guardar_datos()
            self.cargar_citas()
            messagebox.showinfo("Éxito", f"Cita marcada como {nuevo_estado}")
    
    def eliminar_cita(self):
        """Eliminar cita seleccionada"""
        selected = self.tree_citas.selection()
        if not selected:
            return
        
        item = self.tree_citas.item(selected[0])
        cita_id = int(item['values'][0])
        
        if messagebox.askyesno("Confirmar", "¿Está seguro de eliminar esta cita?"):
            citas = self.data_manager.data.get('citas', [])
            self.data_manager.data['citas'] = [c for c in citas if c['id'] != cita_id]
            self.data_manager.guardar_datos()
            self.cargar_citas()
            messagebox.showinfo("Éxito", "Cita eliminada correctamente")
    
    def cerrar_sesion(self):
        """Cerrar sesión y volver al login"""
        if messagebox.askyesno("Cerrar Sesión", "¿Está seguro de cerrar sesión?"):
            self.root.destroy()
            self.usuario_actual = None
            self.iniciar_aplicacion()

# Función principal para ejecutar la aplicación
def main():
    """Función principal para ejecutar el sistema de llantera"""
    try:
        sistema = SistemaLlantera()
        sistema.iniciar_aplicacion()
    except Exception as e:
        print(f"Error al iniciar la aplicación: {e}")
        messagebox.showerror("Error", f"Error al iniciar la aplicación: {e}")

if __name__ == "__main__":
    main()