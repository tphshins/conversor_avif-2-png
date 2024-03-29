import tkinter as tk
from tkinter import filedialog
from PIL import Image

def converter_avif_para_png():
    # Abrir caixa de diálogo para selecionar o arquivo .avif
    arquivo_avif = filedialog.askopenfilename(filetypes=[("Arquivos AVIF", "*.avif")])
    
    if arquivo_avif:
        # Carregar a imagem usando o PIL
        imagem = Image.open(arquivo_avif)
        
        # Abrir caixa de diálogo para selecionar onde salvar a imagem .png
        arquivo_png = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Arquivos PNG", "*.png")])
        
        if arquivo_png:
            # Salvar a imagem no formato .png
            imagem.save(arquivo_png)
            print("Conversão concluída com sucesso!")
        else:
            print("Nenhum local de saída selecionado.")
    else:
        print("Nenhum arquivo .avif selecionado.")

# Criar a janela principal
janela = tk.Tk()
janela.title("Conversor AVIF para PNG")

# Botão para iniciar a conversão
btn_converter = tk.Button(janela, text="Converter AVIF para PNG", command=converter_avif_para_png)
btn_converter.pack(padx=20, pady=10)

# Rodar a interface gráfica
janela.mainloop()
