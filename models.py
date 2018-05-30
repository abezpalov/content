from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

class Article(models.Model):

    id = models.BigAutoField(primary_key=True, editable=False)

    title = models.CharField(max_length=512, db_index=True)
    alias = models.CharField(max_length=512, unique=True)
    intro = models.TextField(null=True, blank=True, default='')
    content = models.TextField(null=True, blank=True, default='')
    description = models.TextField(null=True, blank=True, default='')

    img_url = models.URLField(null=True, blank=True, default='')
    img_path = models.ImageField(null=True, blank=True, upload_to='article/imgs', default='')

    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, default=None,
                               on_delete=models.SET(get_sentinel_user), related_name='+')

    state = models.BooleanField(default=False, db_index=True)

    created = models.DateTimeField(auto_now_add=True, db_index=True)
    edited = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
        verbose_name = 'article'
        verbose_name_plural = 'articles'
        permissions = (('can_publish_articles', 'Can publish articles'),)
