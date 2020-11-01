'''-----------------------------------------------------------------
Python Bot "Friedrich Engels" Version 01.01.01
von Mark Rygielski

Enthält alle Textnachrichten
-----------------------------------------------------------------'''


def badmessage():
    return ', you are bad'

def vote_message(number):
    if number == 1:
        return 'Durch das wählen der Rolle stimmst du zu, die Regeln gelesen und akzeptiert zu haben'
    elif number == 2:
        return 'here: \n everybody: ❌ \n Rabauken: 💡 \n Genossen: 🙅 \n Developer: 🔔 \n Meth: 🎓' 

def added_role():
    return 'added new role to'

def already_has_role_text():
    return 'already has the role'

def already_has_role_text(number):
    if number == 1:
        return " coudn't give role: "
    if number == 2:
        return " already has the role "

def bad_message_detected():
    return " wrote a bad message in the channel: "

def allready_has_role_text(num):
    if num == 1:
        return "Der Idiot"
    if num == 2:
        return "Hat schon die rolle:" 
