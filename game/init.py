# import Settings
import sys
sys.path.append('modules')
sys.path.append('db')
import SentenceGenerator
import Menu
import Rooms
from Player import Player
from Person import Person 

story = ""
# To be implemented later
#accomplishments_limit = 1024
#accomplishments = [accomplishments_limit]
current_person = Person('barkeeper')
#save_file_name = "db/temp.storage"
# Rooms
rooms = Rooms.get_map()
current_room = "outside"
character = Player('brewer', 'bar', rooms)
talked_to_scholar = False
print "Talk to scholar!"
print
print rooms['outside']['description']

print "type help "
# Start the game
while True:
    action = raw_input("> ").strip()
    if action == 'help':
        Menu.get_menu()
# main action source
    elif action == 'quit':
        #Menu.save(save_file_name, accomplishments, character, character.get_location)
        break
    elif action == "exit the Tabord Inn":
        if current_room == "outside":
            print "You are already outside"
        else:
            current_room = "outside"
            print """The Tabard stands before you. It's marked by its swinging sign board,
gaudily done in the Abbot of Hyde's colors. The greatest of the 
great inns all shoved up on each other along South London road. It
dwarves its smalller competitors like the Bull and Feather. It's 
Southwark's finest inn as all know it. Tonight it's full to bursting 
with pilgrims bound Canterbury way. The mud and daub structure with 
exposed timbers stands regally and beckons entry to all who pass by. 
"""
    elif action == "enter the Tabord Inn":
        current_room = "lobby"
        print """The inn is brightly and lively on this summer's eve. The rich timbre of 
drunken song and clink of earth-waren tankards rebound off the walls. 
The peppery smell of many unwashed bodies, and clean horse sweat pervade the
air."""
    elif action == "go to the hearth":
        if current_room == "outside":
            print "You need to go inside first"
        else:
            current_room = "hearth" 
            print """The hearth is wide and open, and dominates the center of the inn's
central hall. It's broad stone flagons are old and crackled with many a
happy fire. Pilgrims from all walks of London town life perch on its wide
berth. The fire is banked low and the rich scent of beeve drippings fill the
the with their smoky goodness."""
    elif action == "go to the bar":
        if current_room == "outside":
            print "You need to go inside first"
        else:
            current_room = "bar"
            print """The bar is a long oaken trestle that stretches along the back of the inn
proper. There are a few stools. Perched on one of them, is scholarly fellow
with an impish grin, and a merry twinkle in his eye. He's strategically
positioned himself near the taps.
"""
    elif action == "talk to scholar":
        if current_room == "outside":
            print "You need to go inside first"
            continue
        if current_room != "bar":
            print "You need to go to the bar"
            continue
        print """His cheeks are ruddy with more than few tankards of good english 
ale. He's a tale spinner for sure. In front of him are an ink pot,
sharp quills at the ready and a large phampilset of foolscrap 
already densely scribbled with his beautiful long hand. """
        talked_to_scholar = True
    elif action == "tell scholar your story":
        if current_room == "outside":
            print "You need to go inside first"
            continue
        if talked_to_scholar == True:
            print "You talked to Scholar"
        else:
            print "You must speak with Scholar first"
            continue
        current_room = "bar"
        print """
I'm gathering tales of good pilgrims now bound to 
see the grave of holy St. Thomas a Beckett. Each man an' woman
has a tale. I'd pay you in cups for your help, good Brewer. 
Your honest face will put them at their ease.
"""
    elif action in character.get_actions():
        character.perform_action(action)
    elif action == 'credits':
        Menu.credits()
# To be implemented later
#    elif action == 'movements':
#        for item in character.get_actions():
#            print item
#    elif action in current_person.get_actions():
#        current_person.perform_action(action)
#    elif action == 'actions':
#        for item in current_person.get_actions():
#            print item
#    elif action == 'save':
#        Menu.save(save_file_name, accomplishments, character, character.get_location)
#    elif action == 'start over':
#        current_person = Person('barkeeper')
#        character.delete_progress()
#        accomplishments = [accomplishments_limit]
#        Menu.restart(save_file_name)
#    elif action == 'where am I':
#        print character.get_location()
# START DEBUG FUNCTIONS
#    elif action == 'change person':
#        current_person.set_person('barkeeper')
#    elif action == 'show rooms':
#        print rooms
#    elif action == 'load':
#        character.get_data()
# END DEBUG FUNCTIONS
    else:
        print "You can't do that here"    
print "bye"
