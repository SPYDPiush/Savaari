from .models import User
from typing import Dict
from django.db.utils import IntegrityError

class UserQueryService:
    pass

class UserAtomicService:
    
    @staticmethod
    def create_user(form_data:Dict[str,str])->User:
        try:
            user=User()
            user.username=form_data.get('username')
            user.mobile=form_data.get('mobile')
            user.full_name=form_data.get('full_name')
            user.email=form_data.get('email')
            user.set_password(form_data.get('password'))
            user.save()
            return user
        except IntegrityError as e:
            return "User already exists\n"+str(e)
        except Exception as e:
            return "Provide valid input.\n"+str(e)