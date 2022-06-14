from verify_ip.ext.db import db

class Ips(db.Model):
    __tablename__ = "ips"
    id = db.Column(db.Integer, primary_key=True)
    ip_number = db.Column(db.Unicode)
    ip_status = db.Column(db.Boolean)
    
    def __repr__(self):
        return f'{self.ip_number}'