"""
User feed suggestions service

MODULES:
    - typing: List, Optional
    - models.project: ProjectResponse
    - models.user: UserResponse
    - services.project_services: ProjectServices
    - services.user_services: UserServices

"""
from typing import List, Optional
from models.projects import ProjectResponse
from models.users import UserResponse
from services.user_services import UserServices
from services.project_services import ProjectServices


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
        user_services = UserServices()
        project_services = ProjectServices()


    async def get_project_suggestions(self, user_id: str):
        """
        Get project suggestions for a user. This is a simple abstract implementation of an alogorithm to generate user feed, a true alogorithm would be more intuitive and deep

        PARAMETERS:
            - user_id: str, user id

        RETURNS:
            - List[ProjectResponse]: list of project objects
        """
        # Get the user to whom the project suggestions are to be made
        user = self.user_services.get_user_by_id(user_id)
        if not user:
            return []
        
        # Make a query using the  user's skills, interests and location.
        filters = {
            "skills": user.skills.extend(user.interests), # Fuse users skills and interests in a single list. user's skills and interests are  almost analogous.
            "location": user.location
        }
        
        # Get projects that match the user's skills, interests and location
        projects = self.project_services.search_projects(filters)

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
        user = self.user_services.get_user_by_id(user_id)
        if not user:
            return []
        
        # Make a query using the  user's skills, interests and location. 
        filters = {  # more filters e.g mutual friends, followers, followings, collabees etc can be added to make the suggestions more accurate
            "skills": user.skills,
            "interests": user.interests,
            "location": user.location
        }
        
        # Get users that match the user's skills, interests and location
        users = self.user_services.search_users(filters)

        return users
