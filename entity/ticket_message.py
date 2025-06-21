class TicketMessage:
    def __init__(self, data):
        self.id = data.get("id")
        self.ticket_id = data.get("ticket_id")
        self.sender_id = data.get("sender_id")
        self.sender_role = data.get("sender_role")
        self.message = data.get("message")
        self.attachment_path = data.get("attachment_path")
        self.created_at = data.get("created_at")

    def to_dict(self, include_id=True):
        data = {
            "id": self.id,
            "ticket_id": self.ticket_id,
            "sender_id": self.sender_id,
            "sender_role": self.sender_role,
            "message": self.message,
            "attachment_path": self.attachment_path,
            "created_at": self.created_at
        }
        
        if not include_id:
            data.pop("id", None)
            
        return {k: v for k, v in data.items() if v is not None}
