from coreClientes.dadosClientes import clientes_download
from envioEmail.clientes_ativos import clientes_ativos_json
from envioEmail.enviar_email import enviar_email

login_core = 'thiago@teraidc.com.br'
senha_core =  [1, 1, 2, 0, 2, 2]

roboResponse = ([
    clientes_download(login_core, senha_core),
    clientes_ativos_json(),
    enviar_email()
])
print(roboResponse)