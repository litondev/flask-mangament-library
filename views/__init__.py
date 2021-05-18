from .user.web.auth import Auth as UserWebAuth
from .user.actions.auth import Auth as UserActionsAuth
from .user.web.user import User as UserWeb

user_web_auth = UserWebAuth()
"""
 - /signin (GET)
 - /signup (GET)
"""

user_actions_auth = UserActionsAuth()
"""
 - /signin (POST)
 - /signup (POST)
"""

user_web = UserWeb()
"""
 - /user (GET)
"""