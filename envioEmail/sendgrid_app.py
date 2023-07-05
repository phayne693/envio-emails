import configparser
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

# # config = configparser.ConfigParser()
# # config.read('config.ini')


# # try:
# #     settings = config['SETTINGS']
# # except:
# #     settings = {}

# # API = settings.get('APIKEY',None)
# # from_email = settings.get('FROM', None)
# # to_email = settings.get('TO','')

# # subject = 'Teste'
# # html_content = '''<table border="0" cellpadding="0" cellspacing="0" class="module" data-role="module-button" data-type="button" role="module" style="table-layout:fixed;" width="100%" data-muid="fc9ef803-9840-4ee1-a9d3-1f65d3f73223">
# #             <tbody>
# #                 <tr>
# #                     <td align="center" bgcolor="#0D3012" class="outer-td"><img class="max-width" border="0" style="display:block;text-decoration:none; font-family:Helvetica, arial, sans-serif; font-size:16px; height:120px;margin-top:35px" width="300" alt="" data-proportionally-constrained="true" data-responsive="false" src="http://cdn.mcauto-images-production.sendgrid.net/318491f3e44f0d19/c45ef979-5136-4854-abd9-1c1f03f02661/308x136.png" height="100">
# #                     </td>
# #                 </tr>   
# #             </tbody>
# #         </table>
# #         <table border="0" cellpadding="0" cellspacing="0" class="module" data-role="module-button" data-type="button" role="module" style="table-layout:fixed;" width="100%" data-muid="fc9ef803-9840-4ee1-a9d3-1f65d3f73223">
# #             <tbody>
# #                 <tr>
# #                     <td style="height:50px">
                    
# #                     </td>
# #                 </tr>
# #                 <tr>
# #                     <td align="left" bgcolor="white" class="outer-td" style="font-size:16px;letter-spacing:0px; line-height:normal;font-family:helvetica,sans-serif;">Segue o documento de CLIENTES ATIVOS em anexo.
                    
# #                     </td>
# #                 </tr>     
# #                 <tr>
# #                     <td style="height:25px">
                    
# #                     </td>
# #                 </tr>
            
# #             </tbody>
# #         </table>
# #         <table border="0" cellpadding="0" cellspacing="0" class="module" data-role="module-button" data-type="button" role="module" style="table-layout:fixed;" width="100%" data-muid="fc9ef803-9840-4ee1-a9d3-1f65d3f73223">
# #             <tbody>
# #                 <tr>
# #                     <td align="left" bgcolor="white" class="outer-td" style="font-size:16px;letter-spacing:0px; line-height:normal;font-family:helvetica,sans-serif;">
                    
# #                     </td>
# #                 </tr>
# #                 <tr>
# #                     <td style="height:100px">
                    
# #                     </td>
# #                 </tr>
# #                 <tr>
# #                     <td align="left" bgcolor="white" class="outer-td" style="font-size:16px;letter-spacing:0px; line-height:normal;font-family:helvetica,sans-serif;"><strong>Abraços da equipe Norway Digital.</strong>
# #                     </td>
# #                 </tr>
# #                 <tr>
# #                     <td style="height:25px">
                    
# #                     </td>
# #                 </tr> 
# #                 <tr>
# #                     <td style="height:25px">
                    
# #                     </td>
# #                 </tr>
            
# #             </tbody>
# #         </table>
# #         <table width="100%" style="margin: auto; text-align: center;background:#0D3012">
# #                 <tr>
# #                     <td style="height:25px">
                    
