class Player:
    # Create player's name
    def __init__(self, name, location, rooms):
        self.name = name
        self.location = location
        self.rooms = rooms
    def get_name(self):
        return self.name
    def get_actions(self):
        result = list(enumerate(self.rooms[self.location]['actions']))
        for k, v in result:
            result[k] = v
        return result
    def perform_action(self, action):
        if(action in self.get_actions()):
            self.move_to(action)
    def move_to(self, place):
        if place == self.location:
            print "You're already there..."
            return False
        rooms = list(enumerate(self.rooms))
#       for k, v in rooms:
#           if action == "leave bar":
    def get_location(self):
        return "currently located in: " + self.location
    def get_data(self):
        result = self.name \
        + '\n' + self.location \
        + '\n' + " ".join(self.directions)
        print result 
        return result