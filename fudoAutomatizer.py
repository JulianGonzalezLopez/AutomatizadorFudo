from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time


class automatizador():

    caminoN = '//*[@id="body"]/main/div/ert-delivery-table-1/div[1]/table/tbody'
    caminoBotonN = '/html/body/ui-view/ert-delivery/div[2]/main/div/ert-delivery-table-1/div[2]/ert-button/button'
    caminoA = '//*[@id="body"]/main/div/ert-delivery-table-2/div[1]/table/tbody'
    caminoBotonA = '/html/body/ui-view/ert-delivery/div[2]/main/div/ert-delivery-table-1/div[2]/ert-button/button'

    def __init__(self, PATH, username, password, headless = True):
        chrome_options = Options()
        print(headless)
        if(headless == True):
            chrome_options.headless = True

        self.driver = webdriver.Chrome(PATH, options=chrome_options)
        self.username = username
        self.password = password


    def __str__(self):
        return f"Object of class automatizador. User = {self.username} -- Password: {self.password}"
 
    def bajarPedidos(self,tipoDePedido,ochoOsiete):
        mesa = 0
        if ochoOsiete == 8:
            print('INICIANDO BAJADO DE PEDIDOS: NARANJAS')
        else:
            print('INICIANDO BAJADO DE PEDIDOS: AMARILLOS')
        mesa = self.driver.find_element(By.XPATH,tipoDePedido)
        pedidosABajar = mesa.find_elements(By.TAG_NAME,"tr")
        print("Cantidad de pedidos a bajar: " + str(len(pedidosABajar)))

        for i in range(0,len(pedidosABajar)-1):
            time.sleep(0.3)
            try:
                pedidosABajar[i].find_element(By.XPATH,'td[' + str(ochoOsiete) + ']/ert-icon-button/button').click()
            except WebDriverException:
                print("Faltan confirmar")

    def mostrarMasLoopV2(self,caminoBoton,num):
        print('INICIANDO APRETADO DE MOSTRAR MAS')
        if(num == 7):
            cantidad = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/ui-view/ert-delivery/div[2]/main/div/ert-delivery-table-1/h3/span[2]/span[2]'))).text
        else:
            cantidad = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/ui-view/ert-delivery/div[2]/main/div/ert-delivery-table-2/h3/span[2]'))).text
        aux = ""
        print(cantidad)
        while(aux != cantidad):

            aux = cantidad

            time.sleep(1)
            try:
                btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,caminoBoton)))
                btn.click()
            except:
                print('No hay mas elementos para mostrar')

            time.sleep(1)

            if(num == 7):
                cantidad = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/ui-view/ert-delivery/div[2]/main/div/ert-delivery-table-1/h3/span[2]/span[2]'))).text
            else:
                cantidad = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/ui-view/ert-delivery/div[2]/main/div/ert-delivery-table-2/h3/span[2]'))).text
                
            print(f"Cantidad anterior: {aux}. Cantidad nueva: {cantidad}")


    def bajarLoop(self,num):
        if(num == 8):

            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,self.caminoN)))
            time.sleep(5)
            self.mostrarMasLoopV2(self.caminoBotonN, num)
        else:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,self.caminoN)))
            time.sleep(5)
            self.mostrarMasLoopV2(self.caminoBotonA, num)

        time.sleep(5)

        if(num == 8):
            self.bajarPedidos(self.caminoN, num)
        else:
            self.bajarPedidos(self.caminoA, num)

        time.sleep(5)
        self.driver.refresh()
    
    def abrirFUDO(self):
        self.driver.get("https://app-v2.fu.do/login.html")
        time.sleep(5)
        #Obtenemos los 3 elementos a interactuar en la pagina
        userBox = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="user"]')))
        passwordBox = self.driver.find_element(By.XPATH,'//*[@id="password"]')
        sendButton = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/button')
        #Hacemos un clear para evitar usar info previa
        userBox.clear()
        passwordBox.clear()
        #Enviamos USERNAME Y PASSWORD como credenciales
        userBox.send_keys(self.username)
        passwordBox.send_keys(self.password)
        #Enviamos la info
        sendButton.click()
        #Esperamos a que se genere el deliveryButton y se clickea
        deliveryButton = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/ui-view/ert-tables/div[1]/ert-tables-subtop/ul/li[3]/a')))
        deliveryButton.click()



auto = automatizador("C:\Program Files (x86)\chromedriver.exe", "a a aa", "No dijiste la palabra magica")

auto.abrirFUDO()

auto.bajarLoop(8)

auto.bajarLoop(7)