from django.db import models
#from django.contrib.auth.models import AbstractUser
from users.myAbstractUser import AbstractUser
#from django.contrib
import uuid

# esta clase define el perfil de usuario y extiende de AbstractUser
# por que solo se necesitaba eliminar los campos de first_name y last_name
# el resto del contenido se podia conservar
class TBL_USUARIOS(models.Model):
    id_tbl_usuario = models.UUIDField(primary_key=True,default=uuid.uuid4)
    
    # img = models.ImageField(upload_to = 'user/', blank= True, null = True)
    val_correo = models.UUIDField(default=uuid.uuid4,editable=False)
    genero = models.CharField(max_length=20, default='Prefiero no decirlo',blank=True)
    


class User(AbstractUser):
    """Define el modelo de inicio se sesion del usuario, hereda de AbstractUser y elimina algunos campos"""   
    id = None
    id_myuser = models.UUIDField(primary_key=True,default=uuid.uuid4())
    first_name = None
    last_name = None
    #myuser_tbl_usuario = models.OneToOneField(TBL_USUARIOS, on_delete=models.CASCADE, related_name='id_myuser')
    nombre = models.CharField(max_length=100,blank=True)
    a_paterno = models.CharField(max_length=100, blank=True)
    a_materno = models.CharField(max_length=100,blank=True)

    
    
    # img = models.ImageField(upload_to = 'user/', blank= True, null = True)
    # val_correo = models.UUIDField(default=uuid.uuid4,editable=False)
    # genero = models.CharField(max_length=20, default='Prefiero no decirlo',blank=True)

# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from django.db import models

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError("The Email field must be set")
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(email, password, **extra_fields)

# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=30, blank=True)
#     last_name = models.CharField(max_length=30, blank=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(auto_now_add=True)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return self.email
