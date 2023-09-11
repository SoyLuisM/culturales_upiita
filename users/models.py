from django.db import models
#from django.contrib.auth.models import AbstractUser
from users.myAbstractUser import AbstractUser
#from django.contrib
import uuid

class User(AbstractUser):
    """Define el modelo de inicio se sesion del usuario, hereda de AbstractUser y elimina algunos campos"""   
    id = None
    id_myuser = models.UUIDField(primary_key=True,default=uuid.uuid4())
    first_name = None
    last_name = None
    

class TBL_USUARIOS(models.Model):
    id_tbl_usuario = models.UUIDField(primary_key=True,default=uuid.uuid4)
    nombre = models.CharField(max_length=100,blank=True)
    a_paterno = models.CharField(max_length=100, blank=True)
    a_materno = models.CharField(max_length=100,blank=True)
    img = models.ImageField(upload_to = 'user/', blank= True, null = True)
    val_correo = models.UUIDField(default=uuid.uuid4,editable=False)
    genero = models.CharField(max_length=20, default='Prefiero no decirlo',blank=True)
    id_User = models.OneToOneField(User, on_delete=models.CASCADE, default=1)