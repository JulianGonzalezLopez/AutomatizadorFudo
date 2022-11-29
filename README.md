# AutomatizadorFudo
<h4>:construction: Proyecto en construcción :construction:</h4>
Pequeño script de python que te ahorra apretar mil veces el boton de bajar pedidos
<h4>A saber</h4>
  <p>-La clase automatizador recibe 3 argumentos, la  direccion en la que tengas guardado el chromedriver, tu usuario y tu pass de fudo.</p>
  <p>-Una vez creada la instancia, debemos llamar a los metodos:</p>
  <ul>
    <li> auto.abrirFUDO(): Abre la pagina y calza las credenciales</li>
    <li> auto.bajarLoop(8): Baja los pedidos "Naranjas" (los de arriba)</li>
    <li> auto.bajarLoop(7): Baja los pedidos "Amarillos" (los de abajo)</li>
  </ul>
    
<h4>Dependencias</h4>
  <p>Para usar este script necesitamos:</p>
  <ol>
    <li>-Python</li>
    <li>-La libreria Selenium</li>
    <li>-Chromedriver (A futuro buscaré que acepte otros navegadores)</li>
  </ol>
