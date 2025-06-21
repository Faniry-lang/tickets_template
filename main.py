from entity import User, TicketMessage
from service import UserService, TicketMessageService
from api import DBCONNECTOR

user: User = User({
    'id': '2',
    'lastname': 'Bibi',
    'firstname': 'Super super bg',
    'login': 'super bg.bibi',
    'email': 'bibi@example.com',
    'admin': '0',
    'user_mobile': '+33612345678',
    'office_phone': '0123456789',
    'user_group_list': ['support', 'tech'],
    'photo': None,
    'job': 'Technicien support'
})

# user_service = UserService()
# bibi = user_service.findById(3)
# user_service.delete(bibi)
# users = user_service.findAll()
# print(users)

tm_service = TicketMessageService()
ticketMessage = TicketMessage({
    "ticket_id": 1,
    "sender_id": 1,
    "sender_role": "Agent",
    "message": "coucou les amis",
    "attachment_path": None,
    "created_at": None
})
tm_service.save(ticketMessage)
tickets_messages = tm_service.findAll()
print([t.message for t in tickets_messages])
