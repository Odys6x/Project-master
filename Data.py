import shelve
import user as u
Data = shelve.open("UserData")

class submit(u.User):
    def __init__(self,username,image,time,date,location,reason):
        super().__init__(username)
        self.__image = image
        self.__time = time
        self.__date = date
        self.__location = location
        self.__reason = reason

def set_data(username,image,time,date,location,reason):
    i = submit()
    i.image = image
    i.time = time
    i.date = date
    i.location = location
    i.reason = reason
    Data[username] = i
