from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models import CharField, EmailField, BooleanField, IntegerField
from django.db.models import Model,CASCADE
from django.core.validators import MaxValueValidator,MinValueValidator

class UserManager(BaseUserManager):
    def create_user(self, username, email, full_name, mobile, password=None):
        if not email:
            raise ValueError("The Email field must be set.")
        if not username:
            raise ValueError("The Username field must be set.")
        if not full_name:
            raise ValueError("The Full Name field must be set.")
        if not mobile:
            raise ValueError("The Mobile field must be set.")

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            full_name=full_name,
            mobile=mobile,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, full_name, mobile, password=None):
        user = self.create_user(
            username=username,
            email=email,
            full_name=full_name,
            mobile=mobile,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
#======================================================================================================================#
# User
#======================================================================================================================#

class User(AbstractBaseUser):

    class Meta:
        db_table = 'user'

    #------------------------------------------------------------------------------------------------------------------#

    username = CharField(max_length = 255, unique = True)
    full_name = CharField(max_length = 255)
    email = EmailField(max_length = 255, unique = True)
    mobile= IntegerField(verbose_name="Mobile No.",unique=True,validators=[MaxValueValidator(9999999999),MinValueValidator(5000000000)])
    
    is_active = BooleanField(default = True)
    is_admin = BooleanField(default = False)
    is_superuser = BooleanField(default = False)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'full_name','mobile']

    objects = UserManager()


    #------------------------------------------------------------------------------------------------------------------#

    def get_full_name(self) -> str:
        return self.full_name

    #------------------------------------------------------------------------------------------------------------------#

    def get_short_name(self) -> str:
        return self.full_name

    #------------------------------------------------------------------------------------------------------------------#

    def __str__(self) -> str:
        return self.username

    #------------------------------------------------------------------------------------------------------------------#

    @property
    def is_staff(self) -> bool:
        return self.is_superuser

    #------------------------------------------------------------------------------------------------------------------#

    def has_perm(self, perm, obj = None) -> bool:
        return True

    #------------------------------------------------------------------------------------------------------------------#

    def has_module_perms(self, app_label) -> bool:
        return True

#======================================================================================================================#
