import win32com.client as win32

def email_conclusao(destino, anexo):

    # Criar a integração com o outlook
    outlook = win32.Dispatch('outlook.application')

    # Criar um email
    email = outlook.CreateItem(0)

    # Configurar as informações do seu e-mail
    email.To = destino
    email.Subject = "E-mail automático do Python"

    email.HTMLBody = f"""
    <p>Prezado(as)</p>

    <p>Segue relatório em anexo</p>


    <p>Atenciosamente</p>
    <p>Bot</p>
    """

    email.Attachments.Add(anexo)
    email.Send()

    print("Email enviado com sucesso para: ", destino)
