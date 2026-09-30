import tkinter as tk

# 1. Criar a janela principal
janela = tk.Tk()
janela.title("Exemplo de Radiobutton")
janela.geometry("300x200")

# 2. Criar a variável que vai armazenar a opção selecionada
# Usamos StringVar porque as opções são textos (strings)
opcao_selecionada = tk.StringVar(value="Opção 1")

# Função para mostrar o que foi selecionado
def mostrar_selecao():
    print(f"Você selecionou: {opcao_selecionada.get()}")

# 3. Criar os Radiobuttons
# Importante: todos devem usar a mesma 'variable', mas ter 'value' diferentes
rb1 = tk.Radiobutton(janela, text="Opção 1", variable=opcao_selecionada, value="Opção 1", command=mostrar_selecao)
rb2 = tk.Radiobutton(janela, text="Opção 2", variable=opcao_selecionada, value="Opção 2", command=mostrar_selecao)
rb3 = tk.Radiobutton(janela, text="Opção 3", variable=opcao_selecionada, value="Opção 3", command=mostrar_selecao)

# 4. Posicionar os botões na janela
rb1.pack(anchor="w", padx=20, pady=5)
rb2.pack(anchor="w", padx=20, pady=5)
rb3.pack(anchor="w", padx=20, pady=5)

# Iniciar o aplicativo
janela.mainloop()
