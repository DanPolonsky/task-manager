import datetime
from flask_sqlalchemy import SQLAlchemy
from server import db

class UserProjectAssociation(db.Model):
    __tablename__ = 'user_project_associations'
    
    user = db.relationship("User", nullable=False)
    project = db.relationship("Project", back_populates="associations", nullable=False)
    permission = db.Column(db.String(50), back_populates="associations", nullable=False)

    def __repr__(self):
        return f"Association <'user: '{self.user}', project: '{self.project}', permissions: '{self.permission}'>"


class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(64), unique=False, nullable=False)
    associations = db.relationship("UserProjectAssociation", back_populates="user")

    def __repr__(self):
        return f"User <'email: '{self.email}', username: '{self.username}', password: {self.password}, projects: '{self.projects}>'"


class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    owner = db.relationship("User", nullable=False)
    name = db.Column(db.String(80), unique=False, nullable=False)
    associations = db.relationship("UserProjectAssociation", back_populates="Project")
    tasks = db.relationship('Task', backref='Task', lazy=True)

    def __repr__(self):
        return f"Project <name: '{self.name}', tasks: {self.tasks}, owner '{self.owner}', users: '{self.users}>"



class Task(db.Model):
    __tablename__ = "tasks"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(80), unique=False, nullable=False)
    due_date = db.Column(db.DateTime, default=None, nullable=False)
    assignee = db.relationship('User', lazy=True, nullable=True)

    def __repr__(self):
        return f"Task <name: '{self.name}', description: {self.description}, due_date: {self.due_date}>, assignee: '{self.assignee}'"
    