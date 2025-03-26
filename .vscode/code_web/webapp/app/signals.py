from django.contrib.auth.models import User, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def add_default_permissions(sender, instance, created, **kwargs):
    if created:  # Chỉ cấp quyền khi user mới được tạo
        permission = Permission.objects.get(codename="add_post")
        instance.user_permissions.add(permission)
