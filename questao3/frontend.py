import sys
import os

# O caminho para onde está seu código Flask
path = '/home/GustavoGranero/mysite'  # Substitua pelo caminho correto onde seu aplicativo está localizado
if path not in sys.path:
    sys.path.append(path)

from app import app as application

# Defina a secret_key para a aplicação
application.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # Insira sua chave secreta aqui

# O servidor WSGI espera a aplicação ser chamada 'application'
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
