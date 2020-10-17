'''-----------------------------------------------------------------
Python Bot "Friedrich Engels" Version 01.02.01
von Mark Rygielski

Stellt nach dem Verbinden des Bott alle wichtige Sachen ein

Externe Datein (im selben Ordner):
- .ent mit dem Token
-----------------------------------------------------------------'''
import discord

from textoutput.system_messages import startupmessage
from serverconfic.ids import Channel_ID

def start(client):
    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))
        txt = startupmessage()
        channel = client.get_channel(Channel_ID('bot_output'))
        await channel.send(txt.format(client))
        


