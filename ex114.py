import requests

def verifica(url):
  try:
    response = requests.get(url)
    if response.status_code == 200:
      print(f"O site {url} está funcionando!")
    else:
      print(f"O site {url} está com problemas. Código de status: {response.status_code}")
  except:
    print(f"Ocorreu um erro ao conectar ao site {url}")

# Exemplo de uso
url = "https://www.google.com"
verifica(url)