import requests
import json
from PIL import ImageTk, Image

servers = {
	'BR1'	: 'br1.api.riotgames.com',
	'EUN1'	: 'eun1.api.riotgames.com',
	'EUW1'	: 'euw1.api.riotgames.com',
	'JP1'	: 'jp1.api.riotgames.com',
	'KR'	: 'kr.api.riotgames.com',
	'LA1'	: 'la1.api.riotgames.com',
	'LA2'	: 'la2.api.riotgames.com',
	'NA1'	: 'na1.api.riotgames.com',
	'OC1'	: 'oc1.api.riotgames.com',
	'TR1'	: 'tr1.api.riotgames.com',
	'RU'	: 'ru.api.riotgames.com'
}


class LOL:
    def __init__(self,key :str):
        self.key = key
        with open('./Dragontail/10.25.1/data/en_US/championFull.json', 'r') as file:
            self.championdata = json.load(file)

    def get_summoner_id(self, region, summoner):
        resp = requests.get(f'https://{servers[region]}/lol/summoner/v4/summoners/by-name/{summoner}?api_key={self.key}')
        if resp.status_code != 200:
            return -1
        summonerdata = json.loads(resp.content)
        self.summ_id = summonerdata['id']
        return self.summ_id

    def get_champion_data(self,summoner,region,champions_amount):       
        summ_id = self.get_summoner_id(region, summoner)
        if summ_id == -1:
            return -1
        resp = requests.get(f'https://{servers[region]}/lol/champion-mastery/v4/champion-masteries/by-summoner/{summ_id}?api_key={self.key}')
        mastery = json.loads(resp.content)
        keys = self.championdata['keys']
        champions = {}
        for champion in mastery[:champions_amount]:
            championkey = str(champion['championId'])
            champions[keys[championkey]] = champion['championPoints']
        return champions

    def get_champion_image(self,name):
        img = Image.open(f'./Dragontail/img/champion/splash/{name}_0.jpg')
        return ImageTk.PhotoImage(image=img)

    def get_rank_image(self, rank):
        img = Image.open(f'./Resources/{rank}.png')
        return ImageTk.PhotoImage(image=img)

    def get_summoner_league(self, region):
        resp = requests.get(f'https://{servers[region]}/lol/league/v4/entries/by-summoner/{self.summ_id}?api_key={self.key}')
        leaguedata = json.loads(resp.content)
        return leaguedata




