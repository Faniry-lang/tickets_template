class User:
    def __init__(self, data: dict):
        self.id = data.get('id')
        self.lastname = data.get('lastname')
        self.firstname = data.get('firstname')
        self.fullname = data.get('fullname') or f"{self.firstname} {self.lastname}".strip()
        self.login = data.get('login')
        self.email = data.get('email')
        self.user_mobile = data.get('user_mobile')
        self.office_phone = data.get('office_phone')
        self.admin = data.get('admin')
        self.user_group_list = data.get('user_group_list')
        self.photo = data.get('photo')
        self.job = data.get('job')

    def __repr__(self):
        return (f"id={self.id!r}, fullname={self.fullname!r}, login={self.login!r}, "
                f"email={self.email!r}, admin={self.admin!r}")

    def to_dict(self):
        return {k: v for k, v in {
            "id": self.id,
            "lastname": self.lastname,
            "firstname": self.firstname,
            "login": self.login,
            "email": self.email,
            "user_mobile": self.user_mobile,
            "office_phone": self.office_phone,
            "admin": self.admin,
            "user_group_list": self.user_group_list,
            "photo": self.photo,
            "job": self.job
        }.items() if v is not None}