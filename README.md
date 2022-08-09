# Esto es una Api para verificar la diferencia de dias entre dos fechas

## ¿Que hace esta  Api?

1. Permite Registrarse y hacer login devolviendo un jwt
2. Da la opcion de ingresar dos fechas, y dará como resultado la diferencia de dias que hay entre estas dos 
3. Guardara un historial de las fechas que ha ingresado los usuarios 


## Como usarla o configurla

1. Clona el repositorio o descargalo como zip.

```git clone https://github.com/daniel-canino/api-date.git```

2. Instala las dependencias/librerias en requirements.txt

```pip install -r requirements.txt```

3. Ejecuta las migraciones.

```python manage.py makemigrations```
```python manage.py migrate```

4. Crea un superusuario.

```python manage.py createsuperuser```

5. Corre el servidor.
```python manage.py runserver```

### Link de la api publica 

https://api-date.herokuapp.com/
1. https://api-date.herokuapp.com/
2. https://api-date.herokuapp.com/user/historial
3. https://api-date.herokuapp.com/user/user
4. https://api-date.herokuapp.com/date

### Link de Postman 
https://www.getpostman.com/collections/baa39a49aeedd61082af