# #                     </td>
# #                 </tr>
# #                 <tr>
# #                     <td align="center" bgcolor="#0D3012" class="outer-td">
# #                         <a href="https://www.instagram.com/creditofederalnb/"><img src="http://cdn.mcauto-images-production.sendgrid.net/318491f3e44f0d19/3684b554-caa5-4946-8308-327fd098442e/262x268.png" style="width:2.5em;padding:1%"></a>
# #                         <a href="https://br.linkedin.com/company/norwaybank"><img src="http://cdn.mcauto-images-production.sendgrid.net/318491f3e44f0d19/8934fefc-b991-44d7-8c88-98590c56369c/262x268.png" style="width:2.5em;padding:1%"></a>
# #                         <a href="https://pt-br.facebook.com/norwaybank.br/"><img src="http://cdn.mcauto-images-production.sendgrid.net/318491f3e44f0d19/8920f5d0-e286-4bf6-ac96-bd0c217e371f/262x268.png" style="width:2.5em;padding:1%"></a>
# #                         <a href="https://www.youtube.com/channel/UCs4DqqlDN_6urpzBc-2fjgQ/featured"><img src="http://cdn.mcauto-images-production.sendgrid.net/318491f3e44f0d19/9bb8ac59-36c8-40fd-8888-deeaf01eeb1f/262x268.png" style="width:2.5em;padding:1%"></a>
# #                     </td>
# #                 </tr>
# #                 <tr>
# #                     <td align="center" bgcolor="#0D3012" class="outer-td">
# #                         <img src="http://cdn.mcauto-images-production.sendgrid.net/318491f3e44f0d19/ce311a34-a354-4cbe-a2e8-81b143b2f111/487x1.png" style="width:50%">
# #                 </td></tr>
# #                 <tr>
# #                     <td align="center">
# #                     <table data-muid="fc9ef803-9840-4ee1-a9d3-1f65d3f73223" style="background:#0D3012">
# #                         <tr style="background:#0D3012">
# #                         <td style="color:white;font-size:12px">Central de Atendimento:</td>
# #                         </tr>
# #                         <tr>
# #                         <td style="color:white;font-size:12px">Segunda a Sexta das 09h às 18h</td>
# #                         </tr>
# #                         <tr>
# #                         <td style="color:white;font-size:12px"><a style="color:#FBA500;" href="tel:080008877888">0800 887 7888</a> (Em todo o território nacional)</td>
# #                         </tr>
# #                         <tr>
# #                         <td style="color:white;font-size:12px"><a style="color:#FBA500;" href="tel:1120502222">11 2050 2222</a> (Capitais e regiões metropolitanas)</td>
# #                         </tr>
# #                     </table>
# #                     </td>
# #                 </tr>
# #                 <tr>
# #                     <td style="height:25px">
                    
# #                     </td>
# #                 </tr>
# #         </table>
# #         '''


# # def enviar_email_sendgrid(API, from_email, to_email):
# #     if API!= None and from_email!= None and len(to_email)>0:
# #         message = Mail(from_email,to_email,subject,html_content)
# #         try:
# #             sg = SendGridAPIClient(API)
# #             response = sg.send(message)
# #             print(response.status_code)
# #             print(response.body)
# #             print(response.headers)
# #         except Exception as e:
# #             print(e.message)


# # message = Mail(
# #     from_email='jefersonqueiroz2009@hotmail.com',
# #     to_emails='teste@norwaybank.com.br',
# #     subject='Sending with Twilio SendGrid is Fun',
# #     html_content='<strong>and easy to do anywhere, even with Python</strong>')
# # try:
# #     sg = SendGridAPIClient('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')
# #     response = sg.send(message)
# #     print(response.status_code)
# #     print(response.body)
# #     print(response.headers)
# # except Exception as e:
# #     print(e.message)

# import sendgrid
# import os
# from sendgrid.helpers.mail import Mail, Email, To, Content

# sg = sendgrid.SendGridAPIClient(api_key='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')
# from_email = Email("jefersonqueiroz2009@hotmail.com")  # Change to your verified sender
# to_email = To("teste@norwaybank.com.br")  # Change to your recipient
# subject = "Sending with SendGrid is Fun"
# content = Content("text/plain", "and easy to do anywhere, even with Python")
# mail = Mail(from_email, to_email, subject, content)

# # Get a JSON-ready representation of the Mail object
# mail_json = mail.get()

# # Send an HTTP POST request to /mail/send
# response = sg.client.mail.send.post(request_body=mail_json)
# print(response.status_code)
# print(response.headers)

Key = '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'

message = Mail(
    from_email='jefersonqueiroz2009@hotmail.com',
    to_emails='teste@norwaybank.com.br',
    subject='teste',
    plain_text_content='testando api sendgrid',
    html_content='Teste'
)
sg = SendGridAPIClient(api_key='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')
response = sg.send(message)
print('funcionou')
