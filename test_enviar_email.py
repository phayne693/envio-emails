from coreClientes.dadosClientes import clientes_download
from envioEmail.clientes_ativos import clientes_ativos_json
from envioEmail.enviar_email import enviar_email
import os
from dotenv import load_dotenv
load_dotenv()

login_core = os.getenv("LOGIN_CORE")
senha_core =  os.getenv("SENHA_CORE")

roboResponse = ([
    clientes_download(login_core, senha_core),
    clientes_ativos_json(),
    enviar_email()
])
print(roboResponse)