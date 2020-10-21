'''-----------------------------------------------------------------
Python Bot "Friedrich Engels" Version 01.01.01
von Mark Rygielski

Serverspezifische Sachen
-----------------------------------------------------------------'''
import discord
from discord.utils import get
from serverconfic.ids import Channel_ID

async def give_text_in_bot_channel(client, text):
    print (text)
    channel = client.get_channel(int(Channel_ID('bot_output')))
    await channel.send(text)



GENERAL_ROLES = ['everybody', 'Rekrut']

comandprefix = '~'
# ROLES = { role_group: { role_name: emote_name, ... }, ... }
ROLES = {
    'Games': {
        'none': '❌',
        'Rabauken': '💡',
        'Genossen': '🙅',
   },
    'MINT': {
        'Developer': '🔔',
	'Meth': '🎓' 
       }
}
EMOJI_LIST = ['❌', '🙅', '💡', '🔔', '🎓' ]
