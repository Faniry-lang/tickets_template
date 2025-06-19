from repository import TicketRepository
from entity import Ticket

class TicketService:
    def __init__(self):
        self.repository: TicketRepository = TicketRepository()

    def save(self, ticket: Ticket) :
        self.repository.post(ticket)

    def findAll(self) : 
        return self.repository.get()

    def findById(self, id: int) : 
        return self.repository.fetchById(id)
    
    def update(self, ticket: Ticket) :
        return self.repository.put(ticket)
    
    def delete(self, ticket: Ticket) :
        return self.repository.delete(ticket)


        