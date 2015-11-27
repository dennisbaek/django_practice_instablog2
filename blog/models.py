from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=2000)
    category = models.ForeignKey('Category')
    tag = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<Post pk:{} // title:{}>'.format(self.pk, self.title)

class Category(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '<Category pk:{} // title:{}>'.format(self.pk, self.title)

class Comment(models.Model):
    post = models.ForeignKey('Post')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<comment pk:{} // content:{}>'.format(self.pk, self.content)

class Tag(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<Tag pk:{} // title:{}>'.format(self.pk, self.title)
