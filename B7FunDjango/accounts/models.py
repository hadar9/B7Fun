from django.db import models

from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, user_name, first_name, last_name, password,about=None, profile_image=None):
        if not email:
            raise ValueError("user must have an email")
        if not user_name:
            raise ValueError("user must have an user name")
        if not password:
            raise ValueError("user must have password")

        user = self.model(
            email=self.normalize_email(email),
            user_name=user_name,
            first_name=first_name,
            last_name=last_name,
            about=about,
            profile_image=profile_image,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email, user_name, password,first_name=None, last_name=None, ):
        user = self.create_user(
            email=self.normalize_email(email),
            user_name=user_name,
            password=password,
            first_name=first_name,
            last_name=last_name,
            about=None,
            profile_image=None
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    user_name = models.CharField(max_length=30,unique=True, verbose_name="user_name")
    first_name = models.CharField(max_length=30, verbose_name="first name")
    last_name = models.CharField(max_length=30, verbose_name="last name")
    date_joined = models.DateField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateField(verbose_name="last login", auto_now=True)
    about = models.TextField(max_length=500)
    profile_image = models.ImageField(default='default_profile.png', blank=True,upload_to='media')
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name', 'last_name']
    objects = MyUserManager()

    def __str__(self):
        return self.user_name + ' - ' + self.email

    def has_perm(self, perm, obj = None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True