# flask_app

** INSTRUCCIONES PARA CONSTRUIR LA IMAGEN DE DOCKER: **

Tenemos una aplicación hecha en Python "app.py", en el repo y también un archivo Dockerfile con todas las configuraciones para crear un contenedor eficiente. Se utiliza una imagen base ligera de Python, se establece un directorio de trabajo, se instalan dependencias sin caché, se crean directorios necesarios, se exponen los puertos y se define el comando predeterminado para ejecutar la aplicación.

Luego contamos con el archivo "requirments.txt"
Al archivo “requirments.txt” en principio solamente le agregamos la línea “Flask==3.0.3” que sería la dependencia inicial, donde indicamos que se debe instalar Flask en la versión 3.0.3.

** Construir la imagen de Docker: **

comando “docker build -t flask_app .”, para construir la imagen con el nombre “flask_app”

Con el comando “docker images” verifico la creación de la misma

------------------------------------------------------------------------------------------------------------------------------------------------------------------
** Ejecutar el contenedor con un volumen de Docker **

comando “docker run -p 5000:5000 -v $(pwd)/data:/data flask_app” 
--> para iniciar el contenedor y asociarlo a un volumen, en este caso estamos “mapeando” el puerto 5000 del contenedor al puerto 5000 del host, y el directorio /data del host, con el directorio /data del contenedor

PARA PROBAR LA PERSISTENCIA: En un navegador, ingresamos a la URL http://localhost:5000 y vemos que el contador comenzó registrando la primera visita (Visitas: 1)

Ingresamos rápidamente unas cuantas veces a la aplicación, hasta llegar 19 visitas (Visitas: 19)

REINICIO DE CONTENEDOR: Se para el contenedor, con el comando “docker stop ‘ID_Contenedor” y al iniciar nuevamente con el comando "docker run..."

Se vuelve a ingresar al navegador y se suma una nueva visita (Vistias: 20), se revisa el archivo "contador.txt" y efectivamente tiene 20

------------------------------------------------------------------------------------------------------------------------------------------------------------------
** Persistencia de datos utilizando un Bind Mount **

Se genera un directorio "bind_data", se conecta directorio “bind_data” del host al directorio /data del contenedor:

comando: “docker run -d -p 5000:5000 -v  /Users/pablonssss/bind_data:/data  flask_app”

PARA PROBAR LA PERSISTENCIA CON BIND MOUNT:

Accedemos a la consola, comienza ahora con el “Visitas: 1”, ingresamos varias veces (30) y generamos que el contador suba hasta 30:
  
REINICIO DE CONTENEDOR: primero con “docker stop ID_CONT”, y se inicia nuevamente con el comando "docker run..."

Pero como el archivo está en el host, residiendo ahí, no tenemos alteraciones en lo que será la “persistencia”, aunque reinicie “n” veces el contenedor
