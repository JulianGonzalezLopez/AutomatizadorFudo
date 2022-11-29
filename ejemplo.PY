from fudoAutomatizer import automatizador

auto = automatizador("C:\Program Files (x86)\chromedriver.exe", "a a aa", "No dijiste la palabra magica")

auto.abrirFUDO()

auto.bajarLoop(8)

auto.bajarLoop(7)