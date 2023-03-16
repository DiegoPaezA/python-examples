# Criar uma API para gerenciar arquivos utilizando Flask e Python

A API deve ser capaz de:

- Requisição para criar um arquivo txt;
- Requisição para ler um arquivo txt;
- Requisição para atualizar um arquivo txt;

Utilizando POST enviamos para http://127.0.0.1:5000/update_file
```
{
    "mensagem": "Arquivo editado",
    "data": [
        "O arquivo criado foi prueba1.txt 1989 \n",
        " D 1989"
    ]
}
```

## Descrição

Cliente faz uma solicitação para editar um .txt que já existe. O server faz a edição e responde ao client com a alteração feita.

* Bibliotecas necessárias para esta tarefa: Flask, Requests, json. 
* Pesquise como enviar um texto via requisição HTTP (post, put, get, delete).
* Utilize nomes de variáveis autoexplicativas.