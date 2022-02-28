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
            id (str): The user.

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

    def delete_user(user: User):
        """ Function deletes a user.

        Args:
            user (User): The user to delete.
        """
        db.session.delete(user)
        db.session.commit()

    
    def create_project(user: User, project_name: str, description: str) -> Project:

        """ Function creates a new project in database for the provided user.

        Args:
            user (int): The user.
            project_name (str): The project's name.
        """
                
        project = Project(
            name=project_name,
            description=description
        )

        association = UserProjectAssociation(
           project=project,
           user_permission=UserPermissions.OWNER
        )

        user.associations.append(association)
        
        db.session.add(user)
        db.session.commit()

        return project

    def get_user_projects(user: User) -> list:
        """ Function gets a list of projects for the provided user.

        Args:
            user (User): The user.

        Returns:
            list: The list of project objects.
        """
        
        user_associations = user.associations
        return [association.project for association in user_associations]
    

    def get_user_project_permission(user: User, project: Project) -> UserPermissions:
        """ Function gets the user's project permission.

        Args:
            user (User): The user.
            project (Project): The project.

        Returns:
            UserPermissions: The user's project permission.
        """
    
        user_associations = user.associations
        for association in user_associations:
            if association.project.id == project.id:
                return association.user_permission



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


    def delete_project(project: Project):
        """ Function deletes a project.

        Args:
            project (int): The project's id.
        """
        db.session.delete(project)
        db.session.commit()