from api import API
from entity import Ticket, User
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
