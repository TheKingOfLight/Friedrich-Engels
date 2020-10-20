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
from textoutput.user_messages import already_has_role_text
from textoutput.error_messages import error1
from serverconfic.server import ROLES
from serverconfic.server import EMOJI_LIST
from serverconfic.server import give_text_in_bot_channel
from serverconfic.ids import Server_ID
from role_management.untis import from_raction_get_role
from role_management.untis import user_has_role
from role_management.untis import should_ignore_reaction
from serverconfic.server import give_text_in_bot_channel

   
def on_reaction_add_role(client):

    #Die Nachricht, auf die Reagiert werden soll, muss im Cash sein.
    #Daher muss diese nach dem Neustart erneut gesendet werden:
    @client.event
    async def on_ready():
        channel = client.get_channel(int(Channel_ID('vote')))
        text =  vote_message()
        
        message = await channel.send(text)
        guild = client.get_guild(id = int(Server_ID()))
        number_emoji = len(EMOJI_LIST)

        for i in range(0, number_emoji):
            emoji_name = EMOJI_LIST[i]
            await message.add_reaction(emoji_name)
            #fügt de Nachricht alle emojis hinzu, die benötigt wernen

      
    @client.event
    async def on_reaction_add(reaction, user):
        #wird ausgelößt, wenn jemand irgenwo reagiert
        if not should_ignore_reaction(client, user, reaction):
            #Wird nur ausgeführt, wenn es erwünscht ist
            role_name = from_raction_get_role(client, reaction)
            role = discord.utils.get(user.guild.roles, name=role_name)

            if not user_has_role(user, role):
                #Benutzer hat die Rolle noch nicht
                try:
                    await user.add_roles(role)
                    text = str(added_role()+user.name)
                    channel = client.get_channel(int(Channel_ID('vote')))
                    await channel.send(text)
                except discord.Forbidden:
                    channel = client.get_channel(int(Channel_ID('vote')))
                    await channel.send(error1(6))
                    return
            else:
                text = str(already_has_role_text(1) + user.name + \
                           already_has_role_text(2)+ role.name)
                channel = client.get_channel(int(Channel_ID('vote')))
                await channel.send(text)
                channel_name = channel.name
                text = str(error1(9) + channel_name + text)
                await give_text_in_bot_channel(client, text)
        else:
            return


