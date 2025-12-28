""" this is a basic code desiged for beginners to learn to use api with requests libaray
in this code we use poke api because it is the most sutable one for beginners this code covers basics
of requests libaray"""
import requests # import libaray
url = "https://pokeapi.co/api/v2/pokemon/" # url of api or api key for certain api
to_source = input("enter name of a pokemon: ")# asks user name of pokemon and stores it in variable
stuff = input("enter anything you want to know about that pokemon: ")# asks info about pokemon and stores it in variable
url = f"https://pokeapi.co/api/v2/pokemon/{to_source}" # final url which will retrive data related to pokemon
response = requests.get(url) # requests.get(url) is used to request data from the url in the url variable
status = response.status_code # this gives gives status code or bacically status of if the request was fullfiled or denyied
print(f"pokemon: {to_source}")# prints pokemon name entered
print(f"data: {response.json()[stuff]}")# prints data requested by user
print(f"status code: {status}")# prints status code
""" this code does not have error handling because it is complex you can imporve this code this code may have bugs
and impovemts are always welcome thanks for checking out my code"""
