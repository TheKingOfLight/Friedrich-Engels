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

    
