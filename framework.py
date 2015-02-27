
class Settings:
	def save_game():
	def load_game():
	def display_story():
	def restart():

# The barkeep is Chaucer

class Bar:
	current_question = ""
	person_talked_to = ""
	# tell barkeep story
	# barkeep asks question
	# remark from barkeep for correct 
	# remark from barkeep for incorrect
	# story content added by the barkeep
	def give_player_beer(self, player, person_to):
	def deny_beer(self, player, person_to):
	def ask_questions(self, player, person_about):
	def correct_remark(self, player, person_about):
	def incorrect_remark(self, player, person_about)
	# calls Settings.save
	def write_excerpt_to_story(self)

class Player:
	progress = int()
	def get_beer(self, person_about)
	def give_beer(self, person_about)
	def get_people_seen(self)
		# iterate people seen
	def add_people_seen
	def stories_told
	def add_story_told
	def get_progress
	def set_progress
	

class Person:
	description = text
	name = text
	def give_beer
	def read_all_story
	def read_more_story
	def get_story_contents
	def give_description
	def give_name
	def say_goodbye

# enter room
# find out about people there
# talk to everybody and then talk about everyone you talked to
# reward is beer * meets object criteria
#	- 

people = {
	miller : 
}

framework = {
	player : {
	
	},
	rooms : {
		# bar, fire-room, outside, stable
		# each room has 
		room1 : {
			# big open hearth in the middle of the room
			room_description : text,
			# these four directions represent the places you can go
			paths : { 
				person1 : "miller",
				person2 : "knight",
				person3 : "wife of bath"
			},
			people : {
				# miller is the important one
				person : {
					# story is around 3-4 paragraphs
					story : text,
					after_story_quotes : [
						"quote 1", "quote 2", "quote 3"
					],
					# boolean is true or false
					has_story_been_told : boolean,
					question_to_add : text,
					question_points : range(3)
				}
			}
		}
	}
}



def show_path():
	# get the room from the frame
	# show room left, right [,

class menu:
	def safe();
	def load():
	def help():
	def history():
	def extras():
	# make the save function
	# make the

def story_intro():
	# show the exerpt for the story setting

def player_init():
	menu_init()
	# get name 
	# put out excerpt
	# set player in lobby of hostel
	story_intro()
	show_path()
