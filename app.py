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

email_usuario = ''
cidade_usuario = ''

while email_usuario == '':    
    email_usuario = input("Digite o e-mail para receber os e-mail's sobre previsão do tempo da sua cidade: ")

while cidade_usuario == '':
    cidade_usuario = input("Sobre qual cidade você quer saber a previsão do tempo? ")

print('****************************Script sendo executado, aguarde 10 segundos****************************')

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
    print('\n****************************Site aberto com sucesso, aguardando 10 seg para renderização dos elementos****************************\n')
    sleep(10)    

    campo_pesquisa = driver.find_element(By.ID, 'search_pc')
    digitar_naturalmente(cidade_usuario, campo_pesquisa)
    sleep(5)
    campo_dropdown_cidade = driver.find_element(By.XPATH, "//ul[@class='resultado-busqueda']/li")
    driver.execute_script('arguments[0].click()', campo_dropdown_cidade)

    print('\n****************************Pesquisa feita com sucesso, aguardando 10 seg para renderização dos elementos****************************\n')

    sleep(10)

    dia_1_titulo = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d1 activo']/span[@class='col day_col']/span[@class='text-0']").text
    dia_1_sub_titulo = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d1 activo']/span[@class='col day_col']/span[@class='subtitle-m']").text
    dia_1_condicao_tempo = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d1 activo']/span[@class='col day_col']/span[@class='prediccion col']/span/img[@class='simbW']").get_attribute('alt')
    dia_1_img_tempo = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d1 activo']/span[@class='col day_col']/span[@class='prediccion col']/span/img[@class='simbW']").get_attribute('src')
    dia_1_temperatura_minima = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d1 activo']/span[@class='col day_col']/span[@class='temp']/span[@class='min changeUnitT']").text
    dia_1_temperatura_maxima = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d1 activo']/span[@class='col day_col']/span[@class='temp']/span[@class='max changeUnitT']").text

    dia_2_titulo = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d2']/span[@class='col day_col']/span[@class='text-0']").text
    dia_2_sub_titulo = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d2']/span[@class='col day_col']/span[@class='subtitle-m']").text
    dia_2_condicao_tempo = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d2']/span[@class='col day_col']/span[@class='prediccion col']/span/img[@class='simbW']").get_attribute('alt')
    dia_2_img_tempo = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d2']/span[@class='col day_col']/span[@class='prediccion col']/span/img[@class='simbW']").get_attribute('src')
    dia_2_temperatura_minima = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d2']/span[@class='col day_col']/span[@class='temp']/span[@class='min changeUnitT']").text
    dia_2_temperatura_maxima = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d2']/span[@class='col day_col']/span[@class='temp']/span[@class='max changeUnitT']").text

    dia_3_titulo = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d3']/span[@class='col day_col']/span[@class='text-0']").text
    dia_3_sub_titulo = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d3']/span[@class='col day_col']/span[@class='subtitle-m']").text
    dia_3_condicao_tempo = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d3']/span[@class='col day_col']/span[@class='prediccion col']/span/img[@class='simbW']").get_attribute('alt')
    dia_3_img_tempo = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d3']/span[@class='col day_col']/span[@class='prediccion col']/span/img[@class='simbW']").get_attribute('src')
    dia_3_temperatura_minima = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d3']/span[@class='col day_col']/span[@class='temp']/span[@class='min changeUnitT']").text
    dia_3_temperatura_maxima = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d3']/span[@class='col day_col']/span[@class='temp']/span[@class='max changeUnitT']").text

    dia_4_titulo = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d4']/span[@class='col day_col']/span[@class='text-0']").text
    dia_4_sub_titulo = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d4']/span[@class='col day_col']/span[@class='subtitle-m']").text
    dia_4_condicao_tempo = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d4']/span[@class='col day_col']/span[@class='prediccion col']/span/img[@class='simbW']").get_attribute('alt')
    dia_4_img_tempo = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d4']/span[@class='col day_col']/span[@class='prediccion col']/span/img[@class='simbW']").get_attribute('src')
    dia_4_temperatura_minima = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d4']/span[@class='col day_col']/span[@class='temp']/span[@class='min changeUnitT']").text
    dia_4_temperatura_maxima = driver.find_element(By.XPATH, "//ul[@class='grid-container-7 dias_w']/li[@class='grid-item dia d4']/span[@class='col day_col']/span[@class='temp']/span[@class='max changeUnitT']").text

    mail = EmailMessage()
    mail['Subject'] = f'Previsão do tempo para hoje e para os próximos 3 dias para a cidade {cidade_usuario}'
    mensagem = f'''
    <!doctype html>
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <title>Template Previsão do Tempo</title>
        <style>
        </style>
    </head>
    <body style="margin: 0;padding: 0;box-sizing: border-box;">
        <div style="display: block;width: 100%;text-align: center;margin-top: 20px;margin-bottom: 20px;">
            <h2>Previsão do tempo para hoje.</h2>
        </div>
        <div style="display: flex;width: 100%;flex-wrap: wrap;justify-content: center;">        
            <div style="margin: 10px; width:230px;padding: 10px;text-align: center;background-color: cornsilk;border-radius: 10px;box-sizing: border-box;">
                <p style="line-height: 40px"><strong>{dia_1_titulo}</strong></p>
                <p style="line-height: 40px">{dia_1_sub_titulo}</p>
                <img src="{dia_1_img_tempo}" alt="{dia_1_condicao_tempo}" width="48px" height="48px">
                <p style="line-height: 40px">{dia_1_condicao_tempo}</p>
                <p style="line-height: 40px"><span style="color: blue;">Mínima {dia_1_temperatura_minima}Cº</span> - <span style="color: red;">Máxima {dia_1_temperatura_maxima}Cº</p></span>
            </div>
            <div style="margin: 10px; width:230px;padding: 10px;text-align: center;background-color: cornsilk;border-radius: 10px;box-sizing: border-box;">
                <p style="line-height: 40px"><strong>{dia_2_titulo}</strong></p>
                <p style="line-height: 40px">{dia_2_sub_titulo}</p>
                <img src="{dia_2_img_tempo}" alt="{dia_2_condicao_tempo}" width="48px" height="48px">
                <p style="line-height: 40px">{dia_2_condicao_tempo}</p>
                <p style="line-height: 40px"><span style="color: blue;">Mínima {dia_2_temperatura_minima}Cº</span> - <span style="color: red;">Máxima {dia_2_temperatura_maxima}Cº</p></span>
            </div>
            <div style="margin: 10px; width:230px;padding: 10px;text-align: center;background-color: cornsilk;border-radius: 10px;box-sizing: border-box;">
                <p style="line-height: 40px"><strong>{dia_3_titulo}</strong></p>
                <p style="line-height: 40px">{dia_3_sub_titulo}</p>
                <img src="{dia_3_img_tempo}" alt="{dia_3_condicao_tempo}" width="48px" height="48px">
                <p style="line-height: 40px">{dia_3_condicao_tempo}</p>
                <p style="line-height: 40px"><span style="color: blue;">Mínima {dia_3_temperatura_minima}Cº</span> - <span style="color: red;">Máxima {dia_3_temperatura_maxima}Cº</p></span>
            </div>
            <div style="margin: 10px; width:230px;padding: 10px;text-align: center;background-color: cornsilk;border-radius: 10px;box-sizing: border-box;">
                <p style="line-height: 40px"><strong>{dia_4_titulo}</strong></p>
                <p style="line-height: 40px">{dia_4_sub_titulo}</p>
                <img src="{dia_4_img_tempo}" alt="{dia_4_condicao_tempo}" width="48px" height="48px">
                <p style="line-height: 40px">{dia_4_condicao_tempo}</p>
                <p style="line-height: 40px"><span style="color: blue;">Mínima {dia_4_temperatura_minima}Cº</span> - <span style="color: red;">Máxima {dia_4_temperatura_maxima}Cº</p></span>
            </div>
        </div>
    </body>
    </html>
    '''

    mail['From'] = ENDERECO_EMAIL
    mail['To'] = email_usuario
    mail.add_header('Content-Type', 'text/html')
    mail.set_payload(mensagem.encode('utf-8'))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as email:
        email.login(ENDERECO_EMAIL,SENHA_EMAIL)
        email.send_message(mail)
        email.quit()
        print('\n****************************E-mail enviado com sucesso.*************************************\n')
        print('\n****************************Script executado com sucesso, próxima execução em 10 segundos, caso queira interromper script aperte CTRL + C\n')
        
    driver.close

schedule.every(10).seconds.do(app_previsao_tempo)
while True:    
    schedule.run_pending()
    sleep(1)

