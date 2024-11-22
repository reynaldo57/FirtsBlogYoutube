from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError("the user must be set")
        if not email:
            raise ValueError('the email must be set')
        if not password:
            raise ValueError('the pasword must be set')
        
        email=self.normalize_email(email)
        user= self.model(
            username=username,
            email=email,
            password=password,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user
    

    def create_superuser(self, username, email, password, **extra_field):
        extra_field.setdefault('is_staff', True)
        extra_field.setdefault('is_superuser', True)
        extra_field.setdefault('is_active', True)

        if extra_field.get('is_staff') is not True:
            raise ValueError('The superuser must have is_staff=True')
        if extra_field.get('is_superuser') is not True:
            raise ValueError('the superuser must have is superuser=True')
        
        return self.create_user(
            username,
            email,
            password,
            **extra_field
        )