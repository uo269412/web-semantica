<h1>Ejercicio Web Semántica</h1>
<h2>Ejercicio 1</h2>
    <p>Para ejecutar el código de ejercicio 1 hará falta ejecutarlo utilizando Python. Yo he utilizado Pycharm 2022 y la versión 3.9 de Python.</p>
    <h3>Enlace a los recursos utilizados</h3>
    <ul>
        <li><a href="https://data.europa.eu/data/datasets/https-datosabiertos-jcyl-es-web-jcyl-set-es-comercio-artesanosalimentarios-1284266159759?locale=en">Enlace al CSV de registro mercantil </a>(Cabe mencionar que se ha tenido que retocar el CSV ya que tenía formato erróneo</li>
        <li><a href="https://schema.org/Organization">Enlace al schema de organización</a>(Tratado como empresa que está registrada en el Registro Mercantil)</li>
        <li><a href="https://schema.org/RegisterAction">Enlace al schema de registro</a></li>
        <li><a href="https://schema.org/PostalAddress">Enlace al schema de Postal Address</a>(Tratado como localización de la empresa)</li>
        <li><a href="https://schema.org/Person">Enlace al schema de Person</a>(Tratado como trabajador de contacto de la empresa)</li>
    </ul>
    <h3>Enlace a los desliegues de los almacenes RDF (Se necesita conexión con el Internet de la Universidad)</h3>
    <ul>
        <li><a href="http://156.35.98.38:3030">URL Apache Jena</a>[Máquina Windows]</li>
        <li><a href="http://156.35.98.37:9999">URL Blazegraph</a>[Máquina Ubuntu]</li>
    </ul>
<h2>Ejercicio 2</h2>
    <p>Se ha realizado tanto la validación de shex como la de shacl.</p>
<h2>Ejercicio 3</h2>
    <p>En referencias.txt obtenenos información acerca de la funcionalidad de cada consulta. Se pueden realizar tanto en BlazeGraph como en Apache Fuseki Jena.</p>
    <h3>Consultas</h3>
    <ul>
        <li><b>Consulta 1: </b>Número total de empresas que se dedican a un departamento en específico del registro mercantil.</li>
        <li><b>Consulta 2: </b>Consulta que obtiene el municipio que tiene menos organizaciones.</li>
        <li><b>Consulta 3: </b>Localidad y número total de empresas que se encuentran en una situación alta dentro de esa localidad, ordenadas de mayor a menor.</li>
       <li><b>Consulta 4: </b>Email y página web de aquellas empresas que tengan una página web que acabe en .es y un correo que contenga "@" "mail" y acabe en ".com".</li>
    </ul>
    <ins>El resultado de las consultas se puede ver en el vídeo realizado.</ins>
<h2>Ejercicio 4</h2>
    <p>Se ha creado una aplicación web que utiliza el almacén de Apache Fuseki Jena para realizar una consulta SPARQL. Tendremos dos filtros, pudiendo elegir uno de los departamentos que hay, y también pudiendo escribir de forma manual la localidad en la cual queremos encontrar. Para acceder a la aplicación, podremos entrar en el <a href= "http://156.35.98.38:90/web-semantica" >siguiente enlace</a>(con el despliegue algunos caracteres no se procesan de manera correcta) o abrir el archivo index.html (aqui los archivos se procesan de manera correcta). Se necesitaría conexión en el Internet de la Universidad.</p>
