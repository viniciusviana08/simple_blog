# Projeto de Blog com Flask e MySQL

Este é um projeto de blog desenvolvido em Flask que permite a criação de posts, gerenciamento de usuários e possui autenticação de administrador. O projeto se conecta a um banco de dados MySQL para armazenar as informações.

## Funcionalidades

- Exibição de posts públicos com formatação de datas
- Autenticação de usuários e sessão com Flask
- Gerenciamento de usuários e posts pela área de administrador
- Inserção, edição e exclusão de posts
- Criação e exclusão de usuários
- Autenticação diferenciada para administradores
- Tratamento de erros personalizados (404)

## Tecnologias Utilizadas

- [Flask](https://flask.palletsprojects.com/)
- [MySQL](https://www.mysql.com/)
- HTML/CSS (via templates com [Jinja2](https://jinja.palletsprojects.com/))
## Pré-requisitos

- Python 3.7+
- MySQL
- Pacotes listados em `requirements.txt`:
  - `Flask`
  - `mysql-connector-python`

## Como executar o projeto

1. Clone o repositório:
    ```bash
    git clone https://github.com/viniciusviana08/simple_blog.git
    cd simple_blog
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure as variáveis de ambiente no arquivo `config.py`:
    ```python
    DB_HOST = 'localhost'
    DB_USER = 'seu_usuario'
    DB_PASSWORD = 'sua_senha'
    DB_NAME = 'nome_do_banco'
    SECRET_KEY = 'sua_chave_secreta'
    MASTER_EMAIL = 'admin@example.com'
    MASTER_PASSWORD = 'admin_password'
    ```

5. Configure o banco de dados MySQL:
    - Crie o banco de dados e as tabelas necessárias. Exemplo de criação de tabela:
    ```sql
    CREATE DATABASE nome_do_banco;
    USE nome_do_banco;

    CREATE TABLE usuario (
        id_usuario INT PRIMARY KEY AUTO_INCREMENT,
        nome VARCHAR(255),
        email VARCHAR(255) UNIQUE,
        senha VARCHAR(255)
    );

    CREATE TABLE post (
        id_post INT PRIMARY KEY AUTO_INCREMENT,
        id_usuario INT,
        conteudo TEXT,
        data_post TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
    );
    ```

6. Execute a aplicação:
    ```bash
    flask run
    ```

7. Acesse o projeto no navegador:
    ```
    http://127.0.0.1:5000
    ```

