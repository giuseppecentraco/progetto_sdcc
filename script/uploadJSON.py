import requests
import os

def createIndex(endpoint_url, index_name, username, password):

  index_url = endpoint_url + index_name

  data = {
    "settings": {
      "index.mapping.total_fields.limit":3000
    },
    "mappings": {
      "properties": {
        "coordinates": {
          "type": "geo_point",
          "ignore_malformed": True
        },
        "created_at" : {
          "type" : "date",
          "format" : "EEE MMM dd HH:mm:ss Z YYYY"
        }
      }
    }
  }

  auth = (username, password)

  response = requests.put(index_url, json=data, auth=auth)
  print("Risultato creazione indice " + response.text)

def uploadJSON(endpoint_url, index_name, file, username, password):

  file_name = "_doc"
  url = endpoint_url + index_name + "/" + file_name

  headers = {
    "Content-Type": "application/json"
  }

  with open(file, "r") as file:
    data = file.readlines()  #il contenuto del file viene memorizzato in data

  auth = (username, password)
  successo = 0
  fallimento = 0

  for i in range(len(data)):
   response = requests.post(url, headers=headers, data=data[i].rstrip(",\n"), auth=auth)

   if "error" not in response:
	   successo+=1
   else:
	   fallimento+=1

  print("Caricamenti con successo " + str(successo) + " su " + str(successo+fallimento))
  print("Caricamenti falliti " + str(fallimento) + " su " + str(successo + fallimento))

def main():

  username = input("Inserisci username: ")
  password = input("Inserisci password: ")
  endpoint_url = input("Inserisci endpoint_url: ")

  index = "indice"

  createIndex(endpoint_url, index, username, password)

  folder_source = input("Inserisci il path della cartella con i json da caricare: ")

  file_list = os.listdir(folder_source)

  for file in file_list:
    uploadJSON(endpoint_url, index,folder_source + "/" + file, username, password)
    print(file + " caricato")


main()