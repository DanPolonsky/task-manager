from server import db
from enum import Enum

class UserPermissions(Enum):
    """
        Enum class for user permissions.
    """
    OWNER = 0
    ADMIN = 1
    MEMBER = 2


class UserProjectAssociation(db.Model):
    __tablename__ = 'user_project_associations'
    user_id = db.Column(db.ForeignKey('users.id'), primary_key=True)
    project_id = db.Column(db.ForeignKey('projects.id'), primary_key=True)
    
    user = db.relationship("User", back_populates="associations", uselist=False)
    project = db.relationship("Project", back_populates="associations", uselist=False)
    
    user_permission = db.Column(db.Enum(UserPermissions), nullable=False)

    def __repr__(self):
        return f"Association <'user: '{self.user}', project: '{self.project}', user-permission: '{self.user_permission}'>"


class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(64), unique=False, nullable=False)
    
    associations = db.relationship("UserProjectAssociation", back_populates="user")

    def __repr__(self):
        return f"User <'email: '{self.email}', username: '{self.username}', password: {self.password}, projects: '{self.associations}>'"


class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(300), unique=False, nullable=True)
    
    associations = db.relationship("UserProjectAssociation", back_populates="project")

    tasks = db.relationship('Task', lazy=True)
    
    def __repr__(self):
        return f"Project <name: '{self.name}', tasks: , users: '{self.associations}>"



class Task(db.Model):
    __tablename__ = "tasks"
    
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.ForeignKey('projects.id'), primary_key=True)
    
    name = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(80), unique=False, nullable=False)
    due_date = db.Column(db.DateTime, default=None, nullable=False)
    
    assignee_id = db.Column(db.ForeignKey('users.id'), primary_key=True)
    assignee = db.relationship('User', uselist=False)

    def __repr__(self):
        return f"Task <name: '{self.name}', description: {self.description}, due_date: {self.due_date}>, assignee: '{self.assignee}'"
    


