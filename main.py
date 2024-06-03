import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pyswip

# Função para chamar o Prolog e obter a melhor rota
def encontrar_rota(origem, destino):
    prolog = pyswip.Prolog()
    prolog.consult('rotas.pl') # Carrega o arquivo Prolog com as definições de rotas
    consulta = f"melhor_rota({origem}, {destino}, Rota, Distancia)"
    
    try:
        resultado = list(prolog.query(consulta))
        if resultado:
            rota = resultado[0]['Rota']
            distancia = resultado[0]['Distancia']
            return rota, distancia
        else:
            return None, None
    except Exception as e:
        messagebox.showerror("Erro", str(e))
        return None, None

# Função de callback do botão
def on_click():
    origem = origem_var.get()
    destino = destino_var.get()
    
    if not origem or not destino:
        messagebox.showwarning("Aviso", "Por favor, selecione tanto a cidade de origem quanto a de destino.")
        return
    
    rota, distancia = encontrar_rota(origem, destino)
    
    if rota:
      rota_invertida = rota[::-1]
      resultado_var.set(f"Rota: {' -> '.join(map(str, rota_invertida))}\nDistância: {distancia} km")
    else:
      resultado_var.set("Nenhuma rota encontrada entre as cidades especificadas.")


# Criação da interface gráfica com Tkinter
root = tk.Tk()
root.title("Planejador de Rotas")

# Ajuste do tamanho da janela principal
root.geometry("600x400")
root.resizable(False, False) # Serve para não deixar o tamanho da janela ser alterado

# Carregar imagem de fundo
background_image = tk.PhotoImage(file="background_image.png")

# Adicionar imagem de fundo
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Lista de cidades
cidades = ["goiania", "anapolis", "rio_verde", "brasilia", "luziania", "trindade", "jatai", "planaltina", "goianesia"]

# Obter a altura da janela
window_height = root.winfo_height()

# Calcular o deslocamento vertical para centralizar os widgets
vertical_offset = (window_height - 180) // 2  # Ajuste conforme necessário

# Tamanho da fonte
font_size = 11

# Labels e Comboboxes centralizados
tk.Label(root, text="Cidade de Origem:", bg="white", font=("Courier New", font_size)).place(relx=0.25, rely=0.3 - vertical_offset/400)
origem_var = tk.StringVar(root)
origem_combobox = ttk.Combobox(root, textvariable=origem_var, values=cidades, font=("Courier New", font_size))
origem_combobox.place(relx=0.55, rely=0.3 - vertical_offset/400)

tk.Label(root, text="Cidade de Destino:", bg="white", font=("Courier New", font_size)).place(relx=0.25, rely=0.4 - vertical_offset/400)
destino_var = tk.StringVar(root)
destino_combobox = ttk.Combobox(root, textvariable=destino_var, values=cidades, font=("Courier New", font_size))
destino_combobox.place(relx=0.55, rely=0.4 - vertical_offset/400)

# Botão "Encontrar rota" centralizado
tk.Button(root, text="Encontrar Rota", command=on_click, font=("Courier New", font_size)).place(relx=0.35, rely=0.5 - vertical_offset/400, relwidth=0.3)

# Label "Planejador de Rotas" centralizada no topo
tk.Label(root, text="Planejador de Rotas", bg="#e74c3c", fg="black", font=("Courier New", 14)).place(relx=0.5, rely=0.05, anchor="center")

resultado_var = tk.StringVar()
tk.Label(root, textvariable=resultado_var, bg="white").place(relx=0.025, rely=0.6 - vertical_offset/400, relwidth=0.95)

root.mainloop()
