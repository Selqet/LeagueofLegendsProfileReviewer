import requests
import json
api_key = input('Enter api\n')
summoner_nickname = input('Enter summoner name\n')
resp = requests.get(f'https://ru.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_nickname}?api_key={api_key}')
summoner = json.loads(resp.content)
print(resp.content)
summ_id = summoner['id']
encr_id = summoner['accountId']
puuid = summoner['puuid']
mastery = requests.get(f'https://ru.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{summ_id}?api_key={api_key}')
print(mastery.content)
with open('F:/Python/project/masterylist.json', 'w') as writef:
    json.dump(json.loads(mastery.content), writef)

