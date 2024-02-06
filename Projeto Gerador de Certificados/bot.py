import os
import pandas as pd
from fpdf import FPDF
from Subtasks import envia_email

# Projeto: Gerador de certificados de particição.
# Doc: https://py-pdf.github.io/fpdf2/Tutorial-pt.html

# Planilha de entrada com a lista dos paricipantes
df_dados = pd.read_excel("Entrada/participantes.xlsx")

# Gera o certificado
for index, row in df_dados.iterrows():

    # Cria um pdf com layout Paisagem    
    pdf = FPDF('L')
    pdf.add_page()
    
    # Adiciona imagem modelo
    pdf.image("Entrada/modelo-1.jpg", x=0, y=0)
    pdf.set_font("Arial", "I", 35)

    # Adiciona nome de forma centralizada
    pdf.cell(280, 150, row['Nome'], align='C')

    # Salva o arquivo
    caminho_certificado = f"{os.getcwd()}/Saida/Certificado_{row['Nome']}.pdf"
    pdf.output(caminho_certificado)

    # Envia e-mail de coclusão para o certificado em anexo.
    envia_email.email_conclusao(destino=row['Email'], anexo=caminho_certificado)

    del pdf