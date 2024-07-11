import smtplib
from email.message import EmailMessage

from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options

from selenium.webdriver.common.by import By

import schedule
from time import sleep
import random

def app_previsao_tempo():

    ENDERECO_EMAIL = 'rafaelsoaresat@gmail.com'
    SENHA_EMAIL = 'mxqgwlvnkpavavkn'

    edge_options = Options()

    arguments = ['--lang=pt-BR', '--window-size=800,800']

    for argument in arguments:
        edge_options.add_argument(argument)

    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    def digitar_naturalmente(cidade, campo_pesquisa):
        for letra in cidade:
            campo_pesquisa.send_keys(letra)
            sleep(random.randint(1,5)/30)

    driver.get('https://www.tempo.com/')
    sleep(10)

    campo_pesquisa = driver.find_element(By.ID, 'search_pc')
    digitar_naturalmente('Uberlândia', campo_pesquisa)
    sleep(5)
    campo_dropdown_cidade = driver.find_element(By.XPATH, "//ul[@class='resultado-busqueda']/li")
    driver.execute_script('arguments[0].click()', campo_dropdown_cidade)
    sleep(10)

    dia_1_titulo = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d1 activo']/span[@class='col day_col']/span[@class='text-0']").text
    dia_1_sub_titulo = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d1 activo']/span[@class='col day_col']/span[@class='subtitle-m']").text
    dia_1_condicao_tempo = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d1 activo']/span[@class='col day_col']/span[@class='prediccion col']/span/img[@class='simbW']").get_attribute('alt')
    dia_1_temperatura_minima = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d1 activo']/span[@class='col day_col']/span[@class='temp']/span[@class='min changeUnitT']").text
    dia_1_temperatura_maxima = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d1 activo']/span[@class='col day_col']/span[@class='temp']/span[@class='max changeUnitT']").text

    dia_2_titulo = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d2']/span[@class='col day_col']/span[@class='text-0']").text
    dia_2_sub_titulo = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d2']/span[@class='col day_col']/span[@class='subtitle-m']").text
    dia_2_condicao_tempo = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d2']/span[@class='col day_col']/span[@class='prediccion col']/span/img[@class='simbW']").get_attribute('alt')
    dia_2_temperatura_minima = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d2']/span[@class='col day_col']/span[@class='temp']/span[@class='min changeUnitT']").text
    dia_2_temperatura_maxima = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d2']/span[@class='col day_col']/span[@class='temp']/span[@class='max changeUnitT']").text

    dia_3_titulo = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d3']/span[@class='col day_col']/span[@class='text-0']").text
    dia_3_sub_titulo = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d3']/span[@class='col day_col']/span[@class='subtitle-m']").text
    dia_3_condicao_tempo = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d3']/span[@class='col day_col']/span[@class='prediccion col']/span/img[@class='simbW']").get_attribute('alt')
    dia_3_temperatura_minima = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d3']/span[@class='col day_col']/span[@class='temp']/span[@class='min changeUnitT']").text
    dia_3_temperatura_maxima = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d3']/span[@class='col day_col']/span[@class='temp']/span[@class='max changeUnitT']").text

    dia_4_titulo = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d4']/span[@class='col day_col']/span[@class='text-0']").text
    dia_4_sub_titulo = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d4']/span[@class='col day_col']/span[@class='subtitle-m']").text
    dia_4_condicao_tempo = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d4']/span[@class='col day_col']/span[@class='prediccion col']/span/img[@class='simbW']").get_attribute('alt')
    dia_4_temperatura_minima = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d4']/span[@class='col day_col']/span[@class='temp']/span[@class='min changeUnitT']").text
    dia_4_temperatura_maxima = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d4']/span[@class='col day_col']/span[@class='temp']/span[@class='max changeUnitT']").text

    mail = EmailMessage()
    mail['Subject'] = 'Previsão do tempo para hoje e para os próximos 3 dias'
    mensagem = f'''
    <p>Segue a previsão do tempo para Uberlândia - MG</p>
    <p>Dia da Semana: {dia_1_titulo}</p>
    <p>Dia: {dia_1_sub_titulo}</p>
    <p>Condição do tempo: {dia_1_condicao_tempo}</p>
    <p>Temperatura: Mínima {dia_1_temperatura_minima}Cº - Máxima {dia_1_temperatura_maxima}Cº</p>
    <p>----------------------------------------------------------------------</p>
    <p>Dia da Semana: {dia_2_titulo}</p>
    <p>Dia: {dia_2_sub_titulo}</p>
    <p>Condição do tempo: {dia_2_condicao_tempo}</p>
    <p>Temperatura: Mínima {dia_2_temperatura_minima}Cº - Máxima {dia_2_temperatura_maxima}Cº</p>
    <p>----------------------------------------------------------------------</p>
    <p>Dia da Semana: {dia_3_titulo}</p>
    <p>Dia: {dia_3_sub_titulo}</p>
    <p>Condição do tempo: {dia_3_condicao_tempo}</p>
    <p>Temperatura: Mínima {dia_3_temperatura_minima}Cº - Máxima {dia_3_temperatura_maxima}Cº</p>
    <p>----------------------------------------------------------------------</p>
    <p>Dia da Semana: {dia_4_titulo}</p>
    <p>Dia: {dia_4_sub_titulo}</p>
    <p>Condição do tempo: {dia_4_condicao_tempo}</p>
    <p>Temperatura: Mínima {dia_4_temperatura_minima}Cº - Máxima {dia_4_temperatura_maxima}Cº</p>
    '''

    mail['From'] = ENDERECO_EMAIL
    mail['To'] = ENDERECO_EMAIL
    mail.add_header('Content-Type', 'text/html')
    mail.set_payload(mensagem.encode('utf-8'))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as email:
        email.login(ENDERECO_EMAIL,SENHA_EMAIL)
        email.send_message(mail)
        email.quit()
        
    driver.close

schedule.every(3).minutes.do(app_previsao_tempo)
while True:
    schedule.run_pending()
    sleep(1)