# Docker servidores db

## Comenzando 🚀

Estas instrucciones le permitirán configurar las siguientes bases de datos.

### Pre-requisitos 📋

_- Sistemas operativo **linux**_
_- Instalar  [docker](https://docs.docker.com/install/)_
_- Instalar [docker compose](https://docs.docker.com/compose/)_


### Archivo docker-compose.yml
_Comenzaremos configurando una red para las bases de datos._
>Crear archivo docker-compose.yml
```bash
user@debian:~/Documents/Docker/databases$ nano docker-compose.yml
```
```yaml
version: '3.7'

services:
  ...
networks:
   - databases

```
### MYSQL
_Gestionando configuración de ***mysql***._
>Agregando configuración a docker-compose.yml
```bash
user@debian:~/Documents/Docker/databases$ nano docker-compose.yml
```
```yaml
version: '3.7'


services:
 
 mysql:
  image: mysql:${MYSQL_VERSION}
  restart: always
  ports:
   - ${MYSQL_PORT_LOCAL}:${MYSQL_PORT_DEFAULT}
  environment:
   MYSQL_ROOT_PASSWORD: ${MY_MYSQL_ROOT_PASSWORD}
   MYSQL_USER: ${MY_MYSQL_USER}
   MYSQL_PASSWORD: ${MY_MYSQL_USER_PASSWORD}
   MYSQL_DATABASE: ${MY_MYSQL_DB}
  volumes:
   - ./mysql/db:/var/lib/mysql:rw
   - ./mysql/log:/var/lib/log:rw
  networks:
   - databases
 ...
networks:
   - databases 
```
_La carpeta **mysql/db**  nos permite persistir la información de las bases de datos que gestionemos y la carpeta **mysql/log** nos permite persistir la información de los logs._
>Creando estructura de carpetas:
```bash
user@debian:~/Documents/Docker/databases$ mkdir mysql && mkdir mysql/db && mkdir mysql/log
```
_Dentro del archivo **.env**  podemos gestionar las variables de configuración._

>Creando archivo .env:

```bash
user@debian:~/Documents/Docker/databases$ nano .env
```
>las variables de entorno se definen de la siguiente forma dentro del archivo .env
```bash
# VARIABLES MYSQL
MY_MYSQL_ROOT_PASSWORD=123456
MY_MYSQL_USER=demo
MY_MYSQL_USER_PASSWORD=demo
MY_MYSQL_DB=demo
MYSQL_VERSION=5.7
MYSQL_PORT_DEFAULT=3306
MYSQL_PORT_LOCAL=3306
```
### POSTGRES
_Gestionando configuración de ***postgres***._
>Agregando configuración a docker-compose.yml
```bash
user@debian:~/Documents/Docker/databases$ nano docker-compose.yml
```
```yaml
version: '3.7'


services:
 ...
 postgres:
  image: postgres:${POSTGRES_VERSION}
  restart: always
  ports:
   - ${POSTGRES_PORT_LOCAL}:${POSTGRES_PORT_DEFAULT}
  environment:
   POSTGRES_ROOT_PASSWORD: ${MY_POSTGRES_ROOT_PASSWORD}
   POSTGRES_USER: ${MY_POSTGRES_USER}
   POSTGRES_PASSWORD: ${MY_POSTGRES_USER_PASSWORD}
   POSTGRES_DB: ${MY_POSTGRES_DB}
  volumes:
   - ./postgres/db:/var/lib/postgresql/data
   - ./postgres/log:/var/lib/postgresql/log
  networks:
   - databases
 ...
networks:
  - databases
```
_La carpeta **postgres/db**  nos permite persistir la información de las bases de datos que gestionemos y la carpeta **postgres/log** nos permite persistir la información de los logs._
>Creando estructura de carpetas:
```bash
user@debian:~/Documents/Docker/databases$ mkdir postgres && mkdir postgres/db && mkdir postgres/log
```
_Dentro del archivo **.env**  añadimos las variables._
```bash
user@debian:~/Documents/Docker/databases$ nano .env
```
```bash
# VARIABLES POSTGRES
MY_POSTGRES_ROOT_PASSWORD=123456
MY_POSTGRES_USER=demo
MY_POSTGRES_USER_PASSWORD=demo
MY_POSTGRES_DB=demo
POSTGRES_VERSION=9.4
POSTGRES_PORT_DEFAULT=5432
POSTGRES_PORT_LOCAL=5432
```
### MONGO
_Gestionando configuración de ***mongo***._
>Agregando configuración a docker-compose.yml
```bash
user@debian:~/Documents/Docker/databases$ nano docker-compose.yml
```
```yaml
version: '3.7'


services:
 ...
 mongo:
  image: mongo:${MONGO_VERSION}
  restart: always
  ports:
   - ${MONGO_PORT_LOCAL}:${MONGO_PORT_DEFAULT}
  volumes:
   - ./mongo/db:/data/db
  networks:
   - databases
 ...
networks:
  - databases
```
_La carpeta **mongo/db**  nos permite persistir la información de las bases de datos que gestionemos._
>Creando estructura de carpetas:
```bash
user@debian:~/Documents/Docker/databases$ mkdir mongo && mkdir mongo/db
```
_Dentro del archivo **.env**  añadimos las variables._
```bash
user@debian:~/Documents/Docker/databases$ nano .env
```
```bash
# VARIABLES MONGO
MONGO_VERSION=latest
# Mongo utiliza el siguiente rango de puertos para sus servicios.
MONGO_PORT_DEFAULT=27017-27019
MONGO_PORT_LOCAL=27017-27019
```

### REDIS
_Gestionando configuración de ***redis***._
>Agregando configuración a docker-compose.yml
```bash
user@debian:~/Documents/Docker/databases$ nano docker-compose.yml
```
```yaml
version: '3.7'


services:
 ...
 redis:
  image: redis:${REDIS_VERSION}
  restart: always
  ports:
   - ${REDIS_PORT_LOCAL}:${REDIS_PORT_DEFAULT}
  volumes:
   - ./redis/data:/data:rw
  networks:
   - databases
 ...
networks:
  - databases
```
_La carpeta **redis/db**  nos permite persistir la información de las bases de datos que gestionemos._
>Creando estructura de carpetas:
```bash
user@debian:~/Documents/Docker/databases$ mkdir redis && mkdir redis/db
```
_Dentro del archivo **.env**  añadimos las variables._
```bash
user@debian:~/Documents/Docker/databases$ nano .env
```
```bash
# VARIABLES REDIS
REDIS_VERSION=latest
REDIS_PORT_DEFAULT=6379
REDIS_PORT_LOCAL=6379
```

### FIREBIRD
_Gestionando configuración de ***firebird***._
>Agregando configuración a docker-compose.yml
```bash
user@debian:~/Documents/Docker/databases$ nano docker-compose.yml
```
```yaml
version: '3.7'


services:
 ...
 firebird:
   image: kpsys/firebird
   volumes:
     - ./firebird/db:/usr/local/firebird/data
   ports:
      - ${FIREBIRD_PORT_LOCAL}:${FIREBIRD_PORT_DEFAULT}
   networks:
      - databases
 ...
networks:
  - databases
```
_La carpeta **firebird/db**  nos permite persistir la información de las bases de datos que gestionemos._
>Creando estructura de carpetas:
```bash
user@debian:~/Documents/Docker/databases$ mkdir firebird && mkdir firebird/db
```
_Dentro del archivo **.env**  añadimos las variables._
```bash
user@debian:~/Documents/Docker/databases$ nano .env
```
```bash
# VARIABLES FIREBIRD
FIREBIRD_PORT_DEFAULT=3050
FIREBIRD_PORT_LOCAL=3050
```

## Autores ✒️

* **Jeaneil Bernal Sierra**
* **Cristian Narvaez Useche** 
* **Leonardo Seña Pimentel** 




