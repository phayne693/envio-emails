from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# definindo opcoes para o navegador
options = Options()
options.add_argument('--disabel-blink-features=AutomationControlled')
options.add_experimental_option("UseAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
# iniciando o servico
page = Service(ChromeDriverManager().install())
# localizacao fake
location = '{"latitude": -23.5102, "logitude": -46.6590}'
# defininso as ocnfiguracoes do navegador
options.add_argument(f"--geolocation={location}")
options.add_argument("--disable-extensions")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-browser-side-navigation")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_experimental_option("prefs", {
    "donwload.default.directory": 'C:/Users/Jeferson/Desktop/aws-puppeteer/coreClientes/'#"/home/jeferson/aws-puppeteer/coreClientes"
})
prefs = {"download.default_directory": "C:/Users/Jeferson/Desktop/aws-puppeteer/coreClientes/"}
opt = webdriver.ChromeOptions()
opt.add_experimental_option("prefs", prefs)


def clientes_download(login_core,senha_core):
    print('Iniciado core...')
    navegador = webdriver.Chrome(service=page, options=opt)
    navegador.get('https://app.norwaydigital.com.br/auth/signin')
    time.sleep(5)

    # inserir login
    print('Inserindo login..')
    login = navegador.find_element(By.XPATH, '//*[@id="text"]')
    login.send_keys(login_core)
    # senha
    procurarSenha = navegador.find_element(By.XPATH, '//*[@id="teste"]')
    numerosBtn = procurarSenha.find_elements(By.TAG_NAME, 'button')
    listaBtn = [button.get_attribute('textContent').replace(
        'ou', '') for button in numerosBtn]
    print('Inserindo senha...')
    while len(senha_core) != 0:
        for n in senha_core:
            for i, botao in enumerate(listaBtn):
                if str(senha_core[0]) in botao:
                    numerosBtn[i].click()
                    senha_core.remove(senha_core[0])
                    time.sleep(1)
                    break
    # click entrar
    time.sleep(1)
    acessar = navegador.find_element(
        By.XPATH, '//*[@id="single-spa-application:@infinity/auth"]/body/section/section[1]/form/button')
    acessar.click()
    print('Entrando...')
    time.sleep(5)
    # expandir menu
    hamburguer = navegador.find_element(
        By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/div[1]')
    hamburguer.click()
    # #click clientes
    print('Acessando clientes...')
    clientes = WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="MenuWrapperId"]/a[14]'))
    )
    clientes.click()
    time.sleep(5)
    try:
        #download todos os clientes
        print('Fazendo Download...')
        clickDown = WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div/div/div/section/div[2]/div/div[1]/button'))
        )
        ActionChains(navegador).move_to_element(clickDown).click().perform()
        time.sleep(3)
        retorno = 'Download concluido!'
        return retorno
    except:
        print('Falha no Download!')

