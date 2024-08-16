import tkinter as tk
from tkinter import ttk

class CargaWindow(tk.Toplevel):
    def __init__(self, parent, num_carga):
        super().__init__(parent)
        self.parent = parent
        self.num_carga = num_carga
        self.title(f"Carga {self.num_carga + 1}")

        self.configure(bg='lightgray')  # Configuração de cor de fundo para exemplo

        self.frame = ttk.Frame(self, padding=(20, 10))
        self.frame.pack(padx=20, pady=20)

        self.escolha = tk.IntVar()

        # Exemplo de personalização de fonte
        fonte_label = ('Helvetica', 12, 'bold')

        ttk.Label(self.frame, text=f"Informações da Carga {self.num_carga + 1}", font=fonte_label).pack()

        ttk.Radiobutton(self.frame, text="Paletizada", variable=self.escolha, value=1, command=self.mostrar_opcoes).pack()
        ttk.Radiobutton(self.frame, text="Não paletizada", variable=self.escolha, value=2, command=self.mostrar_opcoes).pack()

        self.sub_opcao = tk.IntVar()
        self.entry_comprimento = ttk.Entry(self.frame, font=fonte_label)
        self.entry_largura = ttk.Entry(self.frame, font=fonte_label)
        self.entry_altura = ttk.Entry(self.frame, font=fonte_label)
        self.entry_paletes = ttk.Entry(self.frame, font=fonte_label)
        self.entry_diametro = ttk.Entry(self.frame, font=fonte_label)
        self.entry_rolos = ttk.Entry(self.frame, font=fonte_label)

        self.btn_calcular = ttk.Button(self.frame, text="Calcular", command=self.calcular)
        self.btn_calcular.pack(pady=10)

        self.label_resultado = ttk.Label(self.frame, text="", font=fonte_label)
        self.label_resultado.pack()

    def mostrar_opcoes(self):
        if self.escolha.get() == 1:  # Paletizada
            self.limpar_widgets()
            ttk.Label(self.frame, text="Comprimento (m):", font=('Arial', 10)).pack()
            self.entry_comprimento.pack()

            ttk.Label(self.frame, text="Largura (m):", font=('Arial', 10)).pack()
            self.entry_largura.pack()

            ttk.Label(self.frame, text="Altura (m):", font=('Arial', 10)).pack()
            self.entry_altura.pack()

            ttk.Label(self.frame, text="Número de paletes:", font=('Arial', 10)).pack()
            self.entry_paletes.pack()

            self.btn_calcular.pack(pady=10)

        elif self.escolha.get() == 2:  # Não paletizada
            self.limpar_widgets()
            ttk.Label(self.frame, text="Selecione o tipo:", font=('Arial', 10)).pack()
            ttk.Radiobutton(self.frame, text="Caixas", variable=self.sub_opcao, value=1, command=self.mostrar_caixas).pack()
            ttk.Radiobutton(self.frame, text="Rolos", variable=self.sub_opcao, value=2, command=self.mostrar_rolos).pack()

    def mostrar_caixas(self):
        self.limpar_widgets()
        ttk.Label(self.frame, text="Comprimento (m):", font=('Arial', 10)).pack()
        self.entry_comprimento.pack()

        ttk.Label(self.frame, text="Largura (m):", font=('Arial', 10)).pack()
        self.entry_largura.pack()

        ttk.Label(self.frame, text="Altura (m):", font=('Arial', 10)).pack()
        self.entry_altura.pack()

        ttk.Label(self.frame, text="Número de caixas:", font=('Arial', 10)).pack()
        self.entry_paletes.pack()

        self.btn_calcular.pack(pady=10)

    def mostrar_rolos(self):
        self.limpar_widgets()
        ttk.Label(self.frame, text="Diâmetro do rolo (m):", font=('Arial', 10)).pack()
        self.entry_diametro.pack()

        ttk.Label(self.frame, text="Altura (m):", font=('Arial', 10)).pack()
        self.entry_altura.pack()

        ttk.Label(self.frame, text="Número de rolos:", font=('Arial', 10)).pack()
        self.entry_rolos.pack()

        self.btn_calcular.pack(pady=10)

    def limpar_widgets(self):
        for widget in self.frame.winfo_children():
            widget.pack_forget()

    def calcular(self):
        try:
            if self.escolha.get() == 1:  # Paletizada
                c = float(self.entry_comprimento.get())
                l = float(self.entry_largura.get())
                h = float(self.entry_altura.get())
                n = int(self.entry_paletes.get())

                vol = c * l * h * n
                self.parent.cbm += vol
                self.label_resultado.config(text=f"Volume: {vol:.2f} m3", font=('Arial', 12, 'italic'))

            elif self.escolha.get() == 2:  # Não paletizada
                if self.sub_opcao.get() == 1:  # Caixas
                    c = float(self.entry_comprimento.get())
                    l = float(self.entry_largura.get())
                    h = float(self.entry_altura.get())
                    n = int(self.entry_paletes.get())

                    vol = c * l * h * n
                    self.parent.cbm += vol
                    self.label_resultado.config(text=f"Volume: {vol:.2f} m3", font=('Arial', 12, 'italic'))

                elif self.sub_opcao.get() == 2:  # Rolos
                    d = float(self.entry_diametro.get())
                    h = float(self.entry_altura.get())
                    n = int(self.entry_rolos.get())

                    vol = 3.1415 * ((d / 2) ** 2) * h * n
                    self.parent.cbm += vol
                    self.label_resultado.config(text=f"Volume: {vol:.2f} m3", font=('Arial', 12, 'italic'))

            # Após calcular, destruir esta janela para abrir a próxima carga ou finalizar
            self.destroy()
            self.parent.proxima_carga()
        except Exception as e:
            self.parent.mostrar_erro(f"Erro ao calcular a carga: {e}")
            self.destroy()
            self.parent.reiniciar()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Cargas")
        self.cbm = 0
        self.num_cargas = 0
        self.num_carga_atual = 0

        self.configure(bg='white')  # Configuração de cor de fundo para exemplo

        self.frame = None
        self.entry_num_cargas = None
        self.entry_fator_cbm = None
        self.label_resultado = None
        self.label_resultado_fator = None

        self.criar_widgets()

    def criar_widgets(self):
        self.frame = ttk.Frame(self, padding=(20, 20))
        self.frame.pack(padx=20, pady=20)

        ttk.Label(self.frame, text="Número de Cargas:", font=('Arial', 12)).pack()
        self.entry_num_cargas = ttk.Entry(self.frame, font=('Arial', 12))
        self.entry_num_cargas.pack()

        ttk.Button(self.frame, text="Iniciar Cálculo", command=self.iniciar_calculo).pack(pady=10)

        self.label_resultado = ttk.Label(self.frame, text="", font=('Arial', 12, 'bold'))
        self.label_resultado.pack()

        ttk.Label(self.frame, text="Fator de CBM:", font=('Arial', 12)).pack()
        self.entry_fator_cbm = ttk.Entry(self.frame, font=('Arial', 12))
        self.entry_fator_cbm.pack()

        ttk.Label(self.frame, text="Resultado:", font=('Arial', 12)).pack()
        self.label_resultado_fator = ttk.Label(self.frame, text="", font=('Arial', 12, 'bold'))
        self.label_resultado_fator.pack()

        ttk.Button(self.frame, text="Reiniciar", command=self.reiniciar).pack(pady=10)

    def iniciar_calculo(self):
        try:
            self.num_cargas = int(self.entry_num_cargas.get())
            self.abrir_proxima_carga()
        except ValueError:
            self.mostrar_erro("Por favor, insira um número válido de cargas.")
            self.reiniciar()

    def abrir_proxima_carga(self):
        if self.num_carga_atual < self.num_cargas:
            carga = CargaWindow(self, self.num_carga_atual)
            self.num_carga_atual += 1
        else:
            self.atualizar_resultado()

    def proxima_carga(self):
        self.abrir_proxima_carga()

    def atualizar_resultado(self):
        self.label_resultado.config(text=f"Volume Total: {self.cbm:.2f} m3", font=('Arial', 14, 'underline'))
        try:
            fator = float(self.entry_fator_cbm.get())
            resultado_fator = self.cbm * fator
            self.label_resultado_fator.config(text=f"{resultado_fator:.2f}", font=('Arial', 12, 'bold'))
        except ValueError:
            self.mostrar_erro("Por favor, insira um fator de CBM válido.")
            self.reiniciar()

    def reiniciar(self):
        self.cbm = 0
        self.num_cargas = 0
        self.num_carga_atual = 0
        self.label_resultado.config(text="")
        self.label_resultado_fator.config(text="")
        self.entry_fator_cbm.delete(0, tk.END)
        if self.frame:
            self.frame.destroy()
        self.criar_widgets()

    def mostrar_erro(self, mensagem):
        erro = tk.Toplevel(self)
        erro.title("Erro")
        ttk.Label(erro, text=mensagem, foreground="red", padding=(20, 10)).pack(padx=20, pady=20)
        ttk.Button(erro, text="Fechar", command=erro.destroy).pack(pady=10)

app = App()
app.mainloop()
