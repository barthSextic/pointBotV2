import Manager as mgr
import CSVHandler as csvh

class Event:
    
    def __init__(self, name : str, db : str, csv = None):
        self.name = name
        self.db = db
        self.csvh = csvh.CSVHandler(csv)
    
    
    # Takes in an event name, database name, and creates a new event.
    # String Format: "EventName, DatabaseName1, DatabaseName2, ..."
    def make(e: str) -> bool:
        mgr.make(e)
        return True


    def remove(e: str) -> bool: 
        pass


    def rename(e: str) -> bool:
        pass    
    
    
    def freeMemory():
        pass
    
    
    def addFromCSV(e) -> bool:
        pass


    def addUser(e: str, user: str) -> bool:
        pass


    def removeUser(e: str, user: str) -> bool:
        pass