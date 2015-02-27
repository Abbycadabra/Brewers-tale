class Person:
    def __init__(self, name):
        self.set_person(name)
        # load this from the storage
        self.actions = []
    def set_person(self, name):
        with open("./db/" + name + ".storage", "r+") as handle:
             # print handle.readlines()
             print 
        handle.close()
    def get_person(self, name):
        set_person(name)
    def get_actions(self):
        return self.actions
    def perform_action(self, action_name):
        print action_name
        print self.name  
