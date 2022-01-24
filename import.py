import requests
api_url = "https://dadosabertos.camara.leg.br/api/v2/deputados?idLegislatura=56&ordem=ASC&ordenarPor=nome"
response = requests.get(api_url)
#print(response.status_code)
if response.status_code == 200:
  for i in response.json()["dados"]:
    print(i["urlFoto"])
    img_data = requests.get(i["urlFoto"]).content
    with open(i["nome"] + ".jpg", "wb") as handler:
      handler.write(img_data)