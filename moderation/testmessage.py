'''-----------------------------------------------------------------
Python Bot "Friedrich Engels" Version 01.02.01
Nachrichtenüberprüfun Version 02.01
von Mark Rygielski

Nachricht auf Unangemessenes Verhalten Testen
Bedeutung: Geschriebenes mit der Blacklist abgleichen
-----------------------------------------------------------------'''


#Setup:
_blacklistname_ = 'blacklist.txt'

#importiere Bibliotheken:
import os, re
#------------------------------------------------------------------



def isBad(message):

    #import Blacklist
    with open (_blacklistname_) as data:
        blacklist_raw = data.read()
        blacklist = set (re.sub("[^\w]", " ",  blacklist_raw).split())
    
    #convert content into Word-list
    content = set( re.sub("[^\w]", " ",  message).split())
    
    #return if content overlaps with blacklist
    return (len(content.intersection(blacklist)) != 0)
