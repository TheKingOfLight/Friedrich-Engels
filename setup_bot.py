'''-----------------------------------------------------------------
Python Bot "Friedrich Engels" Version 01.02.01
von Mark Rygielski

Stellt nach dem Verbinden des Bott alle wichtige Sachen ein

-----------------------------------------------------------------'''
import discord

from textoutput.system_messages import startupmessage
from serverconfic.ids import Channel_ID
from serverconfic.server import give_text_in_bot_channel

def start(client):
    @client.event
    async def on_ready():
        print ('1')
        text = ('We have logged in as {0.user}'.format(client))
        give_text_in_bot_channel(client, text)
        txt = startupmessage()
        channel = client.get_channel(int(Channel_ID('bot_output')))
        await channel.send(txt.format(client))
        


