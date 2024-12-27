"""
User feed suggestions service

MODULES:
    - typing: List, Optional
    - models.project: ProjectResponse
    - models.user: UserResponse
    - services.project_service: ProjectService
    - services.user_service: UserService

"""
from typing import List, Optional
from models.project import ProjectResponse
from models.user import UserResponse
from services.user_service import UserService
from services.project_service import ProjectService


class SuggestionServices:
    """
    Suggestion Services class: Includes methods to get user feed suggestions

    ATTRIBUTES:
        - user_service: UserService, user service object
        - project_service: ProjectService, project service object
    
    """

    def __init__(self):
        """Attributes initializer
        """
        user_service = UserService()
        project_service = ProjectService()


    async def get_project_suggestions(self, user_id: str):
        """
        Get project suggestions for a user. This is a simple implementation of an alogorithm to generate user feed, a true alogorithm would be more intuitive and deep

        PARAMETERS:
            - user_id: str, user id

        RETURNS:
            - List[ProjectResponse]: list of project objects
        """
        # Get the user to whom the suggestions are to be made
        user = self.user_service.get_user_by_id(user_id)
        if not user:
            return []
        
        # Make a query using the  user's skills, interests and location. 
        filters = {
            "skills": user.skills.extend(user.interests), # Fuse users and interests in a singlle list. user's skills and interests are  almost analogous.
            "location": user.location
        }
        
        # Get projects that match the user's skills, interests and location
        projects = self.project_service.search_projects(filters)

        return projects

    async def get_user_suggestions(self, user_id: str):
        """
        Get a feed of user suggestions a user would like to collaborate with/invite into their projects. Also a very rudimentary implementation
        
        PARAMETERS:
            - user_id: str, user id

        RETURNS:
            - List[UserResponse]: list of user objects
        
        """
        # Get the user to whom the suggestions are to be made
        user = self.user_service.get_user_by_id(user_id)
        if not user:
            return []
        
        # Make a query using the  user's skills, interests and location. 
        filters = {  # more filters e.g mutual friends, followers, followings, collabees etc can be added to make the suggestions more accurate
            "skills": user.skills,
            "interests": (user.interests),
            "location": user.location
        }
        
        # Get users that match the user's skills, interests and location
        users = self.user_service.search_users(filters)

        return users
