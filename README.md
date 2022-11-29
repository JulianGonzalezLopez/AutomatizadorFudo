# AutomatizadorFudo
<h4 align="center">:construction: Proyecto en construcción :construction:</h4>
Pequeño script de python que te ahorra apretar mil veces el boton de bajar pedidos

##A saber:
  -La clase automatizador recibe 3 argumentos, la  direccion en la que tengas guardado el chromedriver, tu usuario y tu pass de fudo
  -Una vez creada la instancia, debemos llamar a los metodos:
    ...auto.abrirFUDO() => Abre la pagina y calza las credenciales
    ...auto.bajarLoop(8) => Baja los pedidos "Naranjas" (los de arriba)
    ...auto.bajarLoop(7) => Baja los pedidos "Amarillos" (los de abajo)
    
 ##Dependencias:
  Para usar este script necesitamos:
    -Python
    -La libreria Selenium
    -Chromedriver (A futuro buscaré que acepte otros navegadores)
