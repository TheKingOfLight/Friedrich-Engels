'''-----------------------------------------------------------------
Python Bot "Friedrich Engels" Version 01.02.01
von Mark Rygielski

Aufgabe:
Wenn im entsprechendem Channel eine Reation hinzugefügt wird, soll der
Bot dem User eine zur Reaction passende rolle geben
-----------------------------------------------------------------'''

import discord, os, re
from discord.utils import get

from serverconfic.ids import Channel_ID
from textoutput.user_messages import vote_message
from textoutput.user_messages import added_role
from textoutput.error_messages import error1
from serverconfic.server import ROLES
from serverconfic.server import EMOJI_LIST


#Ermittelt die Rolle, die mit einem Emoji Zusammenhängt
def from_raction_get_role(reaction):

    emoji = reaction.emoji
    if reaction.custom_emoji:
        emoji = reaction.emoji.name
        
    for subgroup in ROLES.values():
        for r, e in subgroup.items():
            if e == emoji:
                return r
    return None
    
def on_reaction_add_role(client):

    #Die Nachricht, auf die Reagiert werden soll, muss im Cash sein.
    #Daher muss diese nach dem Neustart erneut gesendet werden:
    @client.event
    async def on_ready():
        channel = client.get_channel(Channel_ID('vote'))
        text =  vote_message()
        
        message = await channel.send(text)
        number_emoji = len(EMOJI_LIST)

        for i in range(0, number_emoji):
            await message.add_reaction(EMOJI_LIST[i])
            #fügt de Nachricht alle emojis hinzu, die benötigt wernen

      
    @client.event
    async def on_reaction_add(reaction, user):
        #wird ausgelößt, wenn jemand irgenwo reagiert

        #Tests ob die Reaktion ignoriert werden soll:
        if user == client.user:
            #test, ob es der Bot selber war
            return
        channel = client.get_channel(int(Channel_ID('vote')))
        if reaction.message.channel != channel:
            #test, ob der richtige Channel
            return


        role = from_reaction_get_role(raction)
        try:
            await user.add_roles(role)
            text = str(added_role()+user.name)
            channel = client.get_channel(int(Channel_ID('vote')))
            await channel.send(text)
        except discord.Forbidden:
            channel = client.get_channel(int(Channel_ID('vote')))
            await channel.send(error1(6))
            return

