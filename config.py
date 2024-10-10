ambiente = 'teste'

if ambiente == 'teste':
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWORD = 'senai'
    DB_NAME = 'blog'

if ambiente == 'producao':
    DB_HOST = 'Vinicius0803.mysql.pythonanywhere-services.com'
    DB_USER = 'Vinicius0803'
    DB_PASSWORD = 'Renato99'
    DB_NAME = 'Vinicius0803$blog'


# CONFIG CHAVE SECRETA DE SESSÃO
SECRET_KEY = 'blog'

# SENHA DO ADM
MASTER_EMAIL = 'adm@adm'
MASTER_PASSWORD = 'adm123'