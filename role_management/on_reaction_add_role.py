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
from role_management.untis import give_general_role
from role_management.untis import give_role
from serverconfic.server import give_text_in_bot_channel

   
def on_reaction_add_role(client):

    #Die Nachricht, auf die Reagiert werden soll, muss im Cash sein.
    #Daher muss diese nach dem Neustart erneut gesendet werden:
    @client.event
    async def on_ready():
        channel = client.get_channel(int(Channel_ID('vote')))

        #leert den Wahl-Kanal
        print("Started cleanup")
        messages = await channel.history(limit=100).flatten()
        try:
            await channel.delete_messages(messages)
            print("Finished cleaning up {} channel".format(client))
        except discord.Forbidden():
            text = str(error1('4') + channel.name)
            give_text_in_bot_channel(client, text)
        


        
        try:
            await channel.send(vote_message(1))
        except PermissionError:
            text = str(error1(2) + channel.name)
            give_text_in_bot_channel (client, text)
            message = await channel.send(vote_message(2))
        except:
            text = str(error1(0) + 'on reaction_add_role.on_reaction_add_role')
            give_text_in_bot_channel (client, text)         
        
        message = await channel.send(vote_message(2))
        guild = client.get_guild(id = int(Server_ID()))
        number_emoji = len(EMOJI_LIST)
        
        
        for i in range(0, number_emoji):
            emoji_name = EMOJI_LIST[i]
            await message.add_reaction(emoji_name)
            #fügt de Nachricht alle emojis hinzu, die benötigt werden
        

      
    @client.event
    async def on_reaction_add(reaction, user):
        #wird ausgelößt, wenn jemand irgenwo reagiert
        if not should_ignore_reaction(client, user, reaction):
            #Wird nur ausgeführt, wenn es erwünscht ist
            role_name = from_raction_get_role(client, reaction)
            role = discord.utils.get(user.guild.roles, name=role_name)
            text = str(added_role()+user.name)
            channel = client.get_channel(int(Channel_ID('vote')))
            
            await give_role(client, user, role, channel, text)
            await give_general_role(client, user, channel)
            
        else:
            return
