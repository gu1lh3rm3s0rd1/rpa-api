Este projeto contém uma API para armazenar e recuperar dados climáticos e um RPA que extrai informações de clima do Google.

## Estrutura do Projeto
- `app.py`: Código da API Flask.
- `rpa.py`: Código do RPA usando Selenium.
- `clima.db`: Banco de dados SQLite para armazenar os dados da raspagem.
- `.gitignore`: Arquivos e diretórios a serem ignorados pelo Git.
- `requirements.txt`: Dependências necessárias a serem instaladas.
- `test/`: Pasta com códigos teste.

## Pré-requisitos
- Python 3.x
- Pip (gerenciador de pacotes do Python)
- Google Chrome

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/gu1lh3rm3s0rd1/rpa-api.git
    cd rpa-api
    ```

2. Crie um ambiente virtual e ative-o:
    ```sh
    python -m venv venv
    venv\Scripts\activate  # No Windows
    source venv/bin/activate  # No Git
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

## Execução da API

1. Inicie a API Flask:
    ```sh
    python app.py
    ```

2. A API estará disponível em `http://localhost:5000`.

## Execução do RPA

1. Execute o script do RPA em outro terminal:
    ```sh
    python rpa.py
    ```
2. Ou se preferir pode usar o endpoint `/rpa`.

3. O RPA extrairá as informações de clima do Google e enviará para a API.

## Endpoints da API

- `POST /store-data`: Endpoint que recebe os dados extraídos pelo RPA e os armazena no banco de dados.
- `GET /list-data`: Endpoint que retorna os dados armazenados no banco de dados.
- `GET /rpa`: Endpoint que executa o script do RPA e ativa o endpoint /store-data.

## Tecnologias Utilizadas
- Python
- Flask (Framework para a API)
- Flask-RESTX (Swagger e documentação da API)
- SQLite (Banco de dados)
- Selenium (Automação de navegador)
