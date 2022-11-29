from fudoAutomatizer import automatizador

auto = automatizador("C:\Program Files (x86)\chromedriver.exe", "admin@dawor46159", "36PQToQT", True)

auto.abrirFUDO()

auto.bajarLoop('//*[@id="body"]/main/div/ert-delivery-table-1/div[1]/table/tbody',8,'/html/body/ui-view/ert-delivery/div[2]/main/div/ert-delivery-table-1/div[2]/ert-button/button')
auto.bajarLoop('//*[@id="body"]/main/div/ert-delivery-table-2/div[1]/table/tbody',7,'/html/body/ui-view/ert-delivery/div[2]/main/div/ert-delivery-table-1/div[2]/ert-button/button')