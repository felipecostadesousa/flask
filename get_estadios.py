import requests

def get_estadios(url="http://localhost:8080/Estadio"):
  try:
    response = requests.get(url)
    response.raise_for_status()
    print("Status Code:", response.status_code)
    return response.json()
  except requests.exceptions.RequestException as e:
    print("Erro na requisição:", e)
  except ValueError:
    print("Resposta não é um JSON:", response.text)