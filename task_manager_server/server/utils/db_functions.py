from server.models import User, Project, UserProjectAssociation, UserPermissions
from server.utils.utils import hash_password
from server import db



class UserQueries:
    """
        A static class containing db user functions.
    """

    def get_user_by_email(email: str) -> User:
        """ Function gets a user from the database using email.

        Args:
            email (str): The user's email.

        Returns:
            User: The user object.
        """
        return User.query.filter(User.email == email).first()

    
    def get_user_by_username(username: str) -> User:
        """ Function gets a user from the database using username.

        Args:
            username (str): The user's username.

        Returns:
            User: The user object.
        """
        return User.query.filter(User.username == username).first()


    def get_user_by_id(id: str) -> User:
        """ Function gets a user from the database using id.

        Args:
            id (str): The user's id.

        Returns:
            User: The user object.
        """
        return User.query.filter(User.id == id).first()


    def create_user(email: str, username: str, password: str) -> User:
        """ Function creates a new user in database with the provided data.

        Args:
            email (str): The user's email.
            username (str): The user's username.
            password (str): The user's plane password.
        
        Returns:
            User: The created user.

        """

        hashed_password = hash_password(password)

        user = User(
            email=email,
            username=username,
            password=hashed_password,
        )

        db.session.add(user)
        db.session.commit()
        
        return user

    
    def create_project(user_id: int, project_name: str) -> Project:

        """ Function creates a new project in database for the provided user.

        Args:
            user_id (int): The user's id.
            project_name (str): The project's name.
        """
        
        user = UserQueries.get_user_by_id(user_id)

        
        project = Project(
            name=project_name,
        )

        association = UserProjectAssociation(
           project=project,
           user_permission=UserPermissions.OWNER
        )

        user.associations.append(association)
        
        db.session.add(user)
        db.session.commit()

        return project

    def get_user_projects(user_id: int) -> list:
        """ Function gets a list of projects for the provided user.

        Args:
            user_id (int): The user's id.

        Returns:
            list: The list of project objects.
        """
        user = UserQueries.get_user_by_id(user_id)
        
        user_associations = user.associations
        return [association.project for association in user_associations]
        
        

class ProjectQueries:
    """ A static class containing db project functions. """
   
    def get_project_by_id(id: int) -> Project:
        """ Function gets a project from the database using id.

        Args:
            id (int): The project's id.

        Returns:
            Project: The project object.
        """
        return Project.query.filter(Project.id == id).first()


    def get_project_by_name(name: str) -> Project:
        """ Function gets a project from the database using name.

        Args:
            name (str): The project's name.

        Returns:
            Project: The project object.
        """
        return Project.query.filter(Project.name == name).first()



    