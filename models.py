from database import db

class CyberSecurity(db.Model):
    __tablename__ = 'cybersecuritylogin'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

