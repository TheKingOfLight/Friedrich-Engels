'''-----------------------------------------------------------------
Python Bot "Friedrich Engels" Version 01.02.03
von Mark Rygielski

Aufgabe:
Unangemessenes Verhalten im Chat erkennen und bestrafen
Bedeutung der Aufgabe in dieser Version
Unangemessenes Verhalten: ein geschriebenes Wort ist auf einer Liste
Bestrafen: im Chat aufmerksam machen
Aufgabe:
Im Chat Reaction von Usern auf eine Nachricht erkennen und entsprechende Rolle
vergeben

Externe Datein (im selben Ordner):
- .ent mit dem Token
-----------------------------------------------------------------'''


#Setup
#------------------------------------------------------------------

#importiere Bibliotheken:
import discord, os, re
from discord.utils import get
from dotenv import load_dotenv

#importiere Python skripte
from moderation.testmessage import isBad
from role_management.on_reaction_add_role import on_reaction_add_role

#importiere Benachrichtigungen
from textoutput.user_messages import badmessage
from textoutput.user_messages import bad_message_detected
from textoutput.error_messages import error1

#importiere Einstellungen
from serverconfic.setup_bot import welcome_client
from serverconfic.server import comandprefix
from serverconfic.server import give_text_in_bot_channel
comand_prefix = str(comandprefix)

#importiere Token mithilfe von dotenv:
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
#------------------------------------------------------------------



def main():
    #client instanz erzeugen:
    client = discord.Client()

    #Stellt den Bot entsprechend ein, gibt Systemnachrichten aus
    welcome_client(client)

    
    @client.event
    async def on_disconnect():
        #Läuft, die Verbindung zum Server abbricht
        print("Bot has logged off")

        
    @client.event
    async def on_message(message):
        #läuft, wenn der Bot eine Nachricht erhält
        if message.author != client.user:
        
            if message.content.startswith(comand_prefix):
                #prüft, ob ein Befehl gegeben wurde
                print ('command')

            #prüft Nachricht
            if isBad(message.content) :
                text = str(message.author.name + badmessage())
                await message.channel.send(text)
                text = str(message.author.name + bad_message_detected() + \
                           message.channel.name)
                await give_text_in_bot_channel(client, text)
            
    on_reaction_add_role(client)
    #------------------------------------------------------------------

       
    #lässt den Client mit dem TOKEN laufen
    client.run(TOKEN)



if __name__ == "__main__":
    main()
