from __future__ import unicode_literals


from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify



VIEW_STATUS = (
    ('r', 'read'),
    ('u', 'unread'),
)


# Create your models here.

class UserProfile(models.Model):
    url = models.URLField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    icon = models.ImageField(blank=True,upload_to='media/')

class Play(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    logo = models.ImageField(blank=True,upload_to='media/',editable=False)
    play = models.TextField()
    play_image = models.ImageField(blank=True,upload_to='media')
    counter = models.TextField()
    counter_image = models.ImageField(blank=True,upload_to='media')
    hat_tip = models.CharField(max_length=60,blank=True)
    slug = models.SlugField(unique=True,blank=True,editable=False)
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def save(self, *args, **kwargs):
        if not self.id:
            #Only set the slug when the object is created.
            self.slug = slugify(self.title) #Or whatever you want the slug to use
        super(Play, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Submission(models.Model):
    submitter = models.CharField(max_length=200)
    read_by = models.CharField(max_length=1,null=True, blank=True)
    read = models.CharField(max_length=1, choices=VIEW_STATUS, default='u')
    contact = models.EmailField()
    message = models.TextField()
    submitted_date = models.DateTimeField(
            blank=True, null=True)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(ArticleAdmin, self).save_model(request, obj, form, change)

    def __str__(self):
        return self.submitter


