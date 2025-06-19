class Ticket:
    def __init__(self, data: dict):
        self.id = data.get('id')
        self.ref = data.get('ref')
        self.subject = data.get('subject')
        self.message = data.get('message')
        self.status = data.get('status') or data.get('fk_statut')
        self.progress = data.get('progress')
        self.date_creation = data.get('date_creation') or data.get('datec')
        self.date_modification = data.get('date_modification') or data.get('tms')
        self.date_cloture = data.get('date_cloture') or data.get('date_close')
        self.fk_user_create = data.get('fk_user_create')
        self.fk_user_assign = data.get('fk_user_assign')
        self.fk_user_assign_string = data.get('fk_user_assign_string')
        self.category_code = data.get('category_code')
        self.category_label = data.get('category_label')
        self.type_code = data.get('type_code')
        self.type_label = data.get('type_label')
        self.severity_code = data.get('severity_code')
        self.severity_label = data.get('severity_label')
        self.timing = data.get('timing')
        self.email_from = data.get('email_from')
        self.messages = data.get('messages') or []

    def __repr__(self):
        return (f"id={self.id!r}, ref={self.ref!r}, subject={self.subject!r}, "
                f"status={self.status!r}, assigned_to={self.fk_user_assign_string!r}")
    
    def to_dict(self):
        return {k: v for k, v in {
            "id": self.id,
            "ref": self.ref,
            "subject": self.subject,
            "message": self.message,
            "status": self.status,
            "progress": self.progress,
            "date_creation": self.date_creation,
            "date_modification": self.date_modification,
            "date_cloture": self.date_cloture,
            "fk_user_create": self.fk_user_create,
            "fk_user_assign": self.fk_user_assign,
            "category_code": self.category_code,
            "type_code": self.type_code,
            "severity_code": self.severity_code,
            "timing": self.timing,
            "email_from": self.email_from
        }.items() if v is not None}