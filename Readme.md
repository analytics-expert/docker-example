# Criando Imagem e Contêiner com Docker

Este repositório contém uma aplicação Flask simples, juntamente com um arquivo Dockerfile para construir uma imagem Docker da aplicação. A seguir, estão as instruções para criar e executar a imagem Docker da aplicação.

## Pré-requisitos

- Instale o [Docker](https://www.docker.com/products/docker-desktop/) em sua máquina.


## Criando imagem Docker

1. Clone este repositório em sua máquina local usando o seguinte comando: 
    ```
    git clone https://github.com/username/docker-example.git
    ```
2. Navegue até a pasta do repositório clonado:
    ```
    cd docker-example
    ```
3. Use o seguinte comando para construir a imagem Docker:

    ```
    $ docker build -t image-example .
    ```


## Executar a aplicação
1. Execute a imagem Docker criada com o seguinte comando:
    ```
    $ docker run --name container-example -p 5000:5000 image-example
    ```
2. Abra o seu navegador web e acesse os endpoitns
    - http://localhost:5000/hello/MeuNome
    - http://localhost:5000/sum/5/7

## Parar a aplicação

1. Use o seguinte comando para parar o contêiner:
    ```
    docker stop container-example
    ```