'''-----------------------------------------------------------------
Python Bot "Friedrich Engels" Version 01.01.01
von Mark Rygielski

Enthält alle Textnachrichten
-----------------------------------------------------------------'''


def badmessage():
    return ', you are bad'

def vote_message():
    return 'React to vote: \n everybody: ❌ \n Rabauken: 💡 \n Genossen: 🙅 \n Developer: 🔔'

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

