'''-----------------------------------------------------------------
Python Bot "Friedrich Engels" Version 01.02.01
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
from dotenv import load_dotenv

#importiere Python skripte
from moderation.testmessage import testmessage
from on_reaction_add_role import on_reaction_add_role
from setup_bot import start

#importiere Benachrichtigungen
from textoutput.user_messages import badmessage

#importiere Einstellungen
from serverconfic.server import comandprefix
comand_prefix = str(comandprefix)

#importiere Token mithilfe von dotenv:
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
#------------------------------------------------------------------



def main():

    #client instanz erzeugen:
    client = discord.Client()

    #Stellt den Bot entsprechend ein, gibt Systemnachrichten aus
    start(client)

    
    @client.event
    async def on_disconnect():
        #Läuft, die Verbindung zum Server abbricht
        print("Bot has logged off")

        
    @client.event
    async def on_message(message):
        #läuft, wenn der Bot eine Nachricht erhält
        if message.author == client.user:
            #testet, ob der Bot die Nachricht selber gesendet hat
            return
        
        if message.content.startswith(comand_prefix):
            #prüft, ob ein Befehl gegeben wurde
            print ('command')
        
        #nimmt den Nachrichteninhalt als Liste der Wörter
        content = message.content
        wordList = re.sub("[^\w]", " ",  content).split()

        #prüft Nachricht
        if testmessage(content) == 'good':
            return
        elif testmessage(content) == 'bad':
            print ('bad')
            await message.channel.send(badmessage())
        elif testmessage(content) == 'error':      
            print('error')
        else:
            print('error')
    on_reaction_add_role(client)
    #------------------------------------------------------------------

       
    #lässt den Client mit dem TOKEN laufen
    client.run(TOKEN)



if __name__ == "__main__":
    main()
