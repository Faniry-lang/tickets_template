from repository import UserRepository
from entity import User

class UserService:
    def __init__(self):
        self.repository: UserRepository = UserRepository()

    def save(self, user: User) :
        self.repository.post(user)

    def findAll(self) : 
        return self.repository.get()

    def findById(self, id: int) : 
        return self.repository.fetchById(id)
    
    def update(self, user: User) :
        return self.repository.put(user)
    
    def delete(self, user: User) :
        return self.repository.delete(user)


        