# backend/models.py
from extensions import db, bcrypt

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(10), nullable=False, default='user') # 'user' or 'admin'

    skills_offered = db.relationship('Skill', back_populates='offered_by', lazy=True, cascade="all, delete-orphan")
    exchanges_initiated = db.relationship('Exchange', back_populates='requester', lazy=True, cascade="all, delete-orphan")

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

class Skill(db.Model):
    __tablename__ = 'skills'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    offered_by = db.relationship('User', back_populates='skills_offered')
    exchanges = db.relationship('Exchange', back_populates='skill', lazy=True, cascade="all, delete-orphan")

class Exchange(db.Model):
    __tablename__ = 'exchanges'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(20), nullable=False, default='pending') # pending, accepted, completed
    requester_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    skill_id = db.Column(db.Integer, db.ForeignKey('skills.id'), nullable=False)

    requester = db.relationship('User', back_populates='exchanges_initiated')
    skill = db.relationship('Skill', back_populates='exchanges')