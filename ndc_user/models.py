from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.db import models
from membership.models import Membership
from django.conf import settings

class Ndc_user_manager(BaseUserManager):
    def create_user(self, email, first_name,last_name,phone,gender,is_email_verify,password=None):
        """
        Creates and saves a User 
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            phone = phone,
            gender = gender,
            is_email_verify = is_email_verify,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name,last_name,phone,password=None):
        """
        For django-admin purpose only: creates a user who can access django-admin. notice: ndc staff or ndc admin is control by assoc user with role. 
        """
        user = self.create_user(
            email = email,
            first_name = first_name,
            last_name = last_name,
            phone = phone,
            gender = None,
            is_email_verify = True,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Ndc_user(AbstractBaseUser,PermissionsMixin):
    #- ------------------- -
    #- email (aka id) info -
    #- ------------------- -
    email = models.EmailField(max_length=255, unique=True, )
    is_email_verify = models.BooleanField(default=False)
    email_activation_key = models.CharField(blank=True,null=True,max_length=100,unique=True) #this field is only need for non-social-sign-up. this field is generated in the non-social-sign-up-view

    #- ---------- -
    #- basic info -
    #- ---------- -
    create_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    #- --------------- -
    #- membership info -
    #- --------------- -
    phone = models.CharField(max_length=100,blank=True,null=True)
    GENDER_LST = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_LST,blank=True,null=True)
    is_exempt = models.BooleanField(default=False)

    #- ----------------- -
    #- django admin info -
    #- ----------------- -
    #- is_superuser = ... this field exist(without being implicitly declared here) because of PermissionsMixin
    #- is_active: django auth system use is_active = false for the semantic of 'soft removing' a user. 
    #             This buildin auth system use this info to denied login and permission checking
    is_active = models.BooleanField(default=True)
    #- is_staff: django admin system use is_staff field to allow access to the admins site.
    is_staff = models.BooleanField(default=False)

    #- ---------- -
    #- NDC legacy -
    #- ---------- -
    #- ndc_old_id: back_ward_compatability_field for new system work with the old ndc system during updating (old to new system) period.     
    #                 We should remove this field when the old system is fully migrate to the new system
    ndc_old_id = models.CharField(max_length=10,unique=True,blank=True,null=True)
    is_member_old = models.BooleanField(default=False)

    #- --------- -
    #- misc info -
    #- --------- -
    objects = Ndc_user_manager()
    #- REQUIRED_FIELDS : A list of the field names that will be prompted for when creating a user 
    #                    via the createsuperuser management command. The user will be prompted to 
    #                    supply a value for each of these fields. It must include any field for which 
    #                    blank is False or undefined and may include additional fields you want prompted 
    #                    for when a user is created interactively. REQUIRED_FIELDS has no effect in other 
    #                    parts of Django, like creating a user in the admin.
    REQUIRED_FIELDS = ['first_name','last_name','phone']
    #- USERNAME_FIELD : A string describing the name of the field on the User model that is used as the 
    #                   unique identifier. This will usually be a username of some kind, but it can also 
    #                   be an email address, or any other unique identifier.
    USERNAME_FIELD = 'email'

    def get_full_name(self):
        # AbstractBaseUser must implement this get_full_name()
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        # AbstractBaseUser must implement this get_short_name()
        return self.first_name