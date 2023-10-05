from selenium import webdriver
from selenium.webdriver.common.by import By
import schedule
import time
import playsound
from gtts import gTTS

  
def login(drive):
    url = ''
    drive.get(url)
    drive.find_element(By.ID,'').send_keys('')
    drive.find_element(By.ID,'').send_keys('')
    drive.find_element(By.NAME,'').click()
    time.sleep(3)
    
    
def adm_conta(drive):
    url = ''
    drive.get(url)
    drive.find_element(By.ID,'').click()
    time.sleep(3)
def solicitar_ticket(drive):
    url = 'http'
    drive.get(url)
    drive.find_element(By.ID,'').click()
    time.sleep(3)
    
    
def executar():
        drive = webdriver.Chrome()
        print('Navegador iniciando')
        while True:
            try:
                print('executando Script')
                login(drive)
                print('login aprovado')
                pass
            except Exception as err:
                print(f'error ao executar script de login\n {err}')
                drive.refresh()
                
            try:
                print('ACESSANDO ADM CONTA')
                adm_conta(drive)
                print( 'ADM ACESSADA')
                pass
            except Exception as err:
                print(f'error ao acessar adm conta\n {err}')
                drive.refresh()
                
            try:
                print('ACESSANDO PAGINA DO SOLICITAR TICKET')
                solicitar_ticket(drive)
                print('SCRIPT NA ULTIMA ETAPA DO PROCESSO COMCLUIDA')
                texto = gTTS('Pagina de solicitaçaõ de Ticket acessada com sucesso alguem por gentileza  poderia reservar o ticket da janta o botao fica la em baixo',lang='pt-br')
                texto.save('audio2.mp3')
                playsound.playsound('audio2.mp3')
                time.sleep(180)
                
            except Exception as err:
                print(f'pagina solicitar ticket nao processada\n {err}')

schedule.every().day.at("11:01").do(executar)

while 1:
    schedule.run_pending()
    time.sleep(1)