'''-----------------------------------------------------------------
Python Bot "Friedrich Engels" Version 01.02.01
von Mark Rygielski

Enthält Module fürs Role-Manafgement

-----------------------------------------------------------------'''

import discord, os, re
from discord.utils import get

from serverconfic.ids import Channel_ID
from textoutput.user_messages import vote_message
from textoutput.user_messages import added_role
from textoutput.error_messages import error1
from serverconfic.server import ROLES
from serverconfic.server import EMOJI_LIST
from serverconfic.server import GENERAL_ROLES

from serverconfic.server import give_text_in_bot_channel


#Ermittelt die Rolle, die mit einem Emoji Zusammenhängt
def from_raction_get_role(client, reaction):

    emoji = reaction.emoji
    if reaction.custom_emoji:
        emoji = reaction.emoji.name
        
    for subgroup in ROLES.values():
        for r, e in subgroup.items():
            if e == emoji:
                return r
    give_text_in_bot_channel(client, error1(5))
    return None

def user_has_role(user, role):
    for r in user.roles:
        if r.name == role or r == role:
            return True
    return False


#Tests ob die Reaktion ignoriert werden soll:
def should_ignore_reaction(client, user, reaction):
    
    if user == client.user:
        #test, ob es der Bot selber war
        return True
        
    channel = client.get_channel(int(Channel_ID('vote')))
    if reaction.message.channel != channel:
        #test, ob der richtige Channel
        return True
    else:
        return False

async def give_role(client, user, role, channel, text):
    if is_blocked_user(user):
        return
    if user_has_role(user, role):
        text = str(already_has_role_text(1) + user.name + \
            already_has_role_text(2)+ role.name)
        channel = client.get_channel(int(Channel_ID('vote')))
        await channel.send(text)
        channel_name = channel.name
        text = str(error1(9) + channel_name + text)
        await give_text_in_bot_channel(client, text)
        return
    else:
        try:
            await client.add_roles(user, role)
        except discord.Forbidden:
            channel = client.get_channel(int(Channel_ID('vote')))
            await channel.send(error1(6))
            return
        except:
            give_text_in_bot_channel(client, error1(0))
            return
        
        await client.send_message(user, "Added **{}** to active roles ".format(role_to_add))
        give_text_in_bot_channel(text)

        



def give_general_role(client, user, channel):
    #gives the user the general roles
    number_roles = len(GENERAL_ROLES)
    text = ""
        
    for i in range(0, number_roles):
        role_name = str(GENERAL_ROLES[i])
        role = discord.utils.get(user.guild.roles, name=role_name)
        vote_channel = client.get_channel(int(Channel_ID('vote')))
        if not user_has_role(user, role):
            await give_role(client, user, role, vote_channel, text)
            
            



    
    
