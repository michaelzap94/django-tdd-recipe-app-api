from django.db import models
# extend django user model AND CREATE YOUR OWN user model.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin

# Manager class -> can create a user or super user


class UserManager(BaseUserManager):

    # Override the create_user function
    # Creates a NORMAL user
    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if(not email):
            raise ValueError('All users must have an email address')
        # creates a new User Model and assign it to the variable user
        # self.normalize_email(email) is a helper function that comes with the BaseUserManager and
        # will normalize(make sure @ANY.COM) is case insensitive
        # CALLS/Uses the User Model/table/schema we defined below
        user = self.model(email=self.normalize_email(email), **extra_fields)

        user.set_password(password)  # built-in: encrypt the password
        user.save(using=self._db)  # Save the model supports multiple dbs,

        return user  # This user will be the MODEL itself.
    # Override the create_superuser function
    # Creates a super user, -> usually used within the command line

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        # Special part about saving a superuser
        user.is_superuser = True
        user.save(using=self._db)

        return user

# This is the class MODEL/TABLE/SCHEMA


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)  # if user is active keep him, default = True
    is_staff = models.BooleanField(default=False)  # if staff, set this to true

    # Creates a new UserManager Model for our objects
    # SO, when we call this User class,
    # we have access to all of the User details(columns) we define in this Model/table
    objects = UserManager()

    USERNAME_FIELD = 'email'  # Make the username field be the email
