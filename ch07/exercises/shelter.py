import time
import uuid

class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.id = uuid.uuid4()
        self.arrived = time.strftime("%d/%m/%Y") #string formatted time
        
def main():
    goobie = Animal("goobie", "dog")
    print(goobie.name, goobie.type, goobie.id, goobie.arrived)
    bug = Animal("bug", "bird")
    print(bug.name, bug.type, bug.id, bug.arrived)
    
main()