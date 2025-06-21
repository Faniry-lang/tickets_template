from repository import TicketMessageRepository
from entity import TicketMessage

class TicketMessageService:
    def __init__(self):
        self.repository = TicketMessageRepository()

    def save(self, ticketMessage: TicketMessage):
        return self.repository.post(ticketMessage)
    
    def findAll(self) : 
        return self.repository.get()

    def findById(self, id: int) : 
        return self.repository.fetchById(id)
    
    def update(self, ticket: TicketMessage) :
        return self.repository.put(ticket)
    
    def delete(self, ticket: TicketMessage) :
        return self.repository.delete(ticket)


        