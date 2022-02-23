# API de Contratos de Usuários

## Introdução

Esse projeto tem como objetivo principal coletar e classificar dados de Contratos de usuários. Para isso, é alimentado por duas fontes externas de dado, os classifica e os retorna, de forma paginada, por meio de um `endpoint`.

## Principais Tecnologias

- [Python 3](https://www.python.org/)  
    - Linguagem base utilizada para a implementação do projeto.
- [FastAPI](https://fastapi.tiangolo.com/)  
    - Microframework comumente utilizado para a criação de APIs simples.
- [Docker](https://www.docker.com/)  
    - Conteinerizador de sistemas.
- [Docker Compose](https://docs.docker.com/compose/)  
    - Utilziado para orquestração dos containers.

## Realizando a Build

Para montar a build do projeto e o executar, na pasta raíz, execute em seu terminal:

```cmd
$ docker-compose up --build
```

- Caso tudo ocorra bem, o projeto estará rodando na porta **8080**:
    - http://localhost:8080/
### Principais Rotas

- **Health Check**
    - Verifica se o sistema está online.
    - **GET**: `http://localhost:8080/`
        - Exemplo de resposta: `{"status":"ok"}`

- **Customers**
    - Retorna uma página de dados de usuários.
    - **GET**: `http://localhost:8080/customers?country=<CÓDIGO DE PAÍS>&region=<REGIÃO>&classification=<CLASSIFICAÇÃO>&page=<PÁGINA>`
    - Parâmetros:
        - country: Atualmente aceita somente o código `'BR'`
        - região: `'centro', 'centro-oeste', 'centro-leste', 'centro-sul','centro-norte', 'norte', 'nordeste', 'leste', 'sudeste', 'sul', 'sudoeste', 'oeste', 'noroeste'`
        - classifiacação do usuário: `'laborious', 'especial', 'normal'`
        - pagina: Inteiro referente à pagina requerida. Ex.: 6
    - Exemplo de chamada: `http://localhost:8080/customers?country=BR&region=sudeste&classification=laborious&page=6`
    - Exemplo de Resposta:
```json
{
	"pageNumber": 6,  // Numero da página atual
	"pageSize": 10,  // Tamanho da lista de usuários
	"totalCount": 304,  // Total de usuários
	"users": ["..."]  // Lista de usuários
}
```
    - **Obs.:** São retornados 10 usuários por página

### Testes Unitários

O sistema possuí alguns testes unitários. Para executa-los, no terminal, execute:

```cmd
$ docker-compose exec api pytest
```


### Linter

Para garantir uma melhor legibilidade de código, foi utilizado o `flake8`.
Para verificar se os arquivos estão seguindo as regras de legibilidade, execute:

```cdm

$ docker-compose exec api flake8

```
