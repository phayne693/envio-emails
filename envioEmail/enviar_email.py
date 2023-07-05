import smtplib
import os
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#imports para arquivos
from email.mime.base import MIMEBase
from email import encoders
#import para ler xlsx
import xlrd
#lista de emails
def enviar_email():
    email_para = []
    #abrir excel
    lista_emails = xlrd.open_workbook('C:/Users/Jeferson/Desktop/aws-puppeteer/envioEmail/teste.xlsx')#'/home/jeferson/aws-puppeteer/envioEmail/teste.xlsx'
    #ler como lista
    sheet = lista_emails.sheet_by_index(0)
    #percorrer todas as linhas da coluna 0
    for linha in range(0,1):
        email_para.append(sheet.cell_value(linha, 0))
    print(f"Emails encontrados :{email_para}")
    for email in email_para:
        #iniciar o servidor SMTP
        host = 'mail.norwaybank.com.br'
        port = '587'
        login = 'suporte@norwaybank.com.br'
        senha = 'Norway@2023'
        # host = 'smtp.sendgrid.net'
        # port = '587'
        # login = 'MKxovf5PR0uOznwuDGyyRg'
        # senha = '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'
        #entra no servidor
        server  = smtplib.SMTP(host,port)
        #iniciar o TLS
        server.ehlo()
        server.starttls()
        #login na conta
        server.login(login, senha)
        print('Logado')
        #construir email
        corpo = '''<table border="0" cellpadding="0" cellspacing="0" class="module" data-role="module-button" data-type="button" role="module" style="table-layout:fixed;" width="100%" data-muid="fc9ef803-9840-4ee1-a9d3-1f65d3f73223">
            <tbody>
                <tr>
                    <td align="center" bgcolor="#0D3012" class="outer-td"><img class="max-width" border="0" style="display:block;text-decoration:none; font-family:Helvetica, arial, sans-serif; font-size:16px; height:120px;margin-top:35px" width="300" alt="" data-proportionally-constrained="true" data-responsive="false" src="http://cdn.mcauto-images-production.sendgrid.net/318491f3e44f0d19/c45ef979-5136-4854-abd9-1c1f03f02661/308x136.png" height="100">
                    </td>
                </tr>   
            </tbody>
        </table>
        <table border="0" cellpadding="0" cellspacing="0" class="module" data-role="module-button" data-type="button" role="module" style="table-layout:fixed;" width="100%" data-muid="fc9ef803-9840-4ee1-a9d3-1f65d3f73223">
            <tbody>
                <tr>
                    <td style="height:50px">
                    
                    </td>
                </tr>
                <tr>
                    <td align="left" bgcolor="white" class="outer-td" style="font-size:16px;letter-spacing:0px; line-height:normal;font-family:helvetica,sans-serif;">Segue o documento de CLIENTES ATIVOS em anexo.
                    
                    </td>
                </tr>     
                <tr>
                    <td style="height:25px">
                    
                    </td>
                </tr>
            
            </tbody>
        </table>
        <table border="0" cellpadding="0" cellspacing="0" class="module" data-role="module-button" data-type="button" role="module" style="table-layout:fixed;" width="100%" data-muid="fc9ef803-9840-4ee1-a9d3-1f65d3f73223">
            <tbody>
                <tr>
                    <td align="left" bgcolor="white" class="outer-td" style="font-size:16px;letter-spacing:0px; line-height:normal;font-family:helvetica,sans-serif;">
                    
                    </td>
                </tr>
                <tr>
                    <td style="height:100px">
                    
                    </td>
                </tr>
                <tr>
                    <td align="left" bgcolor="white" class="outer-td" style="font-size:16px;letter-spacing:0px; line-height:normal;font-family:helvetica,sans-serif;"><strong>Abraços da equipe Norway Digital.</strong>
                    </td>
                </tr>
                <tr>
                    <td style="height:25px">
                    
                    </td>
                </tr> 
                <tr>
                    <td style="height:25px">
                    
                    </td>
                </tr>
            
            </tbody>
        </table>
        <table width="100%" style="margin: auto; text-align: center;background:#0D3012">
                <tr>
                    <td style="height:25px">
                    
                    </td>
                </tr>
                <tr>
                    <td align="center" bgcolor="#0D3012" class="outer-td">
                        <a href="https://www.instagram.com/creditofederalnb/"><img src="http://cdn.mcauto-images-production.sendgrid.net/318491f3e44f0d19/3684b554-caa5-4946-8308-327fd098442e/262x268.png" style="width:2.5em;padding:1%"></a>
                        <a href="https://br.linkedin.com/company/norwaybank"><img src="http://cdn.mcauto-images-production.sendgrid.net/318491f3e44f0d19/8934fefc-b991-44d7-8c88-98590c56369c/262x268.png" style="width:2.5em;padding:1%"></a>
                        <a href="https://pt-br.facebook.com/norwaybank.br/"><img src="http://cdn.mcauto-images-production.sendgrid.net/318491f3e44f0d19/8920f5d0-e286-4bf6-ac96-bd0c217e371f/262x268.png" style="width:2.5em;padding:1%"></a>
                        <a href="https://www.youtube.com/channel/UCs4DqqlDN_6urpzBc-2fjgQ/featured"><img src="http://cdn.mcauto-images-production.sendgrid.net/318491f3e44f0d19/9bb8ac59-36c8-40fd-8888-deeaf01eeb1f/262x268.png" style="width:2.5em;padding:1%"></a>
                    </td>
                </tr>
                <tr>
                    <td align="center" bgcolor="#0D3012" class="outer-td">
                        <img src="http://cdn.mcauto-images-production.sendgrid.net/318491f3e44f0d19/ce311a34-a354-4cbe-a2e8-81b143b2f111/487x1.png" style="width:50%">
                </td></tr>
                <tr>
                    <td align="center">
                    <table data-muid="fc9ef803-9840-4ee1-a9d3-1f65d3f73223" style="background:#0D3012">
                        <tr style="background:#0D3012">
                        <td style="color:white;font-size:12px">Central de Atendimento:</td>
                        </tr>
                        <tr>
                        <td style="color:white;font-size:12px">Segunda a Sexta das 09h às 18h</td>
                        </tr>
                        <tr>
                        <td style="color:white;font-size:12px"><a style="color:#FBA500;" href="tel:080008877888">0800 887 7888</a> (Em todo o território nacional)</td>
                        </tr>
                        <tr>
                        <td style="color:white;font-size:12px"><a style="color:#FBA500;" href="tel:1120502222">11 2050 2222</a> (Capitais e regiões metropolitanas)</td>
                        </tr>
                    </table>
                    </td>
                </tr>
                <tr>
                    <td style="height:25px">
                    
                    </td>
                </tr>
        </table>
        '''
        # for para enviar todos os emails
        email_msg = MIMEMultipart()
        email_msg['From'] = login
        email_msg['To'] = email
        email_msg['Subject'] = "Teste de email"
        email_msg.attach(MIMEText(corpo,'html'))
        #arquivos
        caminho_arquivos = 'C:/Users/Jeferson/Desktop/aws-puppeteer/envioEmail/clientes_ativos.csv'#'/home/jeferson/aws-puppeteer/clientes_ativos.csv'
        #abrir como leitura binaria
        attchment = open(caminho_arquivos, '+rb')
        #codificar em base64
        att = MIMEBase('application', 'octet-stream')
        att.set_payload(attchment.read())
        encoders.encode_base64(att)
        #cabecalho com anexo de item no email
        att.add_header('Content-Disposition', f'attachment; filename=clientes_ativos.csv')
        #fecha o arquivo
        attchment.close()
        #coloca o anexo no corpo do email
        email_msg.attach(att)
        #armazena os erros 
        emails_nao_enviados = []
        try:
            #enviar email
            server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())
            #printa o email enviado
            retorno = ('Email enviado para: %s' % email)
            return retorno
        except (smtplib.SMTPException, smtplib.SMTPServerDisconnected, smtplib.SMTPResponseException, smtplib.SMTPSenderRefused, smtplib.SMTPRecipientsRefused, smtplib.SMTPDataError, smtplib.SMTPConnectError, smtplib.SMTPHeloError, smtplib.SMTPNotSupportedError, smtplib.SMTPAuthenticationError) as e:
            #grava emaisl nao enviados em variavel
            emails_nao_enviados.append(e)
            retorno = ('Email não enviado para: %s\nErro: %s' % (email, e))
            return retorno
        finally:
            #fechar o servidor
            server.quit()
    #grava em arquivo
    with open('emails.json', 'w') as file:
        json.dump(emails_nao_enviados, file, indent=4)