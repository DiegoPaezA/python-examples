# Criar uma API para gerenciar arquivos utilizando Flask e Python

## Conteúdo

- [Requirementos](#requerimentos)
- [Descrição](#descrição)
- [Rodar o projeto localmente](#rodar-o-projeto-localmente)
- [Rodar o projeto com Docker](#rodar-o-projeto-com-docker)

---

## Requerimentos

A API deve ser capaz de:

- Requisição para criar um arquivo .csv;
- Requisição para editar um arquivo .csv (enviando dados para adicionar no csv original);
- Requisição para ler de n a m linhas de um arquivo .csv;
- Requisição para retornar valores filtrados com valores menores que um valor X (enviar nome da coluna numérica que será realizada a filtragem);
- Fique a vontade para criar outras funcionalidades.

---

## Descrição

Cliente faz uma solicitação para editar um .txt que já existe. O server faz a edição e responde ao client com a alteração feita.

- Bibliotecas necessárias para esta tarefa: Flask, Requests, json, pandas.
- Pesquise como enviar um texto via requisição HTTP (post, put, get, delete).
- Utilize nomes de variáveis autoexplicativas.

---

## Rodar o projeto localmente

1. Execute o arquivo [app.py](app.py) para iniciar o servidor.
2. O arquivo [client_site](client_site.ipynb) contém um exemplo de como interagir com à API.

---

## Rodar o projeto com Docker

Para compilar a imagem do docker e rodar o container é necessário ter o docker instalado na máquina. Para instalar o docker, siga as instruções do site oficial: https://docker-curriculum.com/#introduction.

As configurações do docker estão no arquivo [Dockerfile](Dockerfile).
O arquivo [requirements.txt](requirements.txt) contém as bibliotecas necessárias para rodar o projeto.


1. Para compilar a imagem do docker, execute o comando abaixo:

```
docker build -t yourusername/apifile .
```
2. Para rodar o container, execute o comando abaixo:

```
docker run -p 8888:5000 yourusername/apifile
```

3. Para testar a API, acesse o endereço http://localhost:8888/ e siga as instruções do arquivo [client_site](client_site.ipynb).