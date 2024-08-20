from django.db import models
from django.utils.text import slugify
from django.urls import reverse  # Import reverse function

# Create your models here.
class categories(models.Model):
    category=models.CharField(max_length=100,default="")
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.category
    
class MediaContent(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.URLField(max_length=800)
    short_video_url = models.URLField(max_length=800)
    video_url = models.URLField(max_length=800)
    slug = models.SlugField(unique=True,default="slug")
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(MediaContent, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('watch', kwargs={'slug': self.slug})