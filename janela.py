import customtkinter
from fpdf import FPDF


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("600x300")

def on_entry_click(event, entry):
    if entry.get() == entry.placeholder:
        entry.delete(0, "end")  # Remove o texto padrão
        entry.insert(0, "")  # Garante que o texto não seja mantido ao digitar

def clique():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial")

    # Obter os valores dos campos de entrada
    projeto_texto = projeto.get()
    horas_estimadas_texto = horas_estimadas.get()
    valor_hora_texto = valor_hora.get()
    prazo_estimado_texto = prazo_estimado.get()

    # Calcular o valor total estimado
    valor_total_estimado = int(horas_estimadas_texto) * int(valor_hora_texto)

    pdf.image("template2.png", x=0, y=0)

    pdf.text(115, 145, projeto_texto)
    pdf.text(115, 160, horas_estimadas_texto)
    pdf.text(115, 175, valor_hora_texto)
    pdf.text(115, 190, prazo_estimado_texto)
    pdf.text(115, 205, str(valor_total_estimado))

    pdf.output("orcamento.pdf")
    print("Orçamento gerado com sucesso!")

    

texto = customtkinter.CTkLabel(janela, text="Gerador de Orçamento")
texto.pack(padx=10, pady=10)

# Adicionando a capacidade de usar placeholders nos campos de entrada
projeto = customtkinter.CTkEntry(janela)
projeto.placeholder = "Nome do Projeto"
projeto.insert(0, projeto.placeholder)
projeto.bind("<FocusIn>", lambda event: on_entry_click(event, projeto))
projeto.pack(padx=10, pady=10)

horas_estimadas = customtkinter.CTkEntry(janela)
horas_estimadas.placeholder = "Horas Estimadas"
horas_estimadas.insert(0, horas_estimadas.placeholder)
horas_estimadas.bind("<FocusIn>", lambda event: on_entry_click(event, horas_estimadas))
horas_estimadas.pack(padx=10, pady=10)

valor_hora = customtkinter.CTkEntry(janela)
valor_hora.placeholder = "Valor por Hora"
valor_hora.insert(0, valor_hora.placeholder)
valor_hora.bind("<FocusIn>", lambda event: on_entry_click(event, valor_hora))
valor_hora.pack(padx=10, pady=10)

prazo_estimado = customtkinter.CTkEntry(janela)
prazo_estimado.placeholder = "Prazo Estimado"
prazo_estimado.insert(0, prazo_estimado.placeholder)
prazo_estimado.bind("<FocusIn>", lambda event: on_entry_click(event, prazo_estimado))
prazo_estimado.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text="Gerar Orçamento", command=clique)
botao.pack(padx=10, pady=10)

janela.mainloop()
