> Todos os repositórios do #DevOpsRN encontram-se no link https://github.com/jerimumhs/cpnatal2

# Workshop Intrudução a containers com Docker #CPNatal2
Repositório para a parte prática do workshop. 
Nessa parte, utilizaremos diversos comandos docker para rodar alguns containers.

>Para essa parte prática, é necessário ter o [docker](https://docs.docker.com/install/) e o [docker-compose](https://docs.docker.com/compose/) instalados


# Rodando nginx
Com o comando `pull` baixamos a imagem mais recente do nginx
```shell script
$ docker pull nginx
```

Utilizamos o comando `create` para criar um container da imagem nginx.
```shell script
$ docker create -p 80:80 --name nginx_container nginx
```
>Nesse caso específico, estamos utilizando `-p 80:80` para conectar a porta 80 do container com a porta 80 da nossa máquina

>Estamos nomeando o container utilizando o `--name nginx_container`

Podemos ver todos os containers com o seguinte comando
```shell script
$ docker ps -a
```

Para iniciar o container, utilizamos o comando `docker start`
```shell script
$ docker start nginx_container
```

Com o comando `ps` vemos a lista de containers que estão rodando
```shell script
$ docker ps
```

Podemos inspecionar o log do nosso container utilizando `attach`
> Basta dar CTRL + C para desconectar nosso terminal do container
```shell script
$ docker attach nginx_container
```

Para parar o container utilizamos o `stop`
```shell script
$ docker stop nginx_container
```

Para excluir o nosso container utilizamos o `rm`
```shell script
$ docker rm nginx_container
```

Para excluir a imagem do nginx utilizamos o `rmi`
```shell script
$ docker rmi nginx
```

# Rodando server
Entre na pasta `server` para rodar a aplicação encontrada lá.
> ao contrário do nginx (no qual baixamos a imagem pura e rodamos ela), iremos construir a imagem do nosso server, por isso temos um `Dockerfile` na pasta

Para construir a imagem do server utilizando o `build`
```shell script
$ docker build . -t cpnatal2_intro-docker_server
```
> No comando estamos construindo a imagem na pasta atual (logo o `.`)

> Estamos nomeando nossa imagem com o argumento `-t cpnatal2_intro-docker_server` 

Criamos o container com o comando `create`
```shell script
$ docker create --name server -p 8000:8000 cpnatal2_intro-docker_server
```

Rodamos nosso container com o comando `start`
```shell script
$ docker start server
```

# Rodando requester
Entre na pasta `requester` para rodar a aplicação encontrada lá.
> da mesma forma do server, construiremos a imagem do requester. Por isso temos um `Dockerfile` na pasta

Para construir a imagem do server utilizando o `build`
```shell script
$ docker build . -t cpnatal2_intro-docker_requester
```
> No comando estamos construindo a imagem na pasta atual (logo o `.`)

> Estamos nomeando nossa imagem com o argumento `-t cpnatal2_intro-docker_server` 

Criamos o container com o comando `create`
```shell script
$ docker create --name requester -e "HOST_URL=server" --link server cpnatal2_intro-docker_requester
```
> Estamos utilizando o arqumento `-e "HOST_URL=server"` para passar para nosso container a variável de ambiente `HOST_URL` com o valor `server`

> Como cada container é isolado, precisamos utilizar o argumento `-link server` para que nosso container requester possa ver nosso server

Rodamos nosso container com o comando `start`
```shell script
$ docker start requester
```

# Utilizando docker-compose para rodar server + requester
> O docker-compose é uma ferramenta para orquestrar um conjunto de containers. A configuração dele encontra-se no arquivo `docker-compose.yml`

Para construir as imagens dos serviços do docker-compose utilizamos o `build`
```shell script
$ docker-compose build
```

Para rodar todos os serviços do docker-compose utilizamos o `up`
```shell script
$ docker-compose up
```
