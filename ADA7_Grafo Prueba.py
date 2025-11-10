import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import networkx as nx
import os

class GrafoInteractivo:
    def __init__(self, root):
        self.root = root
        self.root.title("Grafo Interactivo con Costos y Fondo")
        self.G = nx.DiGraph()
        self.pos = {}
        self.selected_node = None
        self.dragging = False
        self.imagen_cargada = False

        # --- PANEL IZQUIERDO ---
        control_frame = tk.Frame(root, bg="#e6f0ff")
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        tk.Label(control_frame, text="Vértice / Estado:", bg="#e6f0ff").pack()
        self.entry_vertice = tk.Entry(control_frame)
        self.entry_vertice.pack()

        tk.Label(control_frame, text="Destino:", bg="#e6f0ff").pack()
        self.entry_destino = tk.Entry(control_frame)
        self.entry_destino.pack()

        tk.Label(control_frame, text="Costo / Objeto:", bg="#e6f0ff").pack()
        self.entry_objeto = tk.Entry(control_frame)
        self.entry_objeto.pack()

        # --- BOTONES DE EDICIÓN ---
        tk.Button(control_frame, text="➕ Insertar vértice", command=self.insertaVertice).pack(fill=tk.X, pady=2)
        tk.Button(control_frame, text="🔗 Insertar arista", command=self.insertarArista).pack(fill=tk.X, pady=2)
        tk.Button(control_frame, text="➡️ Arista dirigida", command=self.insertarAristaDirigida).pack(fill=tk.X, pady=2)
        tk.Button(control_frame, text="❌ Eliminar vértice", command=self.eliminaVertice).pack(fill=tk.X, pady=2)
        tk.Button(control_frame, text="🚫 Eliminar arista", command=self.eliminaArista).pack(fill=tk.X, pady=2)
        tk.Button(control_frame, text="🖼️ Cargar imagen", command=self.cargar_imagen).pack(fill=tk.X, pady=10)
        tk.Button(control_frame, text="🔄 Refrescar dibujo", command=self.actualizar_dibujo).pack(fill=tk.X, pady=2)

        # --- BOTONES DE RECORRIDO ---
        tk.Label(control_frame, text="Recorridos:", bg="#e6f0ff", font=("Arial", 10, "bold")).pack(pady=(10, 2))
        tk.Button(control_frame, text="🚗 Recorrido sin repetir", command=self.calcular_recorrido_unico).pack(fill=tk.X, pady=2)
        tk.Button(control_frame, text="🔁 Recorrido con repetición", command=self.calcular_recorrido_con_repeticion).pack(fill=tk.X, pady=2)

        # --- RESULTADO DE RECORRIDOS ---
        tk.Label(control_frame, text="Resultado:", bg="#e6f0ff", font=("Arial", 10, "bold")).pack(pady=(10, 2))
        self.resultado_text = tk.Text(control_frame, height=10, width=30)
        self.resultado_text.pack(pady=5)

        # --- ÁREA DE GRAFO ---
        self.fig, self.ax = plt.subplots(figsize=(6, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.canvas.mpl_connect('button_press_event', self.on_click)
        self.canvas.mpl_connect('motion_notify_event', self.on_drag)
        self.canvas.mpl_connect('button_release_event', self.on_release)

    # --- FUNCIONES BÁSICAS ---
    def insertaVertice(self):
        v = self.entry_vertice.get().strip()
        if not v:
            messagebox.showerror("Error", "Debe ingresar un nombre de vértice.")
            return
        self.G.add_node(v)
        self.pos[v] = (len(self.pos), len(self.pos))
        self.actualizar_dibujo()

    def insertarArista(self):
        v, w, o = self.entry_vertice.get().strip(), self.entry_destino.get().strip(), self.entry_objeto.get().strip()
        if v not in self.G or w not in self.G:
            messagebox.showerror("Error", "Ambos vértices deben existir.")
            return
        try:
            costo = float(o)
        except ValueError:
            costo = o  # Si no es numérico, guarda el texto
        self.G.add_edge(v, w, peso=costo)
        self.G.add_edge(w, v, peso=costo)
        self.actualizar_dibujo()

    def insertarAristaDirigida(self):
        v, w, o = self.entry_vertice.get().strip(), self.entry_destino.get().strip(), self.entry_objeto.get().strip()
        if v not in self.G or w not in self.G:
            messagebox.showerror("Error", "Ambos vértices deben existir.")
            return
        try:
            costo = float(o)
        except ValueError:
            costo = o
        self.G.add_edge(v, w, peso=costo)
        self.actualizar_dibujo()

    def eliminaVertice(self):
        v = self.entry_vertice.get().strip()
        if v not in self.G:
            messagebox.showerror("Error", "El vértice no existe.")
            return
        self.G.remove_node(v)
        self.pos.pop(v, None)
        self.actualizar_dibujo()

    def eliminaArista(self):
        v, w = self.entry_vertice.get().strip(), self.entry_destino.get().strip()
        if not self.G.has_edge(v, w):
            messagebox.showerror("Error", "La arista no existe.")
            return
        self.G.remove_edge(v, w)
        self.actualizar_dibujo()

    # --- IMAGEN DE FONDO ---
    def cargar_imagen(self):
        archivo = filedialog.askopenfilename(
            title="Seleccionar imagen de fondo",
            filetypes=[("Imágenes", "*.png;*.jpg;*.jpeg")]
        )

        if not archivo:
            messagebox.showwarning("Sin selección", "No se seleccionó ninguna imagen.")
            return

        try:
            self.bg_image = plt.imread(archivo)
            self.imagen_cargada = True
            self.actualizar_dibujo()
            messagebox.showinfo("Imagen cargada", f"Imagen '{os.path.basename(archivo)}' cargada correctamente.")
        except Exception as e:
            messagebox.showerror("Error al cargar imagen", f"No se pudo abrir la imagen:\n{e}")

    # --- ACTUALIZAR GRAFO ---
    def actualizar_dibujo(self):
        self.ax.clear()
        if self.imagen_cargada:
            self.ax.imshow(self.bg_image, extent=[-1, 8, -1, 8], aspect='auto')

        nx.draw(self.G, pos=self.pos, with_labels=True, node_color='lightblue',
                node_size=1500, font_size=9, ax=self.ax, arrows=True)
        labels = nx.get_edge_attributes(self.G, 'peso')
        nx.draw_networkx_edge_labels(self.G, pos=self.pos, edge_labels=labels, ax=self.ax)
        self.ax.set_xlim(-1, 8)
        self.ax.set_ylim(-1, 8)
        self.ax.axis("off")
        self.canvas.draw()

    # --- EVENTOS DE ARRASTRE ---
    def on_click(self, event):
        if event.inaxes != self.ax:
            return
        for node, (x, y) in self.pos.items():
            if (event.xdata - x) ** 2 + (event.ydata - y) ** 2 < 0.05:
                self.selected_node = node
                self.dragging = True
                break

    def on_drag(self, event):
        if self.dragging and self.selected_node and event.inaxes == self.ax:
            self.pos[self.selected_node] = (event.xdata, event.ydata)
            self.actualizar_dibujo()

    def on_release(self, event):
        self.dragging = False
        self.selected_node = None

    # --- FUNCIONES DE RECORRIDO ---
    def calcular_recorrido_unico(self):
        """Recorre todos los estados sin repetir ninguno"""
        if len(self.G.nodes) < 2:
            messagebox.showerror("Error", "Debes tener al menos dos vértices.")
            return
        try:
            recorrido = list(nx.dfs_preorder_nodes(self.G))
            costo_total = 0
            for i in range(len(recorrido) - 1):
                peso = self.G[recorrido[i]][recorrido[i + 1]].get('peso', 0)
                if isinstance(peso, (int, float)):
                    costo_total += peso
            self.mostrar_resultado(recorrido, costo_total, "sin repetir")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def calcular_recorrido_con_repeticion(self):
        """Recorre los estados repitiendo algunos"""
        if len(self.G.nodes) < 2:
            messagebox.showerror("Error", "Debes tener al menos dos vértices.")
            return
        recorrido = list(nx.dfs_edges(self.G))
        costo_total = 0
        for (v, w) in recorrido:
            peso = self.G[v][w].get('peso', 0)
            if isinstance(peso, (int, float)):
                costo_total += peso
        nodos = [recorrido[0][0]] + [w for (_, w) in recorrido]
        self.mostrar_resultado(nodos, costo_total, "con repetición")

    def mostrar_resultado(self, recorrido, costo, tipo):
        self.resultado_text.delete("1.0", tk.END)
        self.resultado_text.insert(tk.END, f"Recorrido ({tipo}):\n")
        self.resultado_text.insert(tk.END, " → ".join(recorrido) + "\n\n")
        self.resultado_text.insert(tk.END, f"Costo total: {costo}\n")

# --- EJECUCIÓN PRINCIPAL ---
if __name__ == "__main__":
    root = tk.Tk()
    app = GrafoInteractivo(root)
    root.mainloop()
