import requests
import json
import Resources
import GUI

GUI.WelcomeWindow()
api_key = GUI.apikey

GUI.MainWindow()

server = input('Enter server\n')
summoner_name = input('Enter summoner name\n')
resp = requests.get(f'https://{Resources.servers[server]}/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={api_key}')
summoner = json.loads(resp.content)
print(resp.content)
summ_id = summoner['id']
encr_id = summoner['accountId']
puuid = summoner['puuid']
mastery = requests.get(f'https://{Resources.servers[server]}/lol/champion-mastery/v4/champion-masteries/by-summoner/{summ_id}?api_key={api_key}')
with open('./masterylist.json', 'w') as writef:
    json.dump(json.loads(mastery.content), writef)
with open(r'.\Dragontail\10.24.1\data\en_US\championFull.json', 'r') as readf:
    data = json.load(readf)
print(data['keys'])