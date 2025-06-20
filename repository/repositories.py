from api import API, DBCONNECTOR
from entity import Ticket, User, TicketMessage
from api import TicketAPI, UserAPI

class TicketRepository:
    def __init__(self):
        self.api: TicketAPI = TicketAPI(API)

    def get(self):
        raw_datas = self.api.get()
        return [Ticket(data) for data in raw_datas]

    def fetchById(self, id: int):
        raw_data = self.api.getById(id)
        return Ticket(raw_data)

    def post(self, ticket: Ticket):
        return self.api.post(ticket.to_dict())

    def put(self, ticket: Ticket):
        return self.api.put(ticket.to_dict())

    def delete(self, ticket: Ticket):
        return self.api.delete(ticket.to_dict())

    def filter(self, criteria: dict):
        sqlfilters = []

        for key, value in criteria.items():
            if isinstance(value, str):
                condition = f"t.{key}:=:'{value}'"
            else:
                condition = f"t.{key}:=:{value}"
            sqlfilters.append(condition)

        raw_data = self.api.filter(sqlfilters)
        return [Ticket(data) for data in raw_data]


class UserRepository:
    def __init__(self):
        self.api: UserAPI = UserAPI(API)

    def get(self):
        raw_datas = self.api.get()
        return [User(data) for data in raw_datas]

    def fetchById(self, id: int):
        raw_data = self.api.getById(id)
        return User(raw_data)

    def post(self, user: User):
        return self.api.post(user.to_dict()) 

    def put(self, user: User):
        return self.api.put(user.to_dict())

    def delete(self, user: User):
        return self.api.delete(user.to_dict())

    def filter(self, criteria: dict):
        sqlfilters = []

        for key, value in criteria.items():
            if isinstance(value, str):
                condition = f"t.{key}:=:'{value}'"
            else:
                condition = f"t.{key}:=:{value}"
            sqlfilters.append(condition)

        raw_data = self.api.filter(sqlfilters)
        return [User(data) for data in raw_data]


class TicketMessageRepository:
    def __init__(self):
        self.dbconnector = DBCONNECTOR

    def get(self):
        rows = self.dbconnector.fetch("SELECT * FROM ticket_messages")
        return [TicketMessage(data) for data in rows]

    def fetchById(self, id: int):
        rows = self.dbconnector.fetch("SELECT * FROM ticket_messages WHERE id = %s", (id,))
        return TicketMessage(rows[0]) if rows is not None else None

    def post(self, ticketMessage: TicketMessage):
        data = ticketMessage.to_dict(include_id=False)  
        
        if not data:
            raise Exception("No data to insert")
            
        fields = ", ".join(data.keys())
        values = list(data.values())
        values_placeholder = ", ".join(["%s"] * len(values))
        
        query = f"INSERT INTO ticket_messages ({fields}) VALUES ({values_placeholder})"
        return self.dbconnector.execute(query, values)

    def put(self, ticketMessage: TicketMessage):
        if ticketMessage.id is None:
            raise Exception("Can't update TicketMessage with id = None")
            
        data = ticketMessage.to_dict(include_id=False)  
        
        if not data:
            raise Exception("No data to update")
            
        set_statement = ", ".join([f"{key} = %s" for key in data.keys()])
        set_values = list(data.values())
        params = set_values + [ticketMessage.id]  
        
        query = f"UPDATE ticket_messages SET {set_statement} WHERE id = %s"
        return self.dbconnector.execute(query, params)

    def delete(self, ticketMessage: TicketMessage):
        if ticketMessage.id is None:
            raise Exception("Can't delete TicketMessage with id = None")
        return self.dbconnector.execute("DELETE FROM ticket_messages WHERE id = %s", (ticketMessage.id,))


   