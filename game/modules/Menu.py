# Menu functions
#     print_menu()
#     select_option()
#     save()
#     quit()
#     credits()

def save(save_path, accomplishments, character, room):
	with open(save_path, 'r+') as f:
		try:
			# data extrapalation should occur
			f.write(str(character.get_data))
			f.write(str(room))
		except IOError:
			print "error"
	f.close()

def load(save_path):
	with open(save_path, 'r') as f:
		try:
			print f.readlines()
		except IOError:
			print "error"
	f.close()

def credits():
   print "Created by Abby Hoover"

def get_menu():
    menu_items = [
    	'exit the Tabord Inn',
    	'enter the Tabord Inn',
    	'go to the hearth',
    	'go to the bar',
    	'talk to scholar',
    	'tell scholar your story',
    	'quit'
    ]
    print "Commands Menu:"
    for item in menu_items:
        print "\t" + item
    print "End Commands"

def restart(save_path):
    with open(save_path, 'r+') as f:
        try:
            f.truncate()
        except IOError:
            print "Save failed"
        print "Saved progress erased"
    f.close()