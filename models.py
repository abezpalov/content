from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

class Article(models.Model):

    id = models.BigAutoField(primary_key=True, editable=False)

    title = models.CharField(max_length=512, db_index=True)
    alias = models.CharField(max_length=512, unique=True)
    intro = models.TextField(null=True, default='')
    content = models.TextField(null=True, default='')

    img_url = models.URLField(null=True, default='')
    img_path = models.ImageField(null=True, default='')

    state = models.BooleanField(default=False, db_index=True)

    created = models.DateTimeField(auto_now_add=True, db_index=True)
    created_at = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.SET(get_sentinel_user),
                                   related_name='+')

    edited = models.DateTimeField(auto_now_add=True, db_index=True)
    edited_at = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.SET(get_sentinel_user),
                                  related_name='+')

    published = models.DateTimeField(null=True, db_index=True)
    published_at = models.ForeignKey(settings.AUTH_USER_MODEL,
                                     on_delete=models.SET(get_sentinel_user),
                                     related_name='+')

    class Meta:
        ordering = ['-created']


