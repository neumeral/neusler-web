from django.db import models


class NavItem(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    subtitle = models.CharField(max_length=100, null=True, blank=True)
    link = models.CharField(max_length=100, null=False, blank=False)
    icon = models.CharField(max_length=25, null=True, blank=True)

    has_subnav = models.BooleanField(default=False, null=False)
    parent_id = models.ForeignKey("NavItem", null=True, blank=True, on_delete=models.PROTECT)

    sequence = models.IntegerField(null=True)


class Author(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    image_path = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)


class BlogPost(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    image_path = models.CharField(max_length=100, null=True, blank=True)
    author = models.ForeignKey("Author", null=True, blank=True, on_delete=models.PROTECT)

    body = models.TextField(null=True, blank=True)

    linkedin_link = models.URLField(null=True, blank=True)
    twitter_link = models.URLField(null=True, blank=True)
    comments_count = models.IntegerField(default=0, null=False, blank=False)
    tags = models.CharField(max_length=200, null=True, blank=True)

    is_draft = models.BooleanField(default=False, null=False)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
