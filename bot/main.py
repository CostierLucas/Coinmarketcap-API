from requests import Request, Session
import requests
import json
from discord_webhook import DiscordWebhook, DiscordEmbed
import datetime

webhook = DiscordWebhook(
    url='WEBHOOK-URL')


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'YOUR API KEY',
}
parameters = {
    'start': '1',
    'limit': '5',
    'convert': 'USD',
}

json = requests.get(url, params=parameters, headers=headers).json()

coins = json['data']
embed = DiscordEmbed(
    title=':chart_with_upwards_trend: COURS CRYPTO', color='03b2f8')
for x in coins:
    embed.add_embed_field(
        name=str(x['symbol']), value=str(x['quote']['USD']['price'])[0:9])
    embed.add_embed_field(name=chr(173), value=chr(173))
    embed.add_embed_field(name=chr(173), value=chr(173))

webhook.add_embed(embed)
response = webhook.execute()
