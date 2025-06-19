from entity import User
from service import UserService
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

rows = DBCONNECTOR.fetch("SELECT * FROM user")
print(rows)