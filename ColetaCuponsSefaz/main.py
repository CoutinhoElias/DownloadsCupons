from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from datetime import datetime, timedelta

# Função para obter o primeiro e o último dia do mês anterior
def obter_primeiro_e_ultimo_dia_mes_anterior(data_atual):
    primeiro_dia_mes_atual = data_atual.replace(day=1)
    ultimo_dia_mes_anterior = primeiro_dia_mes_atual - timedelta(days=1)
    primeiro_dia_mes_anterior = ultimo_dia_mes_anterior.replace(day=1)
    return primeiro_dia_mes_anterior, ultimo_dia_mes_anterior

# Configurar o webdriver (usando ChromeDriver no mesmo diretório do código)
current_directory = os.path.dirname(os.path.abspath(__file__))
driver_path = os.path.join(current_directory, 'chromedriver.exe')  # Substitua por 'chromedriver.exe' no Windows

service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Navegar até a URL da SEFAZ
url = "https://servicos.sefaz.ce.gov.br/internet/acessoseguro/servicosenha/logarusuario/login.asp"
driver.get(url)

# Esperar que os elementos estejam disponíveis e realizar as ações
try:
    # Digitar CPF
    cpf_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'txtUsuario'))
    )
    cpf_input.send_keys('***********')

    # Digitar Senha
    senha_input = driver.find_element(By.NAME, 'txtSenha')
    senha_input.send_keys('******')

    # Selecionar Socio (assumindo que é um campo de seleção)
    socio_select = driver.find_element(By.NAME, 'cboTipoUsuario')
    socio_select.send_keys('SOCIO')  # Ajuste conforme necessário

    # Clicar em ENTRAR
    mfe_button = driver.find_element(By.ID, 'btEntrar')
    mfe_button.click()

    print('Entrei no login da Sefaz...')

    # Clicar no link "MFE - Modulo Fiscal Eletronico"
    mfe_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'MFE - Modulo Fiscal Eletronico'))
    )
    mfe_link.click()

    print('Cliquei na opção MFE...')

    # Clicar no link "Acessar MFe"
    acessar_mfe_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Acessar MFe'))
    )
    acessar_mfe_link.click()

    # Esperar o formulário de seleção de empresa carregar
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'form1'))
    )

    print('agora escolhe a empresa pelo CGF')

    # Escolher empresa pelo CGF
    cgf_to_select = '71389725'
    
    # Esperar a tabela carregar e procurar pelo CGF
    rows = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//form[@id="form1"]//tr'))
    )

    # Verificar cada linha na tabela
    for row in rows:
        cgf_elements = row.find_elements(By.XPATH, './/td[1]/a')
        for cgf_element in cgf_elements:
            if cgf_element.text.strip() == cgf_to_select:
                cgf_element.click()
                break
        else:
            continue
        break
    else:
        print(f'CGF {cgf_to_select} não encontrado na tabela.')

    # Alternar para a nova guia
    new_tab = driver.window_handles[-1]
    driver.switch_to.window(new_tab)

    print('Aopos abrir nova guia tem que clicar em Consultar CF-e...')
#------------------------------------------------------------------------------

    # Clicar no link "Acessar MFe"
    acessar_mfe_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Consultar CF-e'))
    )
    acessar_mfe_link.click()

    # Esperar o formulário de seleção de empresa carregar
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'form1'))
    )
#------------------------------------------------------------------------------

    # Preencher períodos e mudar paginação para 100
    periodo_inicio = driver.find_element(By.XPATH, '//*[@id="form-start-date-search-coupons"]')
    periodo_inicio.send_keys('01/06/2024')

    periodo_fim = driver.find_element(By.XPATH, '//*[@id="form-end-date-search-coupons"]')
    periodo_fim.send_keys('01/06/2024')

    # Continuar com as próximas ações...
    print('fim...')

finally:
    # Fechar o navegador
    # driver.quit()
    pass